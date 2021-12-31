
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 17:00:11 2021

@author: KYLEL
"""

from .SpeakQlTree import SpeakQlTree as st

open_paren = 0
close_paren = 0
sql_out = ""

SQL_KEYWORDS = {
    "selectKeyword" : "SELECT", 
    "fromKeyword" : "FROM",
    "selectElementDelimiter" : ",",
    "tableSourceDelimiter" : ",",
    "selectElementDot" : ".",
    "joinKeyword" : "JOIN"
    }

SQL_KEYWORDS_FOR_ST = SQL_KEYWORDS.copy()
SQL_KEYWORDS_FOR_ST["leftParen"] = "("
SQL_KEYWORDS_FOR_ST["rightParen"] = ")"

antlr_words = [
    "distinctAggregatorKeyword",
    "selectElementAs",
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
    "stringLiteral",
    "functionArgs",
    "functionArg",
    "selectStatement",
    "queryExpression",
    "querySpecification",
    "keywordsCanBeId",
    "mathOperator"
]

#Function complexity: 3 * 2n = 6n
def reorder(speakql_tree):
    #get_expression call complexity: 2n * 3
    table_expression = get_expression("tableExpression", speakql_tree)
    select_expression = get_expression("selectExpression", speakql_tree)
    select_modifier_expression = get_expression("selectModifierExpression", speakql_tree)
    
    return select_expression + table_expression + select_modifier_expression 

#Function complexity: 2n
def get_expression(expression_token, speakql_tree):
    expression = "(" + expression_token
    #Find complexity: n
    expression_start = speakql_tree.find(expression)               
    paren_count = 1
    i = expression_start + 1
    
    if "(" not in speakql_tree[expression_start:]:
        return ""
    
    #While loop complexity: n
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

#function complexity ~ 40n
def replace_synonyms(speakql_tree, SQL_KEYWORDS): 
    #for loop complexity: number of keywords with synonyms in speakQL grammar (currently 4) * n   
    for key in SQL_KEYWORDS.keys():
        #while loop complexity: n * number of times a keyword is in the tree (min of 2, likely max of 10) so 10n
        while key in speakql_tree:
            speakql_tree = replace_keyword(key, SQL_KEYWORDS[key], speakql_tree)
    return speakql_tree

paren_tags = {"leftParen" : "(", "rightParen" : ")"}

#function complexity: 2n
def replace_paren_tags(speakql_tree, paren_tags):
    speakql_tree = speakql_tree.replace(" leftParen ", paren_tags["leftParen"])
    speakql_tree = speakql_tree.replace(" rightParen", paren_tags["rightParen"])
    return speakql_tree

#print(get_expression("functionArg", "(test(functionArg (fullColumnName (uid (simpleId LINE_ITEM)) (dottedId .PRICE))))").replace("functionArg", " L_PAREN "))

#print(tag_function_arg_parens("test functionArg (((A)))", paren_tags))

#Function complexity: num antlr_words * n so ~40n
def remove_antlr_words(speakql_tree, antlr_words):
    for word in antlr_words:
        speakql_tree = speakql_tree.replace(word, "")
    return speakql_tree

#function complexity: 2n
def remove_antlr_parens(speakql_tree):
    for paren in ["(", ")"]:
        speakql_tree = speakql_tree.replace(paren, "")
    return ' '.join(speakql_tree.split())

#function complexity: 2n
def remove_unwanted_white_space(speakql_tree):
    while(" ." in speakql_tree 
          or ". " in speakql_tree 
          or " ," in speakql_tree
          or " ( " in speakql_tree
          or " )" in speakql_tree
          ):
        speakql_tree = speakql_tree.replace(" .", ".")
        speakql_tree = speakql_tree.replace(". ", ".")
        speakql_tree = speakql_tree.replace(" ,", ",")
        speakql_tree = speakql_tree.replace(" ( ", "(")
        speakql_tree = speakql_tree.replace(" )", ")")
    return speakql_tree

def translate_speakql_to_sql_with_st(speakql_tree, verbose = False):
    for key in SQL_KEYWORDS_FOR_ST:
        speakql_tree.replace_keywords_for_rule_name(key, SQL_KEYWORDS_FOR_ST[key])
    speakql_tree.reorder_select_and_table_expressions(0)
    speakql_tree.aggregate_select_and_table_statements()
    if(verbose):
        print("---- Tables and table attributes in query ----")
        print(speakql_tree.get_all_tables_and_elements())
    return remove_unwanted_white_space(speakql_tree.preorder_serialize_tokens(0))

#Function complexity: O(92n)
def translate_speakql_to_sql(speakql_tree, verbose = False):
    #reorder function call complexity: 6n
    reordered_tree = reorder((speakql_tree))
    #replace synonym call complexity: ~40n
    replaced_synonym_tree = replace_synonyms(reordered_tree, SQL_KEYWORDS)
    #remove antlr words call complexity: ~40n
    removed_antlr_words = remove_antlr_words(replaced_synonym_tree, antlr_words)
    #remove antlr parens call complexity: 2n
    no_antlr_parens = remove_antlr_parens(removed_antlr_words)
    #replace paren tag call complexity: 2n
    sql_parens = replace_paren_tags(no_antlr_parens, paren_tags)
    #remove unwanted white space call complexity: 2n
    final_tree = remove_unwanted_white_space(sql_parens)

    if(verbose):
        print("---- Starting with SpeakQl tree ----")
        print(speakql_tree)
        print("---- Setting back to SQL Select - From - Where ----")
        print(reordered_tree)
        print ("---- Replacing SpeakQL Synonyms with SQL Keywords ----")
        print(replaced_synonym_tree)
        print ("---- Removing ANTLR-specific keywords ----")
        print(removed_antlr_words)
        print ("---- Removing ANTLR parens and extra white space ----")
        print(no_antlr_parens)
        print("---- Replacing PAREN tags with ( and ) ----")
        print(sql_parens)
        print("---- Removing unwanted white space ----")
        print(final_tree)

    return final_tree
