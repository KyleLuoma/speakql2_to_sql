#lisp_tree = "(selectStatement (querySpecification (tableThenSelectExpression (tableExpression (fromClause (fromKeyword FROM TABLE) (tableSources (tableSource (tableSourceItem (tableName (fullId (uid (simpleId A))))))) (whereKeyword WHERE) (expression (predicate (predicate (expressionAtom (fullColumnName (uid (simpleId A))))) (comparisonOperator =) (predicate (expressionAtom (fullColumnName (uid (simpleId B))))))))) (selectExpression (selectClause (selectKeyword DISPLAY)) (selectElements (selectElement (fullColumnName (uid (simpleId B))))))) selectModifierExpression))"
from os import remove
import json
from .TableSourceItem import TableSourceItem
from .MultiJoinPartItem import MultiJoinPartItem
from .SpeakQlNode import SpeakQlNode


lisp_tree = "(selectStatement (querySpecification (selectThenTableExpression (selectExpression (selectClause (selectKeyword SELECT)) (selectElements (selectElement (fullColumnName (uid (simpleId A)))) (selectElementDelimiter AND) (selectElement (functionCall (aggregateWindowedFunction SUM (leftParen () (functionArg (fullColumnName (uid (simpleId B)))) (rightParen ))))))) (tableExpression (fromClause (fromKeyword FROM TABLE) (tableSources (tableSource (tableSourceItem (tableName (fullId (uid (simpleId (keywordsCanBeId ONE))))))))))) selectModifierExpression))"

