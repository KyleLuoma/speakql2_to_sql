
from app.src.speakql_speech_recognition.SpeakqlKeywords import SpeakQlKeywords


class QueryValidator:

    def __init__(self):
        
        self.speakql_keywords = SpeakQlKeywords()

    
    def check_l1_segment_is_valid(self, seqment):

        required_kws = self.speakql_keywords.get_min_kws_for_unbundled()
        
               
    



