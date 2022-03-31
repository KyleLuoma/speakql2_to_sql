from .SpeakQlNode import SpeakQlNode

class MultiJoinPartItem:

    def __init__(
        self, join_part_node_id, left_table_name, right_table_name, join_type = "inner", 
        join_direction = "", left_table_alias = "", right_table_alias = ""
    ):
        self.left_table_name = left_table_name
        self.left_table_alias = left_table_alias
        self.join_type = join_type # inner | outer
        self.join_direction = join_direction # left  | right
        self.right_table_name = right_table_name
        self.right_table_alias = right_table_alias
        self.join_part_node_id = join_part_node_id

    def is_equivalent_to(self, compare_jp):
        compare_jp = MultiJoinPartItem()
        #Identical join:
        if (self.left_table_name == compare_jp.get_left_table_name()
            and self.left_table_alias == compare_jp.get_left_table_alias()
            and self.join_type == compare_jp.get_join_type()
            and self.join_direction == compare_jp.get_join_direction()
        ):
            return True
        #Commutative inner join:
        elif (self.left_table_name == compare_jp.get_right_table_name()
            and self.left_table_alias == compare_jp.get_join_table_alias()
            and self.right_table_name == compare_jp.get_left_table_name()
            and self.right_table_alias == compare_jp.get_left_table_alias()
            and self.join_type == "inner" and compare_jp.get_join_type() == "inner"
        ):
            return True
        #Commutative outer join (have to have reverse join direction):
        elif (self.left_table_name == compare_jp.get_right_table_name()
            and self.left_table_alias == compare_jp.get_join_table_alias()
            and self.right_table_name == compare_jp.get_left_table_name()
            and self.right_table_alias == compare_jp.get_left_table_alias()
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
        return MultiJoinPartItem(
            left_table_name = self.right_table_name,
            right_table_name = self.left_table_name,
            join_type = self.join_type,
            join_direction = new_join_direction,
            left_table_alias = self.right_table_alias,
            right_table_alias = self.left_table_alias
        )

    def get_left_table_alias_if_exists_else_name(self):
        if len(self.left_table_alias) > 0:
            return self.left_table_alias
        else:
            return self.left_table_name

    def get_join_part_node_id(self):
        return self.join_part_node_id

    def get_left_table_name(self):
        return self.left_table_name

    def get_left_table_alias(self):
        return self.left_table_alias

    def get_right_table_name(self):
        return self.right_table_name

    def get_join_table_alias(self):
        return self.right_table_alias

    def get_right_table_alias(self):
        return self.right_table_alias

    def get_join_type(self):
        return self.join_type

    def get_join_direction(self):
        return self.join_direction

    def left_table_has_alias(self):
        return len(self.left_table_alias) > 0

    def right_table_has_alias(self):
        return len(self.right_table_alias) > 0

    def set_left_table_name(self, name):
        self.left_table_name = name

    def set_left_table_alias(self, alias):
        self.left_table_alias = alias

    def set_table_two_name(self, name):
        self.right_table_name = name

    def set_table_two_alias(self, alias):
        self.right_table_alias = alias

    def set_join_type(self, joinType):
        self.join_type = joinType

    def set_join_direction(self, direction):
        self.join_direction = direction    

    def as_sql_fragment(self):
        return (
            self.join_type + " " + self.join_direction + 
            " JOIN " + self.right_table_name + " " + 
            self.right_table_alias
        ).strip()