import SpeakQlParseCaller as spc
import SpeakQlTree as st
from speakql_to_sql import *

verbose = True

parse_engine = spc.JavaSpeakQlParseEngine("gen_subquery_table")
parse_caller = spc.SpeakQlParseCaller(parse_engine)

py_parse_engine = spc.PythonSpeakQlParseEngine("pySpeakQl")
py_parse_caller = spc.SpeakQlParseCaller(py_parse_engine)

tree = ""
user_input = ""
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
    elif(user_input.upper() == "VERBOSE OFF"):
        print("Verbose mode is off. Type verbose on to turn it back on.")
        verbose = False
    elif(user_input.upper() == "PRINT SPEAKQL TREE"):
        speakql_tree.print_tree_to_console()
    elif(user_input.upper() == "PRINT ALL NODES"):
        speakql_tree.print_nodes_to_console()
    else:
        tree = parse_caller.run_select_statement(user_input)
        speakql_tree = st.SpeakQlTree(tree)
        print("Serial translator:", translate_speakql_to_sql(tree, verbose = verbose))
        print("Tree translator:", translate_speakql_to_sql_with_st(speakql_tree, verbose = verbose))

    
    
