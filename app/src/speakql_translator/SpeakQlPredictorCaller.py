
from json import JSONDecoder, JSONEncoder
from random import randbytes
import subprocess



class SpeakQlPredictorCaller:

    def __init__(self):
        self.PREDICTOR_PATH = "java -jar c:/research_projects/speakql2_to_sql/app/bin/speakql_predictor.jar"

    def getNextWordsFromQuery(self, query):

        raw_result = subprocess.run(
            self.PREDICTOR_PATH + " -predict \"" + query + "\"" ,
            capture_output=True,
        )

        raw_result = str(raw_result)

        array_start = raw_result.find("stdout=b") + len("stdout=b*")
        array_end = raw_result.find("\\r\\n")

        array_string = raw_result[array_start : array_end]

        word_list = array_string.replace("[", "").replace("]", "").replace("'", "").split(", ")
        return word_list

