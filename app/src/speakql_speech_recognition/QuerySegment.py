
from .SpeakQlPredictorCaller import *
from .SpeakqlKeywords import *

class QuerySegment:

    def __init__(self, segment):
        self.segment = segment
        self.predictor = SpeakQlPredictorCaller()
        self.speakql_keywords = SpeakQlKeywords()
        self.tokens = self.predictor.getLexerTokensFromQuery(segment)
        self.fragments = []

        self.l1_errors = {
            "PARTIAL" : False,
            "ILLEGAL COMBINATION" : False
        }

        self.kw_count_dict = {
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

        self.l1_is_valid = False
        self.is_sfw = False
        self.is_join = False
        self.is_modifier = False

        self._l1_error_check()


    def has_errors(self):
        return (self.l1_errors["PARTIAL"] or self.l1_errors["ILLEGAL COMBINATION"])


    def has_partial_error(self):
        return self.l1_errors["PARTIAL"]


    def get_missing_keyword_list(self):
        if not self.has_partial_error():
            return []
        if self.is_sfw:
            if self.kw_count_dict["SELECT"] == 0:
                return self.speakql_keywords.get_select_kws()
            elif self.kw_count_dict["FROM"] == 0:
                return self.speakql_keywords.get_from_kws()
        elif self.is_join:
            if self.kw_count_dict["JOIN"] == 0:
                return self.speakql_keywords.get_join_kws()
            elif self.kw_count_dict["WITH"] == 0:
                return self.speakql_keywords.get_with_kws()


    def has_illegal_combination_error(self):
        return self.l1_errors["ILLEGAL COMBINATION"]


    def append_fragments(self, fragment_list):
        self.fragments = self.fragments + fragment_list

    
    def append_fragment(self, fragment):
        self.fragments.append(fragment)


    def get_tokens(self):
        return self.tokens


    def get_fragments(self):
        return self.fragments


    def _l1_error_check(self):
        for token in self.tokens:
            kw_type = self.speakql_keywords.lookup_kw_synonym(token)
            self.kw_count_dict[kw_type] = self.kw_count_dict[kw_type] + 1

        self.is_sfw = (self.kw_count_dict["SELECT"] > 0 or self.kw_count_dict["FROM"] > 0)
        self.is_join = (self.kw_count_dict["JOIN"] > 0 or self.kw_count_dict["WITH"] > 0)
        self.is_modifier = (
            self.kw_count_dict["GROUP BY"] > 0
            or self.kw_count_dict["ORDER BY"] > 0
            or self.kw_count_dict["HAVING"] > 0
            or self.kw_count_dict["LIMIT"] > 0
        )

        is_complete = (
            (self.kw_count_dict["SELECT"] > 0 and self.kw_count_dict["FROM"] > 0)
            or (self.kw_count_dict["JOIN"] > 0 and self.kw_count_dict["WITH"] > 0)
            or self.is_modifier
        )

        has_illegal_combination = (
            self.kw_count_dict["SELECT"] > 1
            or self.kw_count_dict["FROM"] > 1
            or self.kw_count_dict["JOIN"] > 1
            or self.kw_count_dict["WITH"] > 1
            or self.kw_count_dict["GROUP BY"] > 1
            or self.kw_count_dict["ORDER BY"] > 1
            or self.kw_count_dict["HAVING"] > 1
            or self.kw_count_dict["LIMIT"] > 1
            or (self.is_sfw and self.is_join)
            or (self.is_sfw and self.is_modifier)
            or (self.is_join and self.is_modifier)
        )

        self.l1_is_valid = is_complete and not has_illegal_combination

        self.l1_errors["PARTIAL"] = not is_complete
        self.l1_errors["ILLEGAL COMBINATION"] = has_illegal_combination


    def summary(self):
        print("Query:", self.segment)
        print("Tokens:", self.tokens)
        print("L1 Errors:", self.l1_errors)
        print("L1 Valid:", self.l1_is_valid)
        print("Is SFW:", self.is_sfw)
        print("Is Join:", self.is_join)
        print("Is Modifier", self.is_modifier)
        
