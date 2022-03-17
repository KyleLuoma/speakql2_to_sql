
#Static class for providing keywords for keywords that can divide up a query during structure determination phase
class SpeakQlKeywords:

    def __init__(self):

        self.exp_delim_kw = [
            "AND THEN",
            #"THEN"
        ]

        self.select_kw = [
            "SELECT",
            "RETRIEVE",
            "SHOW ME",
            "DISPLAY",
            "PRESENT",
            "FIND",
            "GET",
            "WHAT IS",
            "WHAT ARE",
            "WHAT IS THE",
            "WHAT ARE THE"
        ]

        self.from_kw = [
            "FROM",
            "FROM TABLE",
            "FROM TABLES",
            "IN",
            "IN TABLE",
            "IN TABLES"
        ]

        self.join_kw = [
            "JOIN",
            "JOIN TABLE",
            "BY JOINING",
            "BY JOINING TABLE",
            "JOINED WITH",
            "JOIN WITH",
            "JOINED WITH TABLE",
            "JOIN WITH TABLE",
            "BY JOINING WITH TABLE",
            "BY JOINING WITH",
            "LEFT JOIN",
            "OUTER JOIN",
            "INNER JOIN",
            "CROSS JOIN",
            "RIGHT JOIN",
            "NATURAL JOIN"
        ]

        self.with_kw = [
            "WITH",
            "WITH TABLE"
        ]

        self.group_kw = [
            "GROUP",
            "GROUP BY"
        ]

        self.order_kw = [
            "ORDER BY"
        ]

        self.having_kw = [
            "HAVING"
        ]

        self.limit_kw = [
            "LIMIT"
        ]

        #Lookup SQL keyword by its SpeakQL synonyms
        self.synonym_to_keyword_dict = {}

        for kw in self.select_kw:
            self.synonym_to_keyword_dict[kw] = "SELECT"
        for kw in self.from_kw:
            self.synonym_to_keyword_dict[kw] = "FROM"
        for kw in self.join_kw:
            self.synonym_to_keyword_dict[kw] = "JOIN"
        for kw in self.group_kw:
            self.synonym_to_keyword_dict[kw] = "GROUP BY"
        for kw in self.order_kw:
            self.synonym_to_keyword_dict[kw] = "ORDER BY"
        for kw in self.having_kw:
            self.synonym_to_keyword_dict[kw] = "HAVING"
        for kw in self.limit_kw:
            self.synonym_to_keyword_dict[kw] = "LIMIT"
        for kw in self.with_kw:
            self.synonym_to_keyword_dict[kw] = "WITH"

        #Each entry in this set represents the minimum kws that must be present
        #in an unbundled query for the query to be considered valid.
        self.min_kws_for_unbundled = [
            [self.select_kw, self.from_kw],
            [self.join_kw, self.with_kw],
            [self.group_kw],
            [self.order_kw],
            [self.having_kw],
            [self.limit_kw]
        ]

        self.literal_kw = [
            "uid",
            "constant",
            "tableName",
            "tableAlias"
        ]

        self.symbols_dict = {
            "plus" : "+",
            "minus" : "-",
            "is less than or equal to" : "<=",
            "less than or equal to" : "<=",
            "is less than" : "<",
            "less than" : "<",
            "is greater than or equal to" : ">=",
            "greater than or equal to" : ">=",
            "is greater than" : ">",
            "greater than" : ">",
            "not equal to" : "<>",
            "equals" : "=",
            "equal to" : "=",
            "equal" : "=",
            "times" : "*",
            " X " : " * ",
            "divided by" : "/",
            "open parenthesis" : "(",
            "close parenthesis" : ")",
            "end quote" : "'",
            "quote" : "'"
        }


    def lookup_kw_synonym(self, kw):
        try:
            return self.synonym_to_keyword_dict[kw]
        except:
            return "NONE"

    def get_min_kws_for_unbundled(self):
        return self.min_kws_for_unbundled

    def get_symbols_dict(self):
        return self.symbols_dict

    def get_symbol_text_list(self):
        key_list = []
        for key in self.symbols_dict.keys():
            key_list.append(key)
        return key_list

    def get_limit_kws(self):
        return self.limit_kw

    def get_having_kws(self):
        return self.having_kw

    def get_group_kws(self):
        return self.group_kw

    def get_order_kws(self):
        return self.order_kw
    
    def get_exp_delim_kws(self):
        return self.exp_delim_kw

    def get_select_kws(self):
        return self.select_kw

    def get_from_kws(self):
        return self.from_kw

    def get_join_kws(self):
        return self.join_kw

    def get_start_kws(self):
        return (
            self.select_kw 
            + self.from_kw 
            + self.join_kw 
            + self.order_kw 
            + self.group_kw 
            + self.having_kw
            + self.limit_kw
        )

    def get_literal_kws(self):
        return self.literal_kw