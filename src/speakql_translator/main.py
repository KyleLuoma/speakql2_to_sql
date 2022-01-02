import SpeakQlParseCaller as spc
import SpeakQlTree as st
from speakql_to_sql import *

verbose = True

parse_engine = spc.JavaSpeakQlParseEngine("gen_where_expression")
parse_caller = spc.SpeakQlParseCaller(parse_engine)

py_parse_engine = spc.PythonSpeakQlParseEngine("pySpeakQl")
py_parse_caller = spc.SpeakQlParseCaller(py_parse_engine)

tree = ""
user_input = ""
speakql_query = ""
verbose = False

speakql_tree = st.SpeakQlTree(tree)

while user_input.upper() != "QUIT":
    print("SpeakQl2>", end = ' ')
    user_input = input()
    if(user_input.upper() == "QUIT"):
        break
    elif(user_input.upper() == "PRINT PARSE TREE"):
        print(tree)
    elif(user_input.upper() == "VERBOSE ON"):
        print("Verbose mode is on. Type verbose off to turn it off again")
        verbose = True
        speakql_tree.set_verbose(verbose)
    elif(user_input.upper() == "VERBOSE OFF"):
        print("Verbose mode is off. Type verbose on to turn it back on.")
        verbose = False
        speakql_tree.set_verbose(verbose)
    elif(user_input.upper() == "PRINT SPEAKQL TREE"):
        speakql_tree.print_tree_to_console()
    elif(user_input.upper() == "PRINT ALL NODES"):
        speakql_tree.print_nodes_to_console()
    elif(user_input.upper() == "PRINT ELEMENTS"):
        print(speakql_tree.get_all_tables_and_elements())
    elif(user_input.upper() == "PRINT TABLES"):
        tables = speakql_tree.get_all_table_source_items()
        for table in tables:
            print(table.to_string())
    elif(user_input.upper() in ["PRINT PROPERTIES", "PRINT PROPS"]):
        print(speakql_tree.get_properties())
    elif(user_input.upper() == "TEST AGGREGATE COLUMNS"):
        speakql_tree._aggregate_select_elements()
    elif(user_input.upper() == "TEST AGGREGATE TABLES"):
        speakql_tree._aggregate_tables()
    elif(user_input.upper() == "TEST AGGREGATE WHERE"):
        speakql_tree._aggregate_where_statements()
    elif(user_input.upper() == "TEST AGGREGATE ALL"):
        speakql_tree.aggregate_select_and_table_statements()
    elif(user_input.upper() in ["PRINT SERIAL TREE", "PRINT SQL"]):
        print(
            remove_unwanted_white_space(speakql_tree.preorder_serialize_tokens(0))
        )
    elif(user_input.upper() in ["PRINT SPEAKQL", "PRINT SPEAKQL QUERY"]):
        print(speakql_query)
    else:
        speakql_query = user_input
        tree = parse_caller.run_select_statement(speakql_query)
        speakql_tree = st.SpeakQlTree(tree, verbose)
        #print("Serial translator:", translate_speakql_to_sql(tree, verbose = verbose))
        print("Tree translator:", translate_speakql_to_sql_with_st(speakql_tree, verbose = verbose))

    
    