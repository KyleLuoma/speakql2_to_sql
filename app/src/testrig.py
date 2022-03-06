from itertools import count
import speakql_translator.SpeakQlParseCaller as spc
import speakql_translator.SpeakQlTree as st
import json
import time
import pandas as pd

from speakql_translator.speakql_to_sql import *

from speech_recognition.SpeakQlPredictorCaller import *
from speech_recognition.AsrStringProcessor import *

from db_util.db_analyzer import *
from db_util.db_connector import *


def main():

    query = """
               join the department table with the course table on department.id = course.deptid
                and then
                join the course table with the course offering table on course.id = course offering.id
                and then
                join the term table with the course offering table on term.id = course offering.termid
                and then
                show me department name in the department table
                and then
                get title and units from the course table
                and then
                in course offering find on days and start time
                and then
                display nothing from the term table
    """

    asr = AsrStringProcessor(DbAnalyzer(DbConnector()))

    start_time = time.perf_counter()
    asr.process_asr_string(query)
    end_time = time.perf_counter()
    #print("Total Time for multi-processor:", str(end_time - start_time), "seconds")


    global trie
    count_rows = 0
    trie = TrieNode()
    predictor = SpeakQlPredictorCaller()
    keywords = SpeakQlKeywords()
    #build_trie_using_parser("SELECT", predictor, keywords)
    #print(predictor.getNextWordsFromQuery("SELECT xx XOR xx XOR xx NOT RLIKE xx NOT RLIKE xx MEMBER OF ( xx DIV xx"))
    # trie.print_to_console()




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