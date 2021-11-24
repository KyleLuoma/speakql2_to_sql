
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

def replace_keyword(old_keyword, new_keyword, text):
    beginning = text.find("(" + old_keyword)
    ending = find_next_closed_paren(beginning, text)
    return text.replace(text[beginning:ending+1], new_keyword)

def replace_synonyms(speakql_tree, SQL_KEYWORDS):    
    for key in SQL_KEYWORDS.keys():
        while key in speakql_tree:
            speakql_tree = replace_keyword(key, SQL_KEYWORDS[key], speakql_tree)
    return speakql_tree

def remove_antlr_words(speakql_tree, antlr_words):
    for word in antlr_words:
        speakql_tree = speakql_tree.replace(word, "")
    return speakql_tree

def remove_antlr_parens(speakql_tree):
    for paren in ["(", ")"]:
        speakql_tree = speakql_tree.replace(paren, "")
    return ' '.join(speakql_tree.split())
