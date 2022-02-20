import speakql_translator.SpeakQlParseCaller as spc
import speakql_translator.SpeakQlTree as st
import json
import time

from speakql_translator.speakql_to_sql import *

from speech_recognition.SpeakQlPredictorCaller import *
from speech_recognition.AsrStringProcessor import *

from db_util.db_analyzer import *
from db_util.db_connector import *

def main():

    query = """select the count of ( id ) and building id from the room table 
            and then select the count of ( id ) and building id from the room table 
            and then select the count of ( id ) and building id from the room table 
            and then select the count of ( id ) and building id from the room table 
    """

    asr = AsrStringProcessor(DbAnalyzer(DbConnector()))

    start_time = time.perf_counter()
    print(asr.process_asr_string(
        query
    ))
    end_time = time.perf_counter()
    print("Total Time:", str(end_time - start_time), "seconds")

    # asrmp = AsrMultiProcessor()
    # asrmp.scan_query_with_parser(query.replace(",", " ,").upper())

if (__name__ == "__main__"): main()