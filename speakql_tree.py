lisp_tree = "(selectStatement (querySpecification (selectExpression (selectClause (selectKeyword SELECT)) (selectElements (selectElement (fullColumnName (uid (simpleId A)))))) (tableExpression (fromClause (fromKeyword FROM) (tableSources (tableSource (tableSourceItem (tableName (fullId (uid (simpleId B))))))) WHERE (expression (predicate (predicate (expressionAtom (fullColumnName (uid (simpleId A))))) (comparisonOperator =) (predicate (expressionAtom (fullColumnName (uid (simpleId B))))))))) selectModifierExpression))"
level = 0
class SpeakQlTree:

    tree_nodes = ()

    def __init__(self):
        self.next_id = 0
        self.tree_nodes = {}

    def build_tree(self, lisp_tree):
        is_root = True
        depth = 0
        for i in range (0, len(lisp_tree)):
            rule_name = ""
            is_leaf = False
            if lisp_tree[i] == "(":
                for j in range (i + 1, len(lisp_tree)):
                    if lisp_tree[j] == "(" or lisp_tree[j] == ")":
                        rule_name = lisp_tree[i + 1 : j]
                        is_leaf =  lisp_tree[j] == ")"
                        depth = depth + 1
                        self.add_node(
                            rule_name, is_root, is_leaf, depth
                        )
                        is_root = False
                        i = j + 1
                        break
            elif lisp_tree[i] == ")":
                depth = depth - 1
                

    def add_node(self, rule_name, is_root, is_leaf, depth):
        if self.next_id == 1 and self.tree_nodes[0].depth == depth - 1:
            self.tree_nodes[0].add_child(1)
        for i in range(len(self.tree_nodes) - 1, 0, -1):
            if self.tree_nodes[i].depth == depth - 1:
                self.tree_nodes[i].add_child(self.next_id)
                break
        self.tree_nodes[self.next_id] = SpeakQlNode(
            self.next_id,
            rule_name,
            is_root,
            is_leaf,
            depth
        )
        self.next_id = self.next_id + 1
        


                        


class SpeakQlNode:

    def __init__(self, id, rule_name, is_root, is_leaf, depth):
        self.id = id
        self.rule_name = rule_name
        self.is_root = is_root
        self.is_leaf = is_leaf
        self.depth = depth
        self.children = []

    def to_string(self):
        return(
            "ID:" + str(self.id) + 
            " Rule name: " + self.rule_name + 
            " Depth: " + str(self.depth) +
            " Children:" + str(self.children)
        )

    def add_child(self, child_id):
        self.children.append(child_id)


tree = SpeakQlTree()
tree.build_tree(lisp_tree)
print(tree.tree_nodes[level].to_string())
