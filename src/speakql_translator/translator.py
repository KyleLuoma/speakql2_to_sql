from SpeakQlParseCaller import *
from SpeakQlTree import *
from speakql_to_sql import *

parse_engine = JavaSpeakQlParseEngine("gen_where_expression")
parse_caller = SpeakQlParseCaller(parse_engine)

def run_test_query_translation(test_query):
    tree = parse_caller.run_select_statement(test_query)
    speakql_tree = SpeakQlTree(tree)
    return translate_speakql_to_sql_with_st(speakql_tree, verbose = False)