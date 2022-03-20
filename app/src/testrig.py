from itertools import count
import speakql_translator.SpeakQlParseCaller as spc
import speakql_translator.SpeakQlTree as st
import json
import time
import pandas as pd

from speakql_translator.speakql_to_sql import *

from speakql_speech_recognition.SpeakQlPredictorCaller import *
from speakql_speech_recognition.AsrStringProcessor import *
from speakql_speech_recognition.MicrophoneListener import *
from speakql_speech_recognition.QuerySegment import *

from db_util.db_analyzer import *
from db_util.db_connector import *


def main():

    query = """
               join the department table with the course table on department.id equal course.deptid
                and than
                join the course table with the course offering table on course.id equals course offering.id
                and than
                join the term table with the course offering table on term.id equal to course offering.termid
                and then
                show me department name in the department table
                and then
                get title and units from the course table
                and than
                in course offering show me thin and on days and start time
                end then
                display nothing from the term table where year equals 2022
    """

    asr_response = """show me building number in building name in the building table 
    and then show me area and the count of open parenthesis capacity close parenthesis 
    in the room table and then join the building table with the room table on building. I d equal room. Building ID
    """

    microphone = MicrophoneListener()
    keywords = SpeakQlKeywords()
    preferred_phrases = (
        keywords.get_start_kws() 
        + keywords.get_symbol_text_list()
        + keywords.get_exp_delim_kws()
        )
    asr = AsrStringProcessor(DbAnalyzer(DbConnector()))
    predictor = SpeakQlPredictorCaller()
    error_handler = AsrErrorHandler()
    # analyzer = DbAnalyzer(DbConnector())
    # preferred_phrases = preferred_phrases + analyzer.get_column_names()["COLUMN_NAME"].to_list()
    # preferred_phrases = preferred_phrases + analyzer.get_table_names()["TABLE_NAME"].to_list()
    
    # query = microphone.listen(preferred_phrases)
    # print(query)

    #struct_determination_end_to_end_test(asr_response, asr)

    #get_tokenized_string_from_asr_processor(asr_response)
    
    #asr.process_asr_string(query)

    likenesses = error_handler.find_word_sounds_like_keyword_in_string("select a in one", "FROM TABLE")
    print(likenesses)

    # validator = QueryValidator()
    # segment = QuerySegment("SELECT A FROM ONE AND THE FROM TWO GET B AND C")
    # segment = validator.check_l1_segment_kws(segment)
    # segment.summary()
    
def get_tokenized_string_from_asr_processor(asr_query):
    asr = AsrStringProcessor(DbAnalyzer(DbConnector()))    
    print(asr.get_tokenized_query_string_using_lexer(asr_query))



def struct_determination_end_to_end_test(query, asr):
    l1_clarified = test_clarify_l1_keywords(query, asr)
    l2_clarified = test_clarify_l2_keywords(l1_clarified, asr)
    separated = test_separate_unbundled_queries(l2_clarified, asr)
    print("\n\n Output from l1 splitting:")
    for query in separated:
        segment = QuerySegment(query)
        segment.summary()
        print("")
    separated_query_fragments = []
    print("\n\n Output from l2 splitting:")
    l3_separated = []
    for query in separated:
        query = asr.replace_words_with_symbols(query)
        fragment_dict = test_find_query_fragments(query, asr)
        separated_query_fragments.append(fragment_dict)
        print(fragment_dict)
        if 'select' in fragment_dict.keys():
            fragment_dict['select'] = asr._separate_fragment_by_delimiters(fragment_dict['select'], ["AND", ","])
        if 'where' in fragment_dict.keys():
            fragment_dict['where'] = asr._separate_fragment_by_delimiters(fragment_dict['where'], ["AND", "OR", "XOR"])
        if 'from' in fragment_dict.keys():
            fragment_dict['from'] = asr._separate_fragment_by_delimiters(fragment_dict['from'], ["AND", ","])
        l3_separated.append(fragment_dict)
    print("\n\n Output from l3 splitting:")
    for fragment_dict in l3_separated:
        print(fragment_dict)
    print("\n\n")

    


def test_find_query_fragments(query, asr):
    return asr._separate_spj_parts(query)


def test_separate_unbundled_queries(query, asr):
    return asr._separate_unbundled_query(query)


def test_clarify_l1_keywords(query, asr):
    #query = """select thick and thin from table blah end than from table two show me a and b"""
    return asr._clarify_l1_keywords(query, dist_threshold=0)



def test_clarify_l2_keywords(query, asr):
    return asr._clarify_l2_keywords(query, dist_threshold=0)



def test_process_asr_string(query, asr):
    start_time = time.perf_counter()
    asr.process_asr_string(query)
    end_time = time.perf_counter()
    #print("Total Time for multi-processor:", str(end_time - start_time), "seconds")



def build_trie_using_parser(sentence, predictor, keywords, count = 0, remove_kw = "SELECT"):

    #print(sentence)
    #trie.insert(sentence)
    
    next_words = predictor.getNextWordsFromQuery(sentence)
    already_wrote = False
    for word in next_words:
        count = count + 1
        if count % 100 == 0:
            print("Permutations:", str(count))
            print(sentence)
        if (
            ((sentence.count(word) < 2 or word in ["(", ")"]) or (len(word) > 0 and word[0].islower()))
            and len(sentence.split()) < 16
            and word not in (keywords.get_start_kws() + [
                "WHERE", "LEFT PAREN", "OPEN PAREN", "LEFT PARENTHESIS", "OPEN PARENTHESIS", "RIGHT PAREN", "CLOSE PAREN", "RIGHT PARENTHESIS", "CLOSE PARENTHESIS", "AND", ","
                ])
            and sentence.count("AND") + sentence.count(",") < 4
            and sentence.count(")") < 4
            and sentence.count("(") < 4
            and not (word == "(" and sentence.count("(") - sentence.count(")") > 0 )
        ):
            if len(word) > 0 and word[0].islower():
                insert_word = 'xx'
            else:
                insert_word = word
            count = build_trie_using_parser(sentence + " " + insert_word, predictor, keywords, count, remove_kw)
        start_kws = keywords.get_start_kws()
        start_kws.remove("IN")
        if word in start_kws + ["WHERE"] and not already_wrote:
            f = open("select_element_tokens.txt", "a")
            f.write(sentence.replace(remove_kw, "") + "\n")
            f.close()
            already_wrote = True

    return count

                
                


class TrieNode:
    def __init__(self):
        self.sentence = None
        self.children = {}

        # global NodeCount
        # NodeCount += 1

    def insert( self, sentence ):
        node = self
        for word in sentence:
            if word not in node.children:
                node.children[word] = TrieNode()

            node = node.children[word]

        node.sentence = sentence

    def print_to_console(self):
        if self.sentence != None:
            print(self.sentence)
        for node in self.children.values():
            node.print_to_console()


if (__name__ == "__main__"): main()