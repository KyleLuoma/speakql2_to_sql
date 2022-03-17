
import SpeakQlPredictorCaller as spc

class QuerySegment:

    def __init__(self, segment):
        self.segment = segment
        self.predictor = spc.SpeakQlPredictorCaller()
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
