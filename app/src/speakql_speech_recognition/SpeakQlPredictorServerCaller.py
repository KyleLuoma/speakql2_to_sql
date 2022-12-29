from json import JSONDecoder, JSONEncoder
import requests
from .SpeakQlPredictorCaller import SpeakQlPredictorCaller

class SpeakQlPredictorServerCaller(SpeakQlPredictorCaller):

    def __init__(self):
        self.url = "http://localhost:6789/predict"

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