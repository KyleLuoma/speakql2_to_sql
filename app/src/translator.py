from .speakql_translator.SpeakQlParseCaller import *
from .speakql_translator.SpeakQlTree import *
from .speakql_translator.speakql_to_sql import *
import pandas as pd

parse_engine = JavaSpeakQlParseEngine("gen_simple_reorder_modifiers", simple_speakql=True)
parse_caller = SpeakQlParseCaller(parse_engine)

def run_test_query_translation(test_query):
    tree = parse_caller.run_select_statement(test_query)
    speakql_tree = SpeakQlTree(tree)
    query_results = {}
    query_results["sql_query"] = translate_speakql_to_sql_with_st(speakql_tree, verbose = False)
    query_results["speakql_tree_json"] = speakql_tree.as_json()
    return query_results

def full_query_translation(query):
    steps = full_query_translation_with_intermediate_steps(query)
    return steps['sql_query']

def full_query_translation_with_intermediate_steps(query):
    tree = parse_caller.run_select_statement(query)
    speakql_tree = SpeakQlTree(tree, verbose = True)
    query_results = {}
    query_results["speakql_tree"] = speakql_tree.as_json()
    query_results["speakql_query"] = remove_unwanted_white_space(speakql_tree.preorder_serialize_tokens(0))
    for key in SQL_KEYWORDS_FOR_ST:
        speakql_tree.replace_keywords_for_rule_name(key, SQL_KEYWORDS_FOR_ST[key])
    speakql_tree.remove_syntactic_sugar()
    query_results["replaced_keyword_tree"] = speakql_tree.as_json()
    query_results["replaced_keyword_query"] = remove_unwanted_white_space(speakql_tree.preorder_serialize_tokens(0))
    speakql_tree.reorder_select_and_table_expressions(0)
    speakql_tree.reorder_select_modifiers()
    query_results["reordered_tree"] = speakql_tree.as_json()
    query_results["reordered_query"] = remove_unwanted_white_space(speakql_tree.preorder_serialize_tokens(0))
    speakql_tree.rebundle_query()
    query_results["sql_query_tree"] = speakql_tree.as_json()
    query_results["sql_query"] = remove_unwanted_white_space(speakql_tree.preorder_serialize_tokens(0))
    query_results["table_list"] = speakql_tree.get_initial_tables_and_elements_as_json()
    return query_results

def translate_speakql_to_sql_query(speakql_tree, verbose = False):
    for key in SQL_KEYWORDS_FOR_ST:
        speakql_tree.replace_keywords_for_rule_name(key, SQL_KEYWORDS_FOR_ST[key])
    speakql_tree.remove_syntactic_sugar()
    speakql_tree.reorder_select_and_table_expressions(0)
    speakql_tree.aggregate_select_and_table_statements()
    if(verbose):
        print("---- Tables and table attributes in query ----")
        print(speakql_tree.get_all_tables_and_elements())
    return remove_unwanted_white_space(speakql_tree.preorder_serialize_tokens(0))

def remove_unwanted_white_space(speakql_tree):
    while(" ." in speakql_tree 
          or ". " in speakql_tree 
          or " ," in speakql_tree
          or " ( " in speakql_tree
          or " )" in speakql_tree
          or "< =" in speakql_tree
          or "> =" in speakql_tree
          ):
        speakql_tree = speakql_tree.replace(" .", ".")
        speakql_tree = speakql_tree.replace(". ", ".")
        speakql_tree = speakql_tree.replace(" ,", ",")
        speakql_tree = speakql_tree.replace(" ( ", "(")
        speakql_tree = speakql_tree.replace(" )", ")")
        speakql_tree = speakql_tree.replace("< =", "<=")
        speakql_tree = speakql_tree.replace("> =", ">=")
    return speakql_tree


