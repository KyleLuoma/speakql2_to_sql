
from SpeakQlPredictorCaller import SpeakQlPredictorCaller

predictor = SpeakQlPredictorCaller()

assert(predictor.getLexerTokensFromQuery("select a from one") == ["SELECT", "A", "FROM", "ONE"])

