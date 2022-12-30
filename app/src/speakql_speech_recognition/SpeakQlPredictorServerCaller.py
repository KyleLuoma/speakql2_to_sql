from json import JSONDecoder, JSONEncoder
import requests
from .SpeakQlPredictorCaller import SpeakQlPredictorCaller
import subprocess
import os
from urllib3.exceptions import ProtocolError


class SpeakQlPredictorServerCaller(SpeakQlPredictorCaller):

    def __init__(self):
        print("Working Directory", os.getcwd().replace("\\", "/"))
        self.url = "http://localhost:6789/predict"
        self.PREDICTOR_PATH = os.getcwd().replace("\\", "/") + "/app/bin/"
        self.server_process = subprocess.Popen(
            "java -jar " + self.PREDICTOR_PATH + "speakql_predictor.jar -server",
            shell=True
            )
        print("SpeakQL Predictor jar running as process with PID {}".format(self.server_process.pid))

    def getNextWordsFromQuery(self, query):
        result = requests.post(self.url, json = {'rule': "start", 'query': query})
        print(result.text)
        word_list = result.text.replace("[", "").replace("]", "").replace("'", "").split(", ")
        return word_list

    def getNextWordsFromPartial(self, partial_query, rule):
        result = requests.post(self.url, json = {'rule': rule, 'query': partial_query})
        print(result.text)
        word_list = result.text.replace("[", "").replace("]", "").replace("'", "").split(", ")
        return word_list

    def getLexerTokensFromQuery(self, query):
        return super().getLexerTokensFromQuery(query)

    def get_array_from_result(self, raw_result):
        return super().get_array_from_result(raw_result)

    def kill_server(self):
        print("Shutting down SpeakQL Predictor server jar")
        try:
            requests.post("http://localhost:6789/kill")
        except (ConnectionResetError, ProtocolError, requests.exceptions.ConnectionError):
            print("SpeakQL Predictor seems to have been terminated") 