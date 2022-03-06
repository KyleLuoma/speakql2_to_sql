from .SpeakQlPredictorCaller import *
from speakql_translator.SpeakQlTree import *
from .SpeakqlKeywords import *
from db_util.db_analyzer import *
from pyphonetics import Metaphone

import pandas as pd
import multiprocessing as mp
import time

#Class used to handle unbundled queries at the sub-query level using multi-processing
class AsrMultiProcessor:

    def __init__(self, column_names, table_names, distinct_values):
        self.column_names = column_names
        self.table_names = table_names
        self.distinct_values = distinct_values
        self.max_lookahead = 4

    def process_multi_queries(self, asr_queries):
        
        mp_pool = mp.Pool(mp.cpu_count())
        results = mp_pool.map(self.do_processing_tasks, [query for query in asr_queries])
        mp_pool.close()
        return " AND THEN ".join(results)


    #This is the function that is included in the multiprocessing pool, and should be used
    #to define the operations performed on each subquery.
    def do_processing_tasks(self, query):

        query = query.replace(",", " ,")
        query = query.replace(".", " . ")
        query = query.replace("(", " ( ")
        query = query.replace(")", " ) ")
        query = query.replace("\"", " \" ")
        query = query.replace("'", " ' ")
        result = self.scan_query_with_parser(query)

        return result


    #This is the naive approach, we can use it as a baseline for more optimal methods.
    #Also, maybe use it as a last resort fallback if other methods fail to extract
    #a valid speakql query.
    def scan_query_with_parser(self, query):

        keywords = SpeakQlKeywords()
        spc = SpeakQlPredictorCaller()

        #Identify SFW structure within query
        words = query.split()
        speakql_query = ""
        print(words)

        #Start the process by finding the starting keyword at the beginning of the asr text
        for i in range(4, 0, -1):
            if i < len(words):
                candidate_phrase = " ".join(words[0 : i])
                if candidate_phrase in keywords.get_start_kws():
                    speakql_query = speakql_query + candidate_phrase
                    words = words[i  : ]
                    break
                elif i == 0:
                    speakql_query = speakql_query + candidate_phrase

        #scan the rest of the query:
        timeout = 30
        
        while len(words) > 0 and timeout > 0:
            added_word = False
            start_time = time.perf_counter()
            next_keywords = spc.getNextWordsFromQuery(speakql_query)
            end_time = time.perf_counter()
            #print("Time to fetch next words for", speakql_query, "is", str(end_time - start_time))
            
            for literal_kw in keywords.get_literal_kws():
                if literal_kw in next_keywords:
                    next_word_can_be_literal = True
                    next_keywords = next_keywords + self.table_names.TABLE_NAME.str.upper().to_list()
                    next_keywords = next_keywords + self.column_names.COLUMN_NAME.str.upper().to_list()

            #Be greedy, look ahead and consider joined string for multi-word keywords  (i.e. what is the)
            for i in range(self.max_lookahead, 0, -1):
                if (i) <= len(words):
                    candidate = " ".join(words[ : i])
                    #print("'" + candidate + "'")
                    if candidate in next_keywords:
                        speakql_query = speakql_query + " " + candidate
                        words = words[i  : ]
                        added_word = True
                        break
                    elif candidate.replace(" ", "") in next_keywords:
                        speakql_query = speakql_query + " " + candidate.replace(" ", "")
                        words = words[i  : ]
                        added_word = True
                        break
            
            if not added_word:
                timeout = timeout - 1

        if timeout == 0:
            print("WARNING: Query scan timed out!")
            print("TIMED OUT QUERY:", speakql_query)

        #print (next_keywords)
        return speakql_query




    def scan_select_expression(self, select_exp):
        pass

    

    def scan_from_expression(self, table_exp):
        pass



    def scan_where_expression(self, where_exp):
        pass





# Class used to convert an asr string into a valid speakql query
# Will contain several different methods for performing processing actions
class AsrStringProcessor:

    def __init__(self, db_analyzer):
        self.db_analyzer = db_analyzer
        self.predictor = SpeakQlPredictorCaller()
        self.keywords = SpeakQlKeywords()

        print("Number of processors: ", mp.cpu_count())

        self.exp_delims = ["THEN"]

    

    #Current entry point to initiate string processing
    def process_asr_string(self, asr_string):

        amp = AsrMultiProcessor(
            self.db_analyzer.get_column_names(),
            self.db_analyzer.get_table_names(),
            self.db_analyzer.get_distinct_values()
        )

        asr_string = asr_string.upper()
        
        start_time = time.perf_counter()
        asr_queries = self._separate_unbundled_query(asr_string)
        end_time = time.perf_counter()
        print("_separate_unbundled_query() time:", str(end_time - start_time), "seconds")

        start_time = time.perf_counter()
        results = amp.process_multi_queries(asr_queries)
        end_time = time.perf_counter()
        print("Process_multi_queries() time:", str(end_time - start_time), "seconds")
        print(results)

        start_time = time.perf_counter()
        print(amp.do_processing_tasks(asr_string))
        end_time = time.perf_counter()
        print("do_processing_tasks() (single processor) time:", str(end_time - start_time), "seconds")

        return results



    def _get_next_words(self, fragment):
        print(fragment)
        next_words = "hello" #self.predictor.getNextWordsFromQuery(fragment)
        return next_words



    #Pass in ASR transcript and make sure "and then" keywords are correct
    def _clarify_l1_keywords(self, asr_string):
        pass



    def _separate_unbundled_query(self, asr_string):

        unbundled_queries = [asr_string]

        for keyword in self.keywords.get_exp_delim_kws():
            new_unbundled_queries = []
            for query in unbundled_queries:
                while keyword in query:
                    new_unbundled_queries.append(
                        query[ : query.find(keyword)].strip()
                    )
                    query = query[query.find(keyword) + len(keyword) : ]

                new_unbundled_queries.append(query.strip())

            unbundled_queries = new_unbundled_queries

        return unbundled_queries




    