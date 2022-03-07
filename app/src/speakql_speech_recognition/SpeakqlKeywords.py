
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

        self.group_kw = [
            "GROUP",
            "GROUP BY"
        ]

        self.order_kw = [
            "ORDER BY"
        ]

        self.literal_kw = [
            "uid",
            "constant",
            "tableName",
            "tableAlias"
        ]



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
        return self.select_kw + self.from_kw + self.join_kw + self.order_kw + self.group_kw

    def get_literal_kws(self):
        return self.literal_kw