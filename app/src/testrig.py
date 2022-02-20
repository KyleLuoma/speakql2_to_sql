import speakql_translator.SpeakQlParseCaller as spc
import speakql_translator.SpeakQlTree as st
import json

from speakql_translator.speakql_to_sql import *

from speech_recognition.SpeakQlPredictorCaller import *
from speech_recognition.AsrStringProcessor import *

from db_util.db_analyzer import *
from db_util.db_connector import *

def main():

    query = """select building name and building number from table building
                and then get capacity from table room
                and then join the building table with the room table on room.building id = building.id
    """

    asr = AsrStringProcessor(DbAnalyzer(DbConnector()))

    print(asr.process_asr_string(
        query
    ))

    # asrmp = AsrMultiProcessor()
    # asrmp.scan_query_with_parser(query.replace(",", " ,").upper())

if (__name__ == "__main__"): main()