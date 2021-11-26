
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 17:00:11 2021

@author: KYLEL
"""

open_paren = 0
close_paren = 0
sql_out = ""

SQL_KEYWORDS = {
    "selectKeyword" : "SELECT", 
    "fromKeyword" : "FROM",
    "selectElementDelimiter" : ",",
    "joinKeyword" : "JOIN"
    }

antlr_words = [
    "selectExpression",
    "selectClause",
    "selectElements",
    "selectElement",
    "fullColumnName",
    "uid",
    "simpleId",
    "tableExpression",
    "fromClause",
    "tableSources",
    "tableSource",
    "tableSourceItem",
    "tableName",
    "fullId",
    "Item",
    "expression",
    "predicate",
    "expressionAtom",
    "comparisonOperator",
    "Atom",
    "constant",
    "decimalLiteral",
    "joinPart",
    "dottedId",
    "selectModifierExpression",
    "groupByClause",
    "groupBy",
    "aggregateWindowedFunction",
    "functionCall",
    "stringLiteral"
]

def reorder(speakql_tree):
    table_expression = get_expression("tableExpression", speakql_tree)
    select_expression = get_expression("selectExpression", speakql_tree)
    select_modifier_expression = get_expression("selectModifierExpression", speakql_tree)
    
    return select_expression + table_expression + select_modifier_expression 

def get_expression(expression_token, speakql_tree):
    expression = "(" + expression_token
    expression_start = speakql_tree.find(expression)
    paren_count = 1
    i = expression_start + 1
    
    if "(" not in speakql_tree[expression_start:]:
        return ""
    
    while paren_count > 0:
        if i < len(speakql_tree) and speakql_tree[i] == "(":
            paren_count = paren_count + 1
        elif i < len(speakql_tree) and speakql_tree[i] == ")":
            paren_count = paren_count - 1
        i = i + 1
    expression_end = i
    
    return speakql_tree[expression_start:expression_end]

def find_next_closed_paren(start_at, text):
    for i in range(start_at, len(text)):
        if text[start_at] == ")":
            return start_at
        else:
            start_at = start_at + 1
    return 0

def find_inner_open_paren(start_at, text):
    last_seen_open_paren = 0
    i = start_at
    while i < len(text) and text[i] != ")":
        #print("looking for open paren at", str(i), text[i])
        if text[i] == "(":
            last_seen_open_paren = i
        i = i + 1
    return last_seen_open_paren

def replace_keyword(old_keyword, new_keyword, text):
    beginning = text.find("(" + old_keyword)
    ending = find_next_closed_paren(beginning, text)
    return text.replace(text[beginning:ending+1], new_keyword)

def replace_synonyms(speakql_tree, SQL_KEYWORDS):    
    for key in SQL_KEYWORDS.keys():
        while key in speakql_tree:
            speakql_tree = replace_keyword(key, SQL_KEYWORDS[key], speakql_tree)
    return speakql_tree

paren_tags = {"L_PAREN" : "(", "R_PAREN" : ")"}

def tag_function_arg_parens(speakql_tree, paren_tags):
    while "functionArg" in speakql_tree:
        l_paren_location = find_inner_open_paren(speakql_tree.find("functionArg"), speakql_tree)
        r_paren_location = find_next_closed_paren(l_paren_location, speakql_tree)
        speakql_tree = speakql_tree[0 : l_paren_location].replace("functionArg", "") + speakql_tree[l_paren_location : len(speakql_tree)]
        l_paren_location = l_paren_location - (len("functionArg") - 1)
        r_paren_location = r_paren_location - len("functionArg")
        speakql_tree = speakql_tree[0 : l_paren_location] + " L_PAREN " + speakql_tree[l_paren_location : r_paren_location] + " R_PAREN " + speakql_tree[r_paren_location : len(speakql_tree)]
    return speakql_tree

def replace_paren_tags(speakql_tree, paren_tags):
    speakql_tree = speakql_tree.replace("L_PAREN", paren_tags["L_PAREN"])
    speakql_tree = speakql_tree.replace("R_PAREN", paren_tags["R_PAREN"])
    return speakql_tree

#print(tag_function_arg_parens("test functionArg (((A)))", paren_tags))

def remove_antlr_words(speakql_tree, antlr_words):
    for word in antlr_words:
        speakql_tree = speakql_tree.replace(word, "")
    return speakql_tree

def remove_antlr_parens(speakql_tree):
    for paren in ["(", ")"]:
        speakql_tree = speakql_tree.replace(paren, "")
    return ' '.join(speakql_tree.split())
