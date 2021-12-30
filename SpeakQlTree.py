#lisp_tree = "(selectStatement (querySpecification (tableThenSelectExpression (tableExpression (fromClause (fromKeyword FROM TABLE) (tableSources (tableSource (tableSourceItem (tableName (fullId (uid (simpleId A))))))) (whereKeyword WHERE) (expression (predicate (predicate (expressionAtom (fullColumnName (uid (simpleId A))))) (comparisonOperator =) (predicate (expressionAtom (fullColumnName (uid (simpleId B))))))))) (selectExpression (selectClause (selectKeyword DISPLAY)) (selectElements (selectElement (fullColumnName (uid (simpleId B))))))) selectModifierExpression))"
from os import remove
from TableSourceItem import TableSourceItem
from SpeakQlNode import SpeakQlNode


lisp_tree = "(selectStatement (querySpecification (selectThenTableExpression (selectExpression (selectClause (selectKeyword SELECT)) (selectElements (selectElement (fullColumnName (uid (simpleId A)))) (selectElementDelimiter AND) (selectElement (functionCall (aggregateWindowedFunction SUM (leftParen () (functionArg (fullColumnName (uid (simpleId B)))) (rightParen ))))))) (tableExpression (fromClause (fromKeyword FROM TABLE) (tableSources (tableSource (tableSourceItem (tableName (fullId (uid (simpleId (keywordsCanBeId ONE))))))))))) selectModifierExpression))"

level = 0


