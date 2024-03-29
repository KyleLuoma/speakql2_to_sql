
from json import JSONDecoder, JSONEncoder
#from random import randbytes
import subprocess
from sys import platform



class SpeakQlPredictorCaller:

    def __init__(self):
        self.PREDICTOR_PATH = "java -jar c:/research_projects/speakql2_to_sql/app/bin/speakql_predictor.jar"
        self.END_TEXT = ["\\r\\n"]
        if 'linux' in platform:
            self.PREDICTOR_PATH = "java -jar /root/srv/www/speakql2_to_sql/app/bin/speakql_predictor.jar"
            self.END_TEXT = ["\\n\", stderr=b", "\\n', stderr=b"]
            
    def getNextWordsFromQuery(self, query):

        raw_result = subprocess.run(
            self.PREDICTOR_PATH + " -predict \"" + query + "\"" ,
            capture_output=True,
            shell=True
        )

        raw_result = str(raw_result)

        array_start = raw_result.find("stdout=b") + len("stdout=b*")

        array_end = ""

        for option in self.END_TEXT:
            if option in raw_result:
                array_end = raw_result.find(option)
                break

        array_string = raw_result[array_start : array_end]

        word_list = array_string.replace("[", "").replace("]", "").replace("'", "").split(", ")
        return word_list

    

    def getLexerTokensFromQuery(self, query):

        ignore_tokens = ["\\\\n", ""]

        query = query.upper().replace("\n", "")

        raw_result = subprocess.run(
            self.PREDICTOR_PATH + " -tokenize \"" + query + "\"",
            capture_output=True,
            shell=True
        )

        print("DEBUG:", raw_result)

        array_string = self.get_array_from_result(raw_result)
        raw_token_list = array_string.replace("[", "").replace("]", "").replace("\"", "").split(", ")

        token_list = []

        for token in raw_token_list:
            if token.strip() not in ignore_tokens:
                token_list.append(token.strip())

        return token_list


    def get_array_from_result(self, raw_result):
        result = str(raw_result)
        array_start = result.find("stdout=b") + len("stdout=b*")
        array_end = result.find("\\r\\n")
        array_string = result[array_start : array_end]
        return array_string


