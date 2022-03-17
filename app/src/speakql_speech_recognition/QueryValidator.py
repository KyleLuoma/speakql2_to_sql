
from .SpeakqlKeywords import SpeakQlKeywords


class QueryValidator:

    def __init__(self):
        
        self.speakql_keywords = SpeakQlKeywords()

    

    # Scan a segment that was initially separated using the L1 delimiter
    # to verify that it is complete, that is that it contains the minimum
    # keywords required to constitute a valid query.
    def check_l1_segment_has_required_kws(self, segment):

        required_kws = self.speakql_keywords.get_min_kws_for_unbundled()
        segment = segment.split(" ")

        # Indicates if it has minimum required to be considered valid:
        has_required_kws = True

        # Iterate through each possible type of segment (SF, JW, GB, Ord, Hav, Lim)
        for keyword_group in required_kws: 
            has_required_kws = True
            # Iterate through each keyword type in the keyword group. 
            for keyword_type in keyword_group:
                has_keyword = False
                # Iterate through each keyword synonym of type keyword_type
                for keyword in keyword_type:
                    if keyword in segment:
                        has_keyword = True
                        print("Found", keyword)
                        break
                if not has_keyword:
                    has_required_kws = False
            if has_required_kws:
                break
            
        return has_required_kws
        
        



    



