
from .SpeakQlPredictorCaller import *

class QuerySegment:

    def __init__(self, segment):
        self.segment = segment
        self.predictor = SpeakQlPredictorCaller()
        self.tokens = self.predictor.getLexerTokensFromQuery(segment)

        self.l1_errors = {
            "PARTIAL" : False,
            "ILLEGAL COMBINATION" : False
        }

        self.is_valid = False
        self.is_sfw = False
        self.is_join = False
        self.is_modifier = False

    
    def get_tokens(self):
        return self.tokens

    def summary(self):
        print("Query:", self.segment)
        print("Tokens:", self.tokens)
        print("L1 Errors:", self.l1_errors)
        print("L1 Valid:", self.is_valid)
        print("Is SFW:", self.is_sfw)
        print("Is Join:", self.is_join)
        print("Is Modifier", self.is_modifier)
        
