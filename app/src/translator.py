from .speakql_translator.SpeakQlParseCaller import *
from .speakql_translator.SpeakQlTree import *
from .speakql_translator.speakql_to_sql import *

parse_engine = JavaSpeakQlParseEngine("gen_where_expression")
parse_caller = SpeakQlParseCaller(parse_engine)

def run_test_query_translation(test_query):
    tree = parse_caller.run_select_statement(test_query)
    speakql_tree = SpeakQlTree(tree)
    query_results = {}
    query_results["sql_query"] = translate_speakql_to_sql_with_st(speakql_tree, verbose = False)
    query_results["speakql_tree_json"] = speakql_tree.as_json()
    return query_results