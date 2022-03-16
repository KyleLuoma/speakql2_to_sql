
from SpeakQlPredictorCaller import SpeakQlPredictorCaller

predictor = SpeakQlPredictorCaller()

print(predictor.getLexerTokensFromQuery("select a from table one where b is equal to foo <> = , and thin"))


print(predictor.getLexerTokensFromQuery("""show me building number in building name in the building table 
    and then show me area and the count of open parenthesis capacity close parenthesis 
    in the room table and then join the building table with the room table on building. I d equal room. Building ID
    """))