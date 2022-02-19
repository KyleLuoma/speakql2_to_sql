from .SpeakQlPredictorCaller import *
from speakql_translator.SpeakQlTree import *
from db_util.db_analyzer import *

import pandas as pd
import multiprocessing as mp

class AsrMultiProcessor:

    def process_multi_queries(self, asr_queries):

        mp_pool = mp.Pool(mp.cpu_count())
        results = mp_pool.map(self.do_processing_tasks, [query for query in asr_queries])
        mp_pool.close()
        return results

    def do_processing_tasks(self, query):
        spc = SpeakQlPredictorCaller()
        return spc.getNextWordsFromQuery(query)


# Class used to convert an asr string into a valid speakql query
# Will contain several different methods for performing processing actions
class AsrStringProcessor:

    def __init__(self, db_analyzer):
        self.db_analyzer = db_analyzer
        self.predictor = SpeakQlPredictorCaller()

        print("Number of processors: ", mp.cpu_count())

        self.exp_delims = ["THEN"]

    

    #Current entry point to initiate string processing
    def process_asr_string(self, asr_string):

        amp = AsrMultiProcessor()

        asr_string = asr_string.upper()
        asr_queries = self._separate_unbundled_query(asr_string)

        results = amp.process_multi_queries(asr_queries)
        return results



    def _get_next_words(self, fragment):
        print(fragment)
        next_words = "hello" #self.predictor.getNextWordsFromQuery(fragment)
        return next_words



    def _separate_unbundled_query(self, asr_string):

        unbundled_queries = []

        for delim in self.exp_delims:
            while delim in asr_string:
                unbundled_queries.append(
                    asr_string[0 : asr_string.find(delim) + len(delim)]
                        .replace("AND THEN", "")
                        .replace("THEN", "")
                        .strip()
                )
                asr_string = asr_string[asr_string.find(delim) + len(delim) : ]

        unbundled_queries.append(asr_string.strip())

        return unbundled_queries




    