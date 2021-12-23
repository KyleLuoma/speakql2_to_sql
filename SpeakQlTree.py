#lisp_tree = "(selectStatement (querySpecification (tableThenSelectExpression (tableExpression (fromClause (fromKeyword FROM TABLE) (tableSources (tableSource (tableSourceItem (tableName (fullId (uid (simpleId A))))))) (whereKeyword WHERE) (expression (predicate (predicate (expressionAtom (fullColumnName (uid (simpleId A))))) (comparisonOperator =) (predicate (expressionAtom (fullColumnName (uid (simpleId B))))))))) (selectExpression (selectClause (selectKeyword DISPLAY)) (selectElements (selectElement (fullColumnName (uid (simpleId B))))))) selectModifierExpression))"
lisp_tree = "(selectStatement (querySpecification (selectThenTableExpression (selectExpression (selectClause (selectKeyword SELECT)) (selectElements (selectElement (fullColumnName (uid (simpleId A)))) (selectElementDelimiter AND) (selectElement (functionCall (aggregateWindowedFunction SUM (leftParen () (functionArg (fullColumnName (uid (simpleId B)))) (rightParen ))))))) (tableExpression (fromClause (fromKeyword FROM TABLE) (tableSources (tableSource (tableSourceItem (tableName (fullId (uid (simpleId (keywordsCanBeId ONE))))))))))) selectModifierExpression))"