class SpeakQlTree:

    def __init__(self, lisp_tree):
        self.next_id = 0
        self.tree_nodes = {}
        self.table_select_agg_rules = [
            "selectThenTableExpression",
            "tableThenSelectExpression"
        ]
        self.parse_tree = lisp_tree
        self._build_tree(self.parse_tree)
        self.properties = self.get_properties_from_parse_tree(self.parse_tree)

    def get_properties_from_parse_tree(self, parse_tree):
        properties = {
            "num_joinpart" : 0,
            "num_non_commutative_join" : 0,
            "num_select_and_table_expression" : 0,
            "num_functioncall" : 0,
            "num_table_name" : 0,
            "num_non_join_table_name": 0,
            "num_table_alias" : 0,
            "num_element_alias" : 0,
            "num_group_by" : 0
        }
        properties["num_joinpart"] = parse_tree.count("joinPart")
        properties["num_non_commutative_joins"] = parse_tree.count("joinDirection")
        properties["num_select_and_table_expression"] = (
            parse_tree.count("selectThenTableExpression") + 
            parse_tree.count("tableThenSelectExpression")
        )
        properties["num_functioncall"] = parse_tree.count("functionCall")
        properties["num_table_name"] = parse_tree.count("tableName")
        properties["num_non_join_table_name"] = parse_tree.count("(tableSource (tableSourceItem (tableName")
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

    def print_nodes_to_console(self):
        for i in range(0, len(self.tree_nodes)):
            print(self.tree_nodes[i].to_string())

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
        for rule in rule_split:
            if not rule[0].islower():
                rule_string = rule_string + rule + " "
        return rule_string

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
        if "selectElement" in node.get_rule_name() and "selectElements" not in node.get_rule_name():
            in_select_element_tree = True
        for child in node.get_children():
            elements = elements + self.get_select_elements(
                child, table_name = table_name, in_select_element_tree = in_select_element_tree
                )
        return elements

    def _aggregate_select_elements(self, node_id = 0):
        if self.properties["num_select_and_table_expression"] <= 1:
            print("Cannot aggregate select elements in a query with only one select statement.")
            return
        node = self.get_node(node_id)
        elements_by_table = self.get_all_tables_and_elements(node_id = node_id)
        #Find first selectElements rule in query:
        select_elements_node_ids = self.find_nodes_by_rule_name("selectElements", node_id = node_id)
        first_select_elements_node = self.get_node(select_elements_node_ids[0])
        print(select_elements_node_ids)
        print(first_select_elements_node.get_rule_name())
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
        first_select_elements_node.update_children(new_children)       
        #Orphan any following selectElements
        for element in select_elements_node_ids[1:]:
            self.remove_node_from_tree(element, remove_siblings = True)

    def _aggregate_where_statements(self, node_id = 0):
        if (self.properties["num_select_and_table_expression"] <= 1):
            print("Cannot aggregate where statements in a query with only one table expression.")
            return

        from_clause_node_ids = self.find_nodes_by_rule_name("fromClause", node_id = node_id)
        first_from_clause_node = self.get_node(from_clause_node_ids[0])

        where_expression_ids = []
        where_expression_table_lookup = {}
        for from_clause_node_id in from_clause_node_ids:
            new_expressions = self.find_nodes_by_rule_name("whereExpression", from_clause_node_id)
            for expression in new_expressions:
                where_expression_table_lookup[expression] = self.get_all_table_names(from_clause_node_id)
            where_expression_ids = where_expression_ids + new_expressions
            print(where_expression_ids)
            print(where_expression_table_lookup)
        
        if len(where_expression_ids) == 0:
            print("No where expressions exist in this query.")
            return

        if not self.rule_exists_in_tree("whereKeyword", first_from_clause_node.get_id()):
            self._add_node_under_parent(
                "whereKeyword WHERE", 
                True, 
                first_from_clause_node.get_depth() + 1, 
                first_from_clause_node.get_id()
            )

        for expression_id in where_expression_ids:
            #Check if predicates in expression have dotted ids and add them if not
            predicate_ids = self.find_nodes_by_rule_name("predicate", expression_id)
            for predicate_id in predicate_ids:
                if (
                    not self.rule_exists_in_tree("dottedId", predicate_id) 
                    and self.rule_exists_in_tree("fullColumnName", predicate_id)
                ):
                    column_name_id = self.find_nodes_by_rule_name("fullColumnName", predicate_id)[0]
                    uid_id = self.find_nodes_by_rule_name("uid", column_name_id)[0]
                    simple_id_id = self.find_nodes_by_rule_name("simpleId", uid_id)[0]
                    old_simple_id_rule = self.get_token_string_from_rule(self.get_node(simple_id_id))
                    self.get_node(simple_id_id).update_rule_name(
                        "simpleId " + where_expression_table_lookup[expression_id][0]
                    )
                    self._add_node_under_parent(
                        rule_name = "dottedId ." + old_simple_id_rule,
                        is_leaf = True,
                        depth = self.get_node(column_name_id).get_depth() + 1,
                        parent = column_name_id
                    )

            where_expression_node = self.get_node(expression_id)
            if expression_id in first_from_clause_node.get_children():
                self.surround_node_with_parens(expression_id)
            else:
                if not where_expression_ids.index(expression_id) == 0:
                    self._add_node_under_parent(
                        "logicalOperator AND",
                        True,
                        first_from_clause_node.get_depth() + 1,
                        first_from_clause_node.get_id()
                    )        
                old_parent = self.get_node(where_expression_node.get_parent())
                old_parent.remove_child(expression_id)
                first_from_clause_node.add_child(expression_id)
                where_expression_node.update_parent(first_from_clause_node.get_id())
                self.surround_node_with_parens(expression_id)
                
        
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

    def _aggregate_tables(self, node_id = 0):
        #multiple different types of conditions can exist:
        if (self.properties["num_select_and_table_expression"] <= 1):
            print("Cannot aggregate tables in a query with only one table expression.")
            return           
        # - no joins, tables > 1, select and table expressions == tables
        #     consolidate table calls into first table expression (similar to select element agg)
        #     consolidate where statements into first where expression (probably needs a separate method)
        if (self.properties["num_non_join_table_name"] > 1 and self.properties["num_joinpart"] == 0):
            table_sources_node_ids = self.find_nodes_by_rule_name("tableSources", node_id = node_id)
            print(table_sources_node_ids)
            first_table_sources_node = self.get_node(table_sources_node_ids[0])
            all_table_source_node_ids = self.find_nodes_by_rule_name("tableSource", node_id = node_id)
            print(all_table_source_node_ids)
            new_table_sources_children = []
            for i in range(0, len(all_table_source_node_ids)):
                node_id = all_table_source_node_ids[i]
                table_source_node = self.get_node(node_id)
                table_source_node.update_parent(first_table_sources_node.get_id())
                new_table_sources_children.append(node_id)
                if i + 1 < len(all_table_source_node_ids):
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


        # - joins exist, select and table expressions > 1
        #     call to join aggregation method

    def remove_node_from_tree(self, node_id, remove_siblings = False):
        child = self.get_node(node_id)
        parent = self.get_node(child.get_parent())
        children = parent.get_children()
        print(children)
        if len(children) > 1 and not remove_siblings:
            children.remove(node_id)
            parent.update_children(children)
            print(children)
        else:
            parent.update_children([])
        child.update_parent(-1)

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

    def get_all_table_source_items(self, node_id = 0, at_start_node = True):
        table_source_items = []
        node = self.get_node(node_id)
        if "selectExpression" in node.get_rule_name():
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
            table_source_items = table_source_items + self.get_all_table_source_items(child, at_start_node = False)
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

    def remove_duplicates_from_list(self, target_list):
        return list(dict.fromkeys(target_list))

    def get_all_tables_and_elements(self, node_id = 0):
        node = self.get_node(node_id)
        table_alias_dict = {}
        alias_table_dict = {}
        table_elements = []
        table_dict_list = []
        all_table_source_items = self.get_all_table_source_items()
        for table in all_table_source_items:
            table_alias_dict[table.get_name()] = table.get_alias()
            alias_table_dict[table.get_alias()] = table.get_name()
        for rule in self.table_select_agg_rules:
            if rule in node.get_rule_name():
                local_table_source_items = self.get_all_table_source_items(node_id)
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
                if self.properties["num_select_and_table_expression"] > 1:
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

    def find_node_by_rule_name(self, rule_to_find, node_id = 0, check_subqueries = False):
        node = self.get_node(node_id)
        if not check_subqueries:
            if "subQueryTable" in node.get_rule_name():
                return -1
        elif rule_to_find in node.get_rule_name():
            return node_id
        elif not node.get_is_leaf():
            for child in node.get_children():
                return self.find_node_by_rule_name(rule_to_find, child)
        else:
            return -1

    def find_nodes_by_rule_name(self, rule_to_find, node_id = 0, check_subqueries = False):
        node = self.get_node(node_id)
        node_list = []
        if not check_subqueries:
            if "subQueryTable" in node.get_rule_name():
                return node_list
        if rule_to_find == node.get_rule_name().strip().split()[0]:
            node_list.append(node_id)
            return node_list
        for child in node.get_children():
            node_list = node_list + self.find_nodes_by_rule_name(rule_to_find, child)
        return node_list

    def rule_exists_in_tree(self, rule_to_find, node_id = 0, check_subqueries = False):
        rule_list = self.find_nodes_by_rule_name(
            rule_to_find,
            node_id,
            check_subqueries
        )
        return len(rule_list) > 0

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

    def aggregate_select_and_table_statements(self, node_id = 0):
        if self.properties["num_select_and_table_expression"] <= 1:
            print("Cannot aggregate statements in a query with only one select and table statement.")
            return
        #The order in which these are called matters: select -> where -> tables
        self._aggregate_select_elements(node_id)
        self._aggregate_where_statements(node_id)
        self._aggregate_tables(node_id)

        #remove empty statements:
        garbage_nodes = []
        for expression in self.table_select_agg_rules:
            garbage_nodes = garbage_nodes + self.find_nodes_by_rule_name(expression)
            garbage_nodes = garbage_nodes + self.find_nodes_by_rule_name("expressionDelimiter")
        garbage_nodes = self.remove_duplicates_from_list(garbage_nodes)
        garbage_nodes.sort()
        print("Garbage nodes:", garbage_nodes)
        if(len(garbage_nodes) > 1):
            garbage_nodes = garbage_nodes[1:]
            for node_id in garbage_nodes:
                self.remove_node_from_tree(node_id)



class JoinPart:

    def __init__(self):
        self.from_table = ""
        self.to_table = ""
        self.from_on_attr = ""
        self.to_on_attr = ""
        self.pred = ""

    def set_from_table(self, table_name):
        self.from_table = table_name
 



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
