
from .SpeakqlKeywords import SpeakQlKeywords


class QueryValidator:

    def __init__(self):
        
        self.speakql_keywords = SpeakQlKeywords()

    

    # Scan a QuerySegment object that was initially separated using the L1 delimiter
    # to verify that it is complete, that is that it contains the minimum
    # keywords required to constitute a valid query,          
    # and to see if more than the allowed number of 
    # keywords exist within the segment. If so, indicates an error.
    def check_l1_segment_kws(self, query_segment):
        kw_count_dict = {
            "SELECT" : 0,
            "FROM" : 0,
            "JOIN" : 0,
            "WITH" : 0,
            "GROUP BY" : 0,
            "ORDER BY" : 0,
            "HAVING" : 0,
            "LIMIT" : 0,
            "NONE" : 0
        }

        tokens = query_segment.get_tokens()

        for token in tokens:
            kw_type = self.speakql_keywords.lookup_kw_synonym(token)
            kw_count_dict[kw_type] = kw_count_dict[kw_type] + 1

        is_sfw_segment = (kw_count_dict["SELECT"] > 0 or kw_count_dict["FROM"] > 0)
        is_join_segment = (kw_count_dict["JOIN"] > 0 or kw_count_dict["WITH"] > 0)
        is_modifier_segment = (
            kw_count_dict["GROUP BY"] > 0
            or kw_count_dict["ORDER BY"] > 0
            or kw_count_dict["HAVING"] > 0
            or kw_count_dict["LIMIT"] > 0
        )

        is_complete = (
            (kw_count_dict["SELECT"] > 0 and kw_count_dict["FROM"] > 0)
            or (kw_count_dict["JOIN"] > 0 and kw_count_dict["WITH"] > 0)
            or is_modifier_segment
        )

        has_illegal_combination = (
            kw_count_dict["SELECT"] > 1
            or kw_count_dict["FROM"] > 1
            or kw_count_dict["JOIN"] > 1
            or kw_count_dict["WITH"] > 1
            or kw_count_dict["GROUP BY"] > 1
            or kw_count_dict["ORDER BY"] > 1
            or kw_count_dict["HAVING"] > 1
            or kw_count_dict["LIMIT"] > 1
            or (is_sfw_segment and is_join_segment)
            or (is_sfw_segment and is_modifier_segment)
            or (is_join_segment and is_modifier_segment)
        )

        is_valid = is_complete and not has_illegal_combination

        print(tokens)
        print(kw_count_dict)
        print("Valid query: ", is_valid)






    



