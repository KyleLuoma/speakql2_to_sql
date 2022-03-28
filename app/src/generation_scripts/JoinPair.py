
class JoinPair:

    def __init__(self, left_table, right_table, left_key, right_key):
        self.left_table = left_table
        self.right_table = right_table
        self.left_key = left_key
        self.right_key = right_key

    def get_left_table_name(self):
        return self.left_table

    def get_right_table_name(self):
        return self.right_table

    def get_left_table_key(self):
        return self.left_key

    def get_right_table_key(self):
        return self.right_key

    def to_string(self):
        return (
            "join " + str(self.left_table) + 
            " with " + str(self.right_table) + 
            " on " + str(self.left_table) + " . " + str(self.left_key) 
            + " equals " + str(self.right_table) + " . " + str(self.right_key)
            )