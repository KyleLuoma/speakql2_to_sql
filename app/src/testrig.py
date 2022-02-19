import speakql_translator.SpeakQlParseCaller as spc
import speakql_translator.SpeakQlTree as st
import json

from speakql_translator.speakql_to_sql import *

from speech_recognition.SpeakQlPredictorCaller import *
from speech_recognition.AsrStringProcessor import *

from db_util.db_analyzer import *
from db_util.db_connector import *

def main():
    asr = AsrStringProcessor(DbAnalyzer(DbConnector()))

    print(asr.process_asr_string(
        """select a from one 
        and then join one with two on one.id = two.id
        and then select b from two"""
    ))

if (__name__ == "__main__"): main()