level = 0
class SpeakQlTree:

    def __init__(self, lisp_tree, verbose = False):
        self.next_id = 0
        self.tree_nodes = {}
        self.table_select_agg_rules = [
            "queryOrderSpecification",
            "multiQueryOrderSpecification"
        ]
        if("(" not in lisp_tree and ")" not in lisp_tree):
            lisp_tree = "(emptyTree)"
        self.parse_tree = lisp_tree
        self._build_tree(self.parse_tree)
        self.properties = self.get_properties_from_parse_tree(self.parse_tree)
        self.initial_table_source_items = self.get_all_table_source_items(
            node_id = 0,
            return_initial_list = False
        )
        self.initial_tables_and_elements = self.get_all_tables_and_elements(0)
        self.table_lookup_by_alias_dict = self._gen_table_lookup_by_alias_dict(
            self.initial_table_source_items
        )
        self.alias_lookup_by_table_dict = self._gen_alias_lookup_by_table_dict(
            self.initial_table_source_items
        )
        self.verbose = verbose



    def _gen_table_lookup_by_alias_dict(self, initial_table_source_items):
        table_lookup_by_alias_dict = {}
        for tsi in initial_table_source_items:
            if tsi.has_alias():
                table_lookup_by_alias_dict[tsi.get_alias()] = tsi.get_name()
        return table_lookup_by_alias_dict



    def _gen_alias_lookup_by_table_dict(self, initial_table_source_items):
        alias_lookup_by_table = {}
        for tsi in initial_table_source_items:
            if tsi.has_alias():
                alias_lookup_by_table[tsi.get_name()] = tsi.get_alias()
        return alias_lookup_by_table



    def set_verbose(self, verbose):
        self.verbose = verbose



    def print_verbose(self, *args):
        if self.verbose:
            print_this = ""
            for arg in args:
                print_this = print_this + str(arg) + " "
            print(print_this)



    def get_properties_from_parse_tree(self, parse_tree):
        properties = {
            "num_joinpart" : 0,
            "num_multijoinpart" : 0,
            "num_non_commutative_join" : 0,
            "num_select_and_table_expression" : 0,
            "num_multi_query_order_specification" : 0, 
            "num_functioncall" : 0,
            "num_table_name" : 0,
            "num_non_right_table_name": 0,
            "num_table_alias" : 0,
            "num_element_alias" : 0,
            "num_group_by" : 0
        }
        properties["num_joinpart"] = parse_tree.count("joinPart")
        properties["num_multijoinpart"] = parse_tree.count("multiJoinPart")
        properties["num_non_commutative_joins"] = parse_tree.count("joinDirection")
        properties["num_select_and_table_expression"] = parse_tree.count("queryOrderSpecification")
        properties["num_multi_query_order_specification"] = parse_tree.count("multiQueryOrderSpecification")
        properties["num_functioncall"] = parse_tree.count("functionCall")
        properties["num_table_name"] = parse_tree.count("tableName")
        properties["num_non_right_table_name"] = (
            parse_tree.count("(tableSource (tableSourceItem (tableName") + 
            parse_tree.count("(tableSourceNoJoin (tableSourceItem (tableName")
        )
        properties["num_table_alias"] = parse_tree.count("tableAlias")
        properties["num_element_alias"] = parse_tree.count("selectElementAs")
        properties["num_group_by"] = parse_tree.count("groupByClause")
        return properties



    def get_properties(self):
        return self.properties



    def _build_tree(self, lisp_tree):
        lisp_tree = lisp_tree.replace("leftParen (", "leftParen")
        lisp_tree = lisp_tree.replace("rightParen )", "rightParen")
        is_root = True
        depth = 0
        i = 0
        while i < len(lisp_tree):
            rule_name = ""
            is_leaf = False
            if lisp_tree[i] == "(":
                for j in range (i + 1, len(lisp_tree)):
                    if lisp_tree[j] == "(" or lisp_tree[j] == ")":
                        rule_name = lisp_tree[i + 1 : j]
                        is_leaf = lisp_tree[j] == ")"
                        self._add_node_during_build(
                            rule_name, is_root, is_leaf, depth
                        )
                        depth = depth + 1
                        is_root = False
                        i = j #+ 1
                        break
            elif lisp_tree[i] == ")":
                depth = depth - 1
                i = i + 1
            elif lisp_tree[i] != " ":
                for j in range (i, len(lisp_tree)):
                    if lisp_tree[j] == "(" or lisp_tree[j] == ")":
                        rule_name = lisp_tree[i : j]
                        is_leaf = True
                        self._add_node_during_build(
                            rule_name, is_root, is_leaf, depth
                        )
                        i = j #+ 1
                        break
            else:
                i = i + 1


            
    def print_tree_to_console(self, node_id = 0):
        node = self.get_node(node_id)
        print(node.to_tree_string())
        for child in node.get_children():
            self.print_tree_to_console(child)



    def _get_next_id_and_increment(self):
        id = self.next_id
        self.next_id = self.next_id + 1
        return id



    def _add_node_under_parent(self, rule_name, is_leaf, depth, parent):
        new_id = self._get_next_id_and_increment()
        self.tree_nodes[new_id] = SpeakQlNode(
            new_id,
            rule_name,
            False,
            is_leaf,
            depth,
            parent
        )
        parent = self.get_node(parent)
        parent.add_child(new_id)
        return new_id
                


    def _add_node_during_build(self, rule_name, is_root, is_leaf, depth):
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



    def scan_serialize_leafs(self):
        output = ""
        for i in range(0, len(self.tree_nodes)):
            if self.tree_nodes[i].get_is_leaf():
                output = output + self.get_token_string_from_rule(self.get_node(i))
        return output



    def get_token_string_from_rule(self, node):
        rule_split = node.get_rule_name().split()
        rule_string = ""
        for rule in rule_split:
            if not rule[0].islower():
                rule_string = rule_string + rule + " "
        return rule_string



    def as_json(self, node_id = 0, at_start = True):
        node = self.get_node(node_id)
        tree_dict = {}
        tree_dict['name'] = node.get_rule_name()
        tree_dict['children'] = []
        for child in node.get_children():
            tree_dict['children'].append(self.as_json(child, at_start = False))
        if at_start:
            return json.JSONEncoder().encode(tree_dict)
        else: 
            return tree_dict



    def preorder_serialize_tokens(self, node_id, input = "", ignore_rules = []):
        output = input
        node = self.get_node(node_id)
        for rule in ignore_rules:
            if rule in node.get_rule_name():
                return output
        if node.get_is_leaf():
            return self.get_token_string_from_rule(node)
        if len(node.get_rule_name().split()) > 1:
            output = output + self.get_token_string_from_rule(node)
        for child in node.get_children():
            output = output + self.preorder_serialize_tokens(child)
        return output



    def preorder_serialize_functioncall(self, functioncall_node_id, table_name = ""):
        node = self.get_node(functioncall_node_id)
        token = ""
        if "fullColumnName" in node.get_rule_name():
            token = self.preorder_serialize_tokens(functioncall_node_id)
            if "." in token:
                return token
            elif len(table_name) > 0:
                return table_name + "." + token
            else:
                return token
        elif node.get_is_leaf():
            return self.get_token_string_from_rule(node)
        if len(node.get_rule_name().split()) > 1:
            token = token + self.get_token_string_from_rule(node)
        for child in node.get_children():
            token = token + self.preorder_serialize_functioncall(child, table_name = table_name)
        return token



    def get_select_elements(
        self, node_id = 0, check_subqueries = False, table_name = "", in_select_element_tree = False
        ):
        elements = []
        ignore = ["selectElementDelimiter"]
        node = self.get_node(node_id)
        if in_select_element_tree and "functionCall" in node.get_rule_name():
            element = self.preorder_serialize_functioncall(node_id, table_name = table_name)
            return [element] #elements.append(element.strip())
        elif in_select_element_tree and "selectElementDelimiter" not in node.get_rule_name():
            element = self.preorder_serialize_tokens(node_id, ignore_rules = ignore)
            if len(table_name) > 0 and "." not in element:
                elements.append(table_name + "." + element.strip())
            else:
                elements.append(element.strip())
            return elements            
        if "subQueryTable" in node.get_rule_name() and not check_subqueries:
            return elements
        if "tableExpression" in node.get_rule_name():
            return elements
        if "tableExpressionNoJoin" in node.get_rule_name():
            return elements
        if "whereExpression" in node.get_rule_name():
            return elements
        if "selectElement" in node.get_rule_name() and "selectElements" not in node.get_rule_name():
            in_select_element_tree = True
        for child in node.get_children():
            elements = elements + self.get_select_elements(
                child, table_name = table_name, in_select_element_tree = in_select_element_tree
                )
        print(elements)
        return elements



    def get_tablesourceitem_by_name_from_initial_list(self, table_name):
        self.print_verbose("Searching for table in initial list by name:", table_name)
        for table in self.initial_table_source_items:
            if table.get_name() == table_name.strip():
                return table    
        raise ValueError()



    def get_tablesourceitem_by_alias_from_initial_list(self, table_alias):
        self.print_verbose("Searching for table in initial list by alias:", table_alias)
        for table in self.initial_table_source_items:
            if table.get_alias() == table_alias.strip():
                return table
        raise ValueError()



    def get_all_table_names(self, node_id = 0, check_subqueries = False):
        table_names = []
        node = self.get_node(node_id)
        if "tableName" in node.get_rule_name():
            table_names.append(self.preorder_serialize_tokens(node_id).strip())
            return table_names
        elif "joinPart" in node.get_rule_name():
            return table_names
        elif "subQueryTable" in node.get_rule_name() and not check_subqueries:
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



    def get_initial_table_source_items_as_json(self):
        table_source_list = []
        table_source_items = self.get_all_table_source_items()
        for item in table_source_items:
            table_source_list.append(item.as_dict())
        return  json.JSONEncoder().encode(table_source_list)



    # Creates a list of all tables and their aliases within a query
    # Examines all possible mentions of tables within the query
    # If a table is referenced without an alias, but then later an alias is assigned
    # to the same table, this will update the existing entry to add the alias.
    # If it finds a subquery, it will label it as SUBQUERY_<ALIAS>
    # Returns: List of TableSourceItem objects, one for each table in a query
    def get_all_table_source_items(self, node_id = 0, at_start_node = True, return_initial_list = True):
        if return_initial_list:
            return self.initial_table_source_items
        table_source_items = []
        node = self.get_node(node_id)
        if "selectExpression" in node.get_rule_name():
            return table_source_items
        if "multiJoinExpression" in node.get_rule_name():
            return table_source_items
        if "tableSourceItem" in node.get_rule_name():
            table_source_item = TableSourceItem()
            for child in node.get_children():
                if "tableName" in self.get_node(child).get_rule_name():
                    table_source_item.set_name(
                        self.preorder_serialize_tokens(child)
                    )
                elif "tableAlias" in self.get_node(child).get_rule_name():
                    alias_token = self.preorder_serialize_tokens(child)
                    alias_token = alias_token.replace("AS", "")
                    table_source_item.set_alias(alias_token)
            if table_source_item.has_alias() and not table_source_item.has_name():
                table_source_item.set_name("_SUBQUERY_" + table_source_item.get_alias())
            table_source_items.append(table_source_item)
            return table_source_items
        for child in node.get_children():
            table_source_items = table_source_items + self.get_all_table_source_items(
                child, at_start_node = False, return_initial_list = return_initial_list
            )
        if at_start_node:
            table_source_items_final = []
            table_names = []
            table_aliases = []
            table_names_final = []
            subquery_count = 0
            for table in table_source_items:
                table_names.append(table.get_name())
                table_aliases.append(table.get_alias())
            for i in range(0, len(table_source_items)):
                table_one = table_source_items[i]
                if table_one.get_name() in table_aliases: 
                    break
                elif len(table_source_items_final) == 0:
                    table_source_items_final.append(table_one)
                    table_names_final.append(table_one.get_name())
                for j in range(0, len(table_source_items_final)):
                    table_two = table_source_items_final[j]
                    if (
                        table_one.get_name() == table_two.get_name()
                        and table_one.has_alias()
                        and not table_two.has_alias()
                    ):
                        table_two.set_alias(table_one.get_alias()) 
                    elif (
                        table_one.get_name() != table_two.get_name()
                        and table_one.get_name() not in table_names_final
                    ):
                        table_source_items_final.append(table_one)
                        table_names_final.append(table_one.get_name())
            return self.remove_duplicates_from_list(table_source_items_final)
        else:
            return self.remove_duplicates_from_list(table_source_items)



    



    def get_initial_tables_and_elements_as_json(self):
        table_list = self.get_all_tables_and_elements(self, initial_list = True)
        tl_for_json = []
        for table in table_list:
            table_dict = table[0][0]
            table_dict["elements"] = table[1]
            tl_for_json.append(table_dict)
        return json.JSONEncoder().encode(tl_for_json)



    def get_all_tables_and_elements(self, node_id = 0, initial_list = False):
        if initial_list:
            return self.initial_tables_and_elements
        node = self.get_node(node_id)
        table_alias_dict = {}
        alias_table_dict = {}
        table_elements = []
        table_dict_list = []
        all_table_source_items = self.get_all_table_source_items(return_initial_list=False)
        for table in all_table_source_items:
            table_alias_dict[table.get_name()] = table.get_alias()
            alias_table_dict[table.get_alias()] = table.get_name()
        for rule in self.table_select_agg_rules:
            if rule in node.get_rule_name():
                local_table_source_items = self.get_all_table_source_items(node_id, return_initial_list=False)
                if len(local_table_source_items) == 0:
                    break
                table_source_item = local_table_source_items[0]
                if (
                    not table_source_item.has_alias() 
                    and table_source_item.get_name() not in table_alias_dict.values()
                ):
                    table_source_item.set_alias(table_alias_dict[table_source_item.get_name()])
                elif (
                    not table_source_item.has_alias()
                    and table_source_item.get_name() in table_alias_dict.values()
                ):
                    table_source_item.set_alias(table_source_item.get_name())
                    table_source_item.set_name(alias_table_dict[table_source_item.get_alias()])
                if self.properties["num_select_and_table_expression"] > 1 or self.properties["num_multi_query_order_specification"] > 0:
                    select_elements = self.get_select_elements(
                        node_id,
                        table_name = local_table_source_items[0].get_alias_if_exists_else_name()
                    )
                    table_dict_list = [table_source_item.as_dict()]
                else:
                    select_elements = self.get_select_elements(node_id)
                    for table in local_table_source_items:
                        table_dict_list.append(table.as_dict())
                table_elements.append([table_dict_list, select_elements])
                return table_elements
        for child in node.get_children():
            table_elements = table_elements + self.get_all_tables_and_elements(child)
        return table_elements


    # -------------------------------------------------------------------------------------------------------
    # Misc Tree Modifiers
    # -------------------------------------------------------------------------------------------------------

    def remove_duplicates_from_list(self, target_list):
        return list(dict.fromkeys(target_list))


    def remove_node_from_tree(self, node_id, remove_siblings = False):
        child = self.get_node(node_id)
        parent = self.get_node(child.get_parent())
        children = parent.get_children()
        self.print_verbose(children)
        if len(children) > 1 and not remove_siblings:
            children.remove(node_id)
            parent.update_children(children)
            self.print_verbose(children)
        else:
            parent.update_children([])
        child.update_parent(-1)



    def surround_node_with_parens(self, node_id):
        node = self.get_node(node_id)
        parent = self.get_node(node.get_parent())
        siblings = parent.get_children()
        left_id = self._add_node_under_parent(
            rule_name = "leftParen (",
            is_leaf = True,
            depth = parent.get_depth() + 1,
            parent = parent.get_id()
        )
        right_id = self._add_node_under_parent(
            rule_name = "rightParen )",
            is_leaf = True,
            depth = parent.get_depth() + 1,
            parent = parent.get_id()
        )
        new_children = []
        for i in range(0, len(siblings)):
            if siblings[i] not in [node_id, left_id, right_id]:
                new_children.append(siblings[i])
            elif siblings[i] == node_id:
                new_children = new_children + [left_id, node_id, right_id]
            else:
                pass
        parent.update_children(new_children)



    #Given a node_id and a table name or alias name, we convert a simple id (or similar rule below simple id)
    # to a dotted it. Useful when updating predicates during re-bundling processes.
    def replace_simple_id_with_dotted_id(self, node_id, table_or_alias):

        column_name_id = self.find_nodes_by_rule_name("fullColumnName", node_id)[0]
        uid_id = self.find_nodes_by_rule_name("uid", column_name_id)[0]
        simple_id_id = self.find_nodes_by_rule_name("simpleId", uid_id)[0]

        simple_node = self.get_node(simple_id_id)

        while not simple_node.get_is_leaf():
            simple_node = self.get_node(simple_node.get_children()[0])

        old_simple_id_rule = self.get_token_string_from_rule(simple_node)
        
        simple_node.update_rule_name(
            "simpleId " + table_or_alias
        )

        self._add_node_under_parent(
            rule_name = "dottedId ." + old_simple_id_rule,
            is_leaf = True,
            depth = self.get_node(column_name_id).get_depth() + 1,
            parent = column_name_id
        )



    def add_dotted_ids_to_predicates(self, expression_id, table_or_alias, recursive = True):

        predicate_ids = self.find_nodes_by_rule_name("predicate", expression_id)

        for predicate_id in predicate_ids:
            if (
                not self.rule_exists_in_tree("dottedId", predicate_id) 
                and self.rule_exists_in_tree("fullColumnName", predicate_id)
            ):
                self.replace_simple_id_with_dotted_id(
                    predicate_id, table_or_alias
                )

            if recursive:
                for child in self.get_node(predicate_id).get_children():
                    self.add_dotted_ids_to_predicates(child, table_or_alias)



    # -------------------------------------------------------------------------------------------------------
    # Node Retrieval Methods
    # -------------------------------------------------------------------------------------------------------

    def get_node(self, node_id):
        return self.tree_nodes[node_id]



    def find_first_node_with_rule_name(self, rule_to_find, node_id = 0, check_subqueries = False, stop_at_rules = []):
        node_list = self.find_nodes_by_rule_name(
            rule_to_find, node_id, check_subqueries, stop_at_rules
        )
        if len(node_list) > 0:
            return node_list[0]
        else:
            return -1



    def find_nodes_by_rule_name(self, rule_to_find, node_id = 0, check_subqueries = False, stop_at_rules = []):
        node = self.get_node(node_id)
        node_list = []
        if not check_subqueries:
            if "subQueryTable" in node.get_rule_name():
                return node_list
        for rule in stop_at_rules:
            if rule in node.get_rule_name():
                return node_list
        if rule_to_find == node.get_rule_name().strip().split()[0]:
            node_list.append(node_id)
            return node_list
        for child in node.get_children():
            node_list = node_list + self.find_nodes_by_rule_name(rule_to_find, child, stop_at_rules=stop_at_rules)
        return node_list



    def print_nodes_to_console(self):
        for i in range(0, len(self.tree_nodes)):
            print(self.tree_nodes[i].to_string())



    # -------------------------------------------------------------------------------------------------------
    # Condition checking methods
    # -------------------------------------------------------------------------------------------------------

    def rule_exists_in_tree(self, rule_to_find, node_id = 0, check_subqueries = False):
        rule_list = self.find_nodes_by_rule_name(
            rule_to_find,
            node_id,
            check_subqueries
        )
        return len(rule_list) > 0



    # -------------------------------------------------------------------------------------------------------
    # Methods below are for performing SpeakQl Feature transformation including synonym replacement
    # and query element reordering.
    # -------------------------------------------------------------------------------------------------------

    def replace_keywords_for_rule_name(self, rule_name, new_keyword):
        for i in range(0, len(self.tree_nodes)):
            if rule_name in self.tree_nodes[i].get_rule_name():
                self.tree_nodes[i].update_rule_name(
                    rule_name + " " + new_keyword
                )   

    def reorder_select_and_table_expressions(self, node_id):
        node = self.get_node(node_id)
        select_expression = -1
        table_expression = -1
        where_expression = -1
        where_keyword = -1
        select_modifier_expression = -1
        new_children = []
        for child in node.get_children():
            if "selectExpression" in self.get_node(child).get_rule_name():
                select_expression = child
            if "tableExpression" in self.get_node(child).get_rule_name():
                table_expression = child
            if "selectModifierExpression" in self.get_node(child).get_rule_name():
                select_modifier_expression = -1
            if "whereExpression" in self.get_node(child).get_rule_name():
                where_expression = child
            if "whereKeyword" in self.get_node(child).get_rule_name():
                where_keyword = child
        if select_expression > table_expression: #swap the select and table expression positions in parent children list
            for child in node.get_children():
                if child not in [table_expression, select_expression, where_keyword, where_expression]:
                    new_children.append(child)
                if child == table_expression:
                    new_children.append(select_expression)
                if child == select_expression:
                    new_children.append(table_expression)
                    if where_keyword >= 0 and where_expression >= 0:
                        new_children.append(where_keyword)
                        new_children.append(where_expression)
            if select_modifier_expression >= 0:
                new_children.append(table_expression)
            self.get_node(node_id).update_children(new_children)
        elif table_expression > where_expression and (table_expression * where_expression > 0): #The where occurs before tableExpression and so where must be moved to position following table expression
            self.print_verbose("table expression occurs after where expression.")
            for child in node.get_children():
                if child not in [table_expression, where_keyword, where_expression]:
                    new_children.append(child)
                if child == table_expression:
                    new_children.append(table_expression)
                    new_children.append(where_keyword)
                    new_children.append(where_expression)
            self.get_node(node_id).update_children(new_children)
        for child in node.get_children():
            self.reorder_select_and_table_expressions(child)
        


    


    # -------------------------------------------------------------------------------------------------------
    # Methods below are for re-bundling unbundled queries. Order matters, and must proceed as indicated
    # within the rebundle_query method.
    # -------------------------------------------------------------------------------------------------------

    def rebundle_query(self, node_id = 0):
        if self.properties["num_select_and_table_expression"] <= 1 and self.properties["num_multi_query_order_specification"] == 0:
            self.print_verbose("Cannot aggregate statements in a query with only one select and table statement.")
            return
        #The order in which these are called matters: group_by -> select -> where -> join -> tables
        self._infer_group_by(node_id)
        self._bundle_select_elements(node_id)
        self._bundle_where_statements(node_id)
        self._bundle_join_parts(node_id)
        self._bundle_tables(node_id)

        #remove empty statements:
        garbage_nodes = []
        
        for expression in self.table_select_agg_rules:
            garbage_nodes = garbage_nodes + self.find_nodes_by_rule_name(expression)
        if(len(garbage_nodes) > 1):
            garbage_nodes = garbage_nodes[1:]
        garbage_nodes = garbage_nodes + self.find_nodes_by_rule_name("expressionDelimiter")

        garbage_nodes = self.remove_duplicates_from_list(garbage_nodes)
        garbage_nodes.sort()
        self.print_verbose("Garbage nodes:", garbage_nodes)

        for node_id in garbage_nodes:
            self.remove_node_from_tree(node_id)
    


    #Scan the query. If aggregate functions exist, then infer that all non-agg elements should be in group by statement
    def _infer_group_by(self, node_id = 0):
        select_elements = self.get_all_tables_and_elements()
        aggregate_exists = False
        group_by_ids = self.find_nodes_by_rule_name("groupByClause")

        if len(group_by_ids) > 0:
            group_by_id = group_by_ids[0]
        else:
            return

        automatic_ids = self.find_nodes_by_rule_name("automaticGroupByKeyword", group_by_id)
        for auto_id in automatic_ids:
            self.remove_node_from_tree(self.get_node(auto_id).get_parent())

        group_by_node = self.get_node(group_by_id)
        group_by_items = self.find_nodes_by_rule_name("groupByItem", group_by_id)

        existing_items = []
        for item in group_by_items:
            existing_items.append(self.preorder_serialize_tokens(item).strip().replace(" ", ""))
        print("Existing group by items:", existing_items)

        for table in select_elements:
            for element in table[1]:
                if "(" in element and ")" in element:
                    aggregate_exists = True

        if len(existing_items) > 0:
            self._add_node_under_parent(
                "groupByItemDelimiter ,",
                True,
                group_by_node.get_depth() + 1,
                group_by_id
            )
        last_comma = -1
        for table in select_elements:
            for element in table[1]:
                print("Checking if", element, " is in existing items.")
                if not ("(" in element and ")" in element) and element not in existing_items:
                    self._add_node_under_parent(
                        "groupByItem " + element,
                        True,
                        group_by_node.get_depth() + 1,
                        group_by_id
                    )
                    
                    last_comma = self._add_node_under_parent(
                        "groupByItemDelimiter ,",
                        True,
                        group_by_node.get_depth() + 1,
                        group_by_id
                    )
        
        group_by_node.remove_child(last_comma)



    def _bundle_select_elements(self, node_id = 0):
            if self.properties["num_select_and_table_expression"] <= 1 and self.properties["num_multi_query_order_specification"] == 0:
                self.print_verbose("Cannot aggregate select elements in a query with only one select statement.")
                return

            #Rename nothingElement nodes to selectElements
            nothing_element_ids = self.find_nodes_by_rule_name("nothingElement")
            for ne_id in nothing_element_ids:
                ne_node = self.get_node(ne_id)
                ne_node.update_rule_name("selectElements")

            node = self.get_node(node_id)
            elements_by_table = self.get_all_tables_and_elements(node_id = node_id)
            #Find first selectElements rule in query:
            select_elements_node_ids = self.find_nodes_by_rule_name(
                "selectElements", node_id = node_id, stop_at_rules=["whereExpression"]
            )
            first_select_elements_node = self.get_node(select_elements_node_ids[0])
            self.print_verbose(select_elements_node_ids)
            self.print_verbose(first_select_elements_node.get_rule_name())
            #Create a new rule with all elements from the query
            new_children = []
            for table in elements_by_table:
                for element in table[1]:
                    new_id = self._add_node_under_parent(
                        "selectElement " + element,
                        is_leaf = True,
                        depth = first_select_elements_node.get_depth() + 1,
                        parent = first_select_elements_node.get_id()
                    )
                    new_children.append(new_id)
                    #Avoid adding comma after last element:
                    if not (
                        elements_by_table.index(table) == len(elements_by_table) - 1
                        and table[1].index(element) == len(table[1]) - 1
                    ):
                        delim_id = self._add_node_under_parent(
                            "selectElementDelimiter ,",
                            is_leaf = True,
                            depth = first_select_elements_node.get_depth() + 1,
                            parent = first_select_elements_node.get_id()
                        )
                        new_children.append(delim_id)

            #Find the group by clause (if exists) and append any aggregatedWindowedFunctions to the first select element node
            has_group_by = self.rule_exists_in_tree("groupByClause")
            if has_group_by:
                group_by_id = self.find_nodes_by_rule_name("groupByClause")[0]
                function_ids = self.find_nodes_by_rule_name("aggregateWindowedFunction", group_by_id)
                for node_id in function_ids:
                    delim_id = self._add_node_under_parent(
                                "selectElementDelimiter ,",
                                is_leaf = True,
                                depth = first_select_elements_node.get_depth() + 1,
                                parent = first_select_elements_node.get_id()
                            )
                    new_children.append(delim_id)
                    node = self.get_node(node_id)
                    new_children.append(node_id)
                    self.remove_node_from_tree(node_id)
                    node.update_parent(first_select_elements_node.get_id())
                    node.update_depth(first_select_elements_node.get_depth() + 1)
                group_by_select = self.find_nodes_by_rule_name("selectKeyword", group_by_id)
                if len(group_by_select) > 0:
                    select_node = self.get_node(group_by_select[0])
                    self.remove_node_from_tree(select_node.get_id())

            first_select_elements_node.update_children(new_children)       
            #Orphan any following selectElements
            for element in select_elements_node_ids[1:]:
                self.remove_node_from_tree(element, remove_siblings = True)



    def _bundle_where_statements(self, node_id = 0):

        if (self.properties["num_select_and_table_expression"] <= 1 and self.properties["num_multi_query_order_specification"] == 0):
            self.print_verbose("Cannot aggregate where statements in a query with only one table expression.")
            return

        query_order_spec_node_ids = self.find_nodes_by_rule_name("multiQueryOrderSpecification", node_id = node_id)
        first_qos_node = self.get_node(query_order_spec_node_ids[0])
        where_expression_ids = []
        where_expression_table_lookup = {}

        #Find the table name or alias associated with the where clauses:
        for qos_node_id in query_order_spec_node_ids:
            new_expressions = self.find_nodes_by_rule_name("whereExpression", qos_node_id)

            for expression in new_expressions:
                if self.rule_exists_in_tree(rule_to_find = "tableName", node_id = qos_node_id):
                    table_name = self.get_all_table_names(qos_node_id)[0]
                    table_source_item = self.get_tablesourceitem_by_name_from_initial_list(table_name)

                else:
                    alias_name = self.preorder_serialize_tokens(
                        self.find_nodes_by_rule_name("tableAlias", node_id = qos_node_id)[0]
                    ).replace("AS ", "")
                    self.print_verbose("ALIAS NAME:", alias_name)
                    table_source_item = self.get_tablesourceitem_by_alias_from_initial_list(alias_name)

                where_expression_table_lookup[expression] = table_source_item.get_alias_if_exists_else_name()

            where_expression_ids = where_expression_ids + new_expressions
            self.print_verbose(where_expression_ids)
            self.print_verbose("Where expression table dict:", where_expression_table_lookup)
        
        if len(where_expression_ids) == 0:
            self.print_verbose("No where expressions exist in this query.")
            return

        if not self.rule_exists_in_tree("whereKeyword", first_qos_node.get_id()):
            self._add_node_under_parent(
                "whereKeyword WHERE", 
                True, 
                first_qos_node.get_depth() + 1, 
                first_qos_node.get_id()
            )

        for expression_id in where_expression_ids:
            #Check if predicates in expression have dotted ids and add them if not
            self.add_dotted_ids_to_predicates(expression_id, where_expression_table_lookup[expression_id])

            where_expression_node = self.get_node(expression_id)
            if expression_id in first_qos_node.get_children():
                self.surround_node_with_parens(expression_id)
            else:
                if not where_expression_ids.index(expression_id) == 0:
                    self._add_node_under_parent(
                        "logicalOperator AND",
                        True,
                        first_qos_node.get_depth() + 1,
                        first_qos_node.get_id()
                    )        
                old_parent = self.get_node(where_expression_node.get_parent())
                old_parent.remove_child(expression_id)
                first_qos_node.add_child(expression_id)
                where_expression_node.update_parent(first_qos_node.get_id())
                self.surround_node_with_parens(expression_id)



    def _bundle_join_parts(self, node_id = 0):
        
        if(self.properties["num_joinpart"] == 0 and self.properties["num_multijoinpart"] == 0):
            self.print_verbose("Cannot consolidate join parts in a query without join parts")
            return
        
        #Retrieve the first MultiQueryOrderSpecification that contains a TableExpressionNoJoin rule
        multi_query_order_specification_ids = self.find_nodes_by_rule_name("multiQueryOrderSpecification")

        #first_table_expression_node is where we will align all of the consolidated join parts
        for node_id in multi_query_order_specification_ids:
            if self.rule_exists_in_tree("tableExpressionNoJoin"):
                first_table_expression_node = self.get_node(
                    self.find_nodes_by_rule_name("tableExpressionNoJoin", node_id)[0]
                )

        #Retrieve all MultiJoinExpressions
        multi_join_expression_ids = self.find_nodes_by_rule_name("multiJoinExpression")

        #Create a list of JoinParts
        join_part_items = []
        for node_id in multi_join_expression_ids:
            multi_join_part_ids = self.find_nodes_by_rule_name("multiJoinPart", node_id = node_id)
            for join_part_id in multi_join_part_ids:
                
                join_type = "inner"
                if self.rule_exists_in_tree("multiOuterJoin", join_part_id):
                    join_type = "outer"

                join_direction = ""
                if self.rule_exists_in_tree("joinDirection"):
                    join_direction = self.preorder_serialize_tokens(
                        self.find_nodes_by_rule_name("joinDirection", join_part_id)[0]
                    )

                table_source_item_ids = self.find_nodes_by_rule_name(
                    "tableSourceItem", join_part_id, stop_at_rules=["expression"]
                )

                left_table_name = self.preorder_serialize_tokens(
                    self.find_nodes_by_rule_name("tableName", table_source_item_ids[0])[0]
                )

                right_table_name = self.preorder_serialize_tokens(
                    self.find_nodes_by_rule_name("tableName", table_source_item_ids[1])[0]
                )

                left_table_alias = ""
                if self.rule_exists_in_tree("tableAlias", table_source_item_ids[0]):
                    left_table_alias = self.preorder_serialize_tokens(
                        self.find_nodes_by_rule_name("tableAlias", table_source_item_ids[0])[0]
                    )

                right_table_alias = ""
                if self.rule_exists_in_tree("tableAlias", table_source_item_ids[1]):
                    left_table_alias = self.preorder_serialize_tokens(
                        self.find_nodes_by_rule_name("tableAlias", table_source_item_ids[1])[0]
                    )

                while len(self.find_nodes_by_rule_name("withKeyword", join_part_id)) > 0:
                    self.remove_node_from_tree(
                        self.find_nodes_by_rule_name("withKeyword", join_part_id)[0]
                    )

                join_part_items.append(
                    MultiJoinPartItem(
                        join_part_id, 
                        left_table_name=left_table_name,
                        right_table_name=right_table_name,
                        join_type=join_type,
                        join_direction=join_direction,
                        left_table_alias=left_table_alias,
                        right_table_alias=right_table_alias
                    )
                )

        #Order the join_parts together
        # - First join part must reference the base table
        # - succeeding join parts must also reference the base table or a table in a previous join
        tables_in_query = []
        tables_in_query.append(self.initial_table_source_items[0].get_name())
        aliases_in_query = []
        aliases_in_query.append(self.initial_table_source_items[0].get_alias())
        ordered_join_part_items = []
        already_ordered = []
        time_out = 0
        while len(ordered_join_part_items) < len(join_part_items) and time_out < 20:
            time_out = time_out + 1
            self.print_verbose(str(len(ordered_join_part_items)), str(len(join_part_items)))
            for join_part in join_part_items:
                self.print_verbose("JOIN PARTS IN QUERY:", join_part.get_left_table_name(), join_part.get_right_table_name())
                if (((join_part.get_left_table_name().strip() in tables_in_query) 
                        or (join_part.left_table_has_alias() 
                            and join_part.get_left_table_alias().strip() in aliases_in_query
                        ))
                    and join_part.get_join_part_node_id() not in already_ordered 
                ):
                    ordered_join_part_items.append(join_part)
                    already_ordered.append(join_part.get_join_part_node_id())
                    self.remove_node_from_tree(
                        self.find_nodes_by_rule_name("tableSourceItem", join_part.get_join_part_node_id())[0]
                    )
                    tables_in_query.append(join_part.get_right_table_name().strip())
                    if join_part.right_table_has_alias():
                        aliases_in_query.append(join_part.get_right_table_alias().strip())
                    self.print_verbose("Added", join_part.get_right_table_name().strip(), "to ordered query list")
                elif (((join_part.get_right_table_name().strip() in tables_in_query) 
                        or (join_part.right_table_has_alias() 
                            and join_part.get_right_table_alias().strip() in aliases_in_query
                        ))
                    and join_part.get_join_part_node_id() not in already_ordered 
                ):
                    ordered_join_part_items.append(join_part)
                    already_ordered.append(join_part.get_join_part_node_id())
                    self.remove_node_from_tree(
                        self.find_nodes_by_rule_name("tableSourceItem", join_part.get_join_part_node_id())[1]
                    )
                    tables_in_query.append(join_part.get_left_table_name().strip())
                    if join_part.left_table_has_alias():
                        aliases_in_query.append(join_part.get_left_table_alias().strip())
                    self.print_verbose("Added", join_part.get_left_table_name().strip(), "to ordered query list")
                self.print_verbose("TABLES IN QUERY:", tables_in_query)
                    

        #Is each table / alias referenced in at least one join part?
        table_source_items = self.get_all_table_source_items()
        for tsi in table_source_items:
            if not ((tsi.has_alias() and tsi.get_alias() in aliases_in_query) 
                or (tsi.get_name() in tables_in_query)
            ):
                self.print_verbose("WARNING: Table", tsi.get_name(), 
                    "referenced in multi query without corresponding join"
                )
        
        #Move all join expressions to the base query
        self.print_verbose("Moving all joins underneath node", first_table_expression_node.get_rule_name())
        join_nodes = self.find_nodes_by_rule_name("multiJoinExpression")
        table_expression_node = self.get_node(self.find_nodes_by_rule_name("tableExpressionNoJoin")[0])
        for node_id in join_nodes:
            table_expression_node.add_child(node_id)
            table_expression_node.update_rule_name("tableExpression")
            parent = self.get_node(self.get_node(node_id).get_parent())
            parent.remove_child(node_id)



    def _bundle_tables(self, node_id = 0):
        #TODO: add logic to only aggregate a table ID once so you can create multiple expressions sourcing the same table
        #multiple different types of conditions can exist:
        if (self.properties["num_select_and_table_expression"] <= 1 and 
                self.properties["num_multi_query_order_specification"] == 0):
            self.print_verbose("Cannot aggregate tables in a query with only one table expression.")
            return           
        # - no joins, tables > 1, select and table expressions == tables
        #     consolidate table calls into first table expression (similar to select element agg)
        #     consolidate where statements into first where expression (probably needs a separate method)
        if (self.properties["num_non_right_table_name"] > 1 and self.properties["num_joinpart"] == 0):
            table_sources_node_ids = self.find_nodes_by_rule_name("tableSources", node_id = node_id, stop_at_rules=['whereExpression'])
            table_sources_node_ids = table_sources_node_ids + self.find_nodes_by_rule_name("tableExpressionNoJoin", node_id = node_id)
            self.print_verbose(table_sources_node_ids)
            first_table_sources_node = self.get_node(table_sources_node_ids[0])
            all_table_source_node_ids = self.find_nodes_by_rule_name("tableSource", node_id = node_id)
            all_table_source_node_ids = all_table_source_node_ids + self.find_nodes_by_rule_name("tableSourceNoJoin", node_id = node_id)
            self.print_verbose("Table source node IDs:", all_table_source_node_ids)
            new_table_sources_children = []
            if self.rule_exists_in_tree("tableSourceNoJoin", table_sources_node_ids[0]):
                #If this is an unbundled query, add the fromKeyword because it sits in a different spot in the tree
                from_keyword_id = self._add_node_under_parent(
                    "fromKeyword FROM", True, first_table_sources_node.get_depth() + 1, first_table_sources_node.get_id()
                )
                new_table_sources_children.append(from_keyword_id)
            for node_id in all_table_source_node_ids:
                table_source_node = self.get_node(node_id)
                table_source_node.update_parent(first_table_sources_node.get_id())
                new_table_sources_children.append(node_id)
                if not all_table_source_node_ids.index(node_id) == len(all_table_source_node_ids) - 1:
                    new_delimiter_id = self._add_node_under_parent(
                        rule_name = "tableSourceDelimiter ,",
                        is_leaf = True,
                        depth = first_table_sources_node.get_depth() + 1,
                        parent = first_table_sources_node.get_id()
                    )
                    new_table_sources_children.append(new_delimiter_id)
            first_table_sources_node.update_children(new_table_sources_children)
            for node_id in table_sources_node_ids[1:]:
                self.remove_node_from_tree(node_id, remove_siblings = False)


 