level = 0
class SpeakQlTree:

    def __init__(self):
        self.next_id = 0
        self.tree_nodes = {}
        self.table_select_agg_rules = [
            "selectThenTableExpression",
            "tableThenSelectExpression"
        ]

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

    def print_tree_to_console(self):
        for i in range(0, len(self.tree_nodes)):
            print(self.tree_nodes[i].to_string())
                
    def add_node(self, rule_name, is_root, is_leaf, depth):
        parent = -1
        if self.next_id == 1 and self.tree_nodes[0].depth == depth - 1:
            self.tree_nodes[0].add_child(1)
            parent = 0
        for i in range(len(self.tree_nodes) - 1, 0, -1):
            if self.tree_nodes[i].depth == depth - 1:
                self.tree_nodes[i].add_child(self.next_id)
                parent = i
                break
        self.tree_nodes[self.next_id] = SpeakQlNode(
            self.next_id,
            rule_name,
            is_root,
            is_leaf,
            depth,
            parent
        )
        self.next_id = self.next_id + 1

    def replace_keywords_for_rule_name(self, rule_name, new_keyword):
        for i in range(0, len(self.tree_nodes)):
            if rule_name in self.tree_nodes[i].get_rule_name():
                self.tree_nodes[i].update_rule_name(
                    rule_name + " " + new_keyword
                )       

    def scan_serialize_leafs(self):
        output = ""
        for i in range(0, len(self.tree_nodes)):
            if self.tree_nodes[i].get_is_leaf():
                output = output + self.get_token_string_from_rule(self.get_node(i))
        return output

    def get_token_string_from_rule(self, node):
        rule_split = node.get_rule_name().split()
        rule_string = ""
        for rule in rule_split[1:]:
            rule_string = rule_string + rule + " "
        return rule_string

    def preorder_serialize_tokens(self, node_id, input = ""):
        output = input
        node = self.get_node(node_id)
        if node.get_is_leaf():
            return self.get_token_string_from_rule(node)
        if len(node.get_rule_name().split()) > 1:
            output = output + self.get_token_string_from_rule(node)
        for child in node.get_children():
            output = output + self.preorder_serialize_tokens(child)
        return output

    def get_all_select_elements(self, node_id = 0, check_subqueries = False):
        elements = []
        node = self.get_node(node_id)
        if "selectElements" in node.get_rule_name():
            new_elements = self.preorder_serialize_tokens(node_id).split(',')
            for element in new_elements:
                elements.append(element.strip())
            return elements
        elif "subQueryTable" in node.get_rule_name() and not check_subqueries:
            return elements
        else:
            for child in node.get_children():
                elements = elements + self.get_all_select_elements(child)
            return elements

    def get_all_table_names(self, node_id = 0, check_subqueries = False):
        table_names = []
        node = self.get_node(node_id)
        if "tableName" in node.get_rule_name():
            table_names.append(self.preorder_serialize_tokens(node_id))
            return table_names
        else:
            for child in node.get_children():
                table_names = table_names + self.get_all_table_names(child)
            return table_names

    def get_all_table_aliases(self, node_id = 0, check_subqueries = False):
        table_aliases = []
        node = self.get_node(node_id)
        if "tableAlias" in node.get_rule_name():
            table_aliases.append(self.preorder_serialize_tokens(node_id).split()[1])
            return table_aliases
        elif "subQueryTable" in node.get_rule_name() and not check_subqueries:
            return table_aliases
        else:
            for child in node.get_children():
                table_aliases = table_aliases + self.get_all_table_aliases(child)
            return table_aliases

    def get_select_elements_by_table(self, node_id = 0):
        table_elements = { }
        alias_name = ""
        table_name = ""
        node = self.get_node(node_id)
        for rule in self.table_select_agg_rules:
            if rule in node.get_rule_name():
                select_elements = self.get_all_select_elements(node_id)
                try: #to get table names, print warning to console if none exist
                    table_name = self.get_all_table_names(node_id)[0].strip()
                except:
                    print("Warning: expected table name but found none!")
                try: #to get alias names, pass if none exist
                    alias_name = self.get_all_table_aliases(node_id)[0].strip()
                except:
                    pass
                if len(alias_name) > 0:
                    table_elements[alias_name] = select_elements
                else:
                    table_elements[table_name] = select_elements
                # Uncommenting this also gets the subquery tables and children
                # I don't think this is what we want. Some external method should call
                # get_select_elements_by_table(node id of subquery).
                # This should enable subquery translation as a seperate process from the
                # main query.
                # for child in node.get_children():
                #     if child > self.find_node_by_rule_name("subQueryTable", child):
                #         table_elements.update(self.get_select_elements_by_table(child))
                return table_elements
    
        for child in node.get_children():
            table_elements.update(self.get_select_elements_by_table(child))
        return table_elements

    def find_node_by_rule_name(self, rule_to_find, node_id = 0):
        node = self.get_node(node_id)
        if rule_to_find in node.get_rule_name():
            return node_id
        elif not node.get_is_leaf():
            for child in node.get_children():
                return self.find_node_by_rule_name(rule_to_find, child)
        else:
            return -1

    def reorder_select_and_table_expressions(self, node_id):
        node = self.get_node(node_id)
        select_expression = -1
        table_expression = -1
        select_modifier_expression = -1
        new_children = []
        for child in node.get_children():
            if "selectExpression" in self.get_node(child).get_rule_name():
                select_expression = child
            if "tableExpression" in self.get_node(child).get_rule_name():
                table_expression = child
            if "selectModifierExpression" in self.get_node(child).get_rule_name():
                select_modifier_expression = -1
        if select_expression > table_expression:
            for child in node.get_children():
                if child != table_expression and child != select_expression:
                    new_children.append(child)
                if child == table_expression:
                    new_children.append(select_expression)
                if child == select_expression:
                    new_children.append(table_expression)
            if select_modifier_expression >= 0:
                new_children.append(table_expression)
            self.get_node(node_id).update_children(new_children)
        for child in node.get_children():
            self.reorder_select_and_table_expressions(child)
        
    def get_node(self, node_id):
        return self.tree_nodes[node_id]



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

    def add_child(self, child_id):
        self.children.append(child_id)

    def add_parent(self, parent_id):
        self.parent = parent_id

    def update_rule_name(self, new_value):
        self.rule_name = new_value

    def update_children(self, new_children):
        self.children = new_children

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

class JoinExpression:

    def __init__(self, from_table, to_table, from_on_attr, to_on_attr, pred):
        self.from_table = from_table
        self.to_table = to_table
        self.from_on_attr = from_on_attr
        self.to_on_attr = to_on_attr
        self.pred = pred

# tree = SpeakQlTree()
# tree.build_tree(lisp_tree)
# print(tree.scan_serialize_leafs())
# tree.replace_keywords_for_rule_name("selectKeyword", "SELECT")
# tree.replace_keywords_for_rule_name("fromKeyword", "FROM")
# tree.replace_keywords_for_rule_name("joinKeyword", "JOIN")
# tree.replace_keywords_for_rule_name("selectElementDelimiter", ",")
# tree.replace_keywords_for_rule_name("leftParen", "(")
# tree.replace_keywords_for_rule_name("rightParen", ")")
# tree.print_tree_to_console()
# print(tree.scan_serialize_leafs())
# print(tree.preorder_serialize_tokens(0))
# tree.reorder_select_and_table_expressions(0)
# print(tree.preorder_serialize_tokens(0))
# print(tree.get_all_select_elements(0))
# print(tree.get_select_elements_by_table(0))
