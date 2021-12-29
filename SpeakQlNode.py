class SpeakQlNode:

    def __init__(self, id, rule_name, is_root, is_leaf, depth, parent = -1):
        self.id = id
        self.rule_name = rule_name
        self.is_root = is_root
        self.is_leaf = is_leaf
        self.depth = depth
        self.children = []
        self.parent = parent

    def to_string(self):
        return(
            "ID:" + str(self.id) + 
            " Rule name: " + self.rule_name + 
            " Depth: " + str(self.depth) +
            " Children: " + str(self.children) +
            " Parent: " + str(self.parent) +
            " Root: " + str(self.is_root) +
            " Leaf: " + str(self.is_leaf)
        )

    def to_tree_string(self):
        pad = ""
        pad_char = ".."
        for i in range(0, self.depth):
            pad = pad + pad_char
        return pad + self.rule_name

    def add_child(self, child_id):
        self.children.append(child_id)

    def add_parent(self, parent_id):
        self.parent = parent_id

    def update_rule_name(self, new_value):
        self.rule_name = new_value

    def update_children(self, new_children):
        self.children = new_children

    def update_parent(self, new_parent):
        self.add_parent(new_parent)

    def get_children(self):
        return self.children

    def get_parent(self):
        return self.parent

    def get_rule_name(self):
        return self.rule_name

    def get_depth(self):
        return self.depth

    def get_is_root(self):
        return self.is_root

    def get_is_leaf(self):
        return self.is_leaf

    def get_id(self):
        return self.id