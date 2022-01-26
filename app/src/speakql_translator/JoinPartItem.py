from .SpeakQlNode import SpeakQlNode

class JoinPartItem:

    def __init__(
        self, from_table_name, join_table_name, join_type = "inner", 
        join_direction = "", from_table_alias = "", join_table_alias = ""
    ):
        self.from_table_name = from_table_name
        self.from_table_alias = from_table_alias
        self.join_type = join_type # inner | outer
        self.join_direction = join_direction # left  | right
        self.join_table_name = join_table_name
        self.join_table_alias = join_table_alias

    def is_equivalent_to(self, compare_jp):
        compare_jp = JoinPartItem()
        #Identical join:
        if (self.from_table_name == compare_jp.get_from_table_name()
            and self.from_table_alias == compare_jp.get_from_table_alias()
            and self.join_type == compare_jp.get_join_type()
            and self.join_direction == compare_jp.get_join_direction()
        ):
            return True
        #Commutative inner join:
        elif (self.from_table_name == compare_jp.get_join_table_name()
            and self.from_table_alias == compare_jp.get_join_table_alias()
            and self.join_table_name == compare_jp.get_from_table_name()
            and self.join_table_alias == compare_jp.get_from_table_alias()
            and self.join_type == "inner" and compare_jp.get_join_type() == "inner"
        ):
            return True
        #Commutative outer join (have to have reverse join direction):
        elif (self.from_table_name == compare_jp.get_join_table_name()
            and self.from_table_alias == compare_jp.get_join_table_alias()
            and self.join_table_name == compare_jp.get_from_table_name()
            and self.join_table_alias == compare_jp.get_from_table_alias()
            and self.join_type == "outer" and compare_jp.get_join_type() == "outer"
            and (
                (self.join_direction == "left" and compare_jp.get_join_direction() == "right")
                or
                (self.join_direction == "right" and compare_jp.get_join_direction() == "left")
            )
        ):
            return True

    def get_commuted_outer_join(self):
        new_join_direction = ""
        if self.join_direction == "left":
            new_join_direction = "right"
        else:
            new_join_direction = "left"
        return JoinPartItem(
            from_table_name = self.join_table_name,
            join_table_name = self.from_table_name,
            join_type = self.join_type,
            join_direction = new_join_direction,
            from_table_alias = self.join_table_alias,
            join_table_alias = self.from_table_alias
        )

    def get_from_table_name(self):
        return self.from_table_name

    def get_from_table_alias(self):
        return self.from_table_alias

    def get_join_table_name(self):
        return self.join_table_name

    def get_join_table_alias(self):
        return self.join_table_alias

    def get_join_type(self):
        return self.join_type

    def get_join_direction(self):
        return self.join_direction

    def set_from_table_name(self, name):
        self.from_table_name = name

    def set_from_table_alias(self, alias):
        self.from_table_alias = alias

    def set_table_two_name(self, name):
        self.join_table_name = name

    def set_table_two_alias(self, alias):
        self.join_table_alias = alias

    def set_join_type(self, joinType):
        self.join_type = joinType

    def set_join_direction(self, direction):
        self.join_direction = direction    

    def as_sql_fragment(self):
        return (
            self.join_type + " " + self.join_direction + 
            " JOIN " + self.join_table_name + " " + 
            self.join_table_alias
        ).strip()