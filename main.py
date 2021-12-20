import SpeakQlParseCaller as spc
import SpeakQlTree as st
from speakql_to_sql import *

verbose = True

parse_engine = spc.JavaSpeakQlParseEngine("gen_disaggregate")
parse_caller = spc.SpeakQlParseCaller(parse_engine)

py_parse_engine = spc.PythonSpeakQlParseEngine("pySpeakQl")
py_parse_caller = spc.SpeakQlParseCaller(py_parse_engine)

user_input = ""
while user_input.upper() != "QUIT":
    print("SpeakQl2>", end = ' ')
    user_input = input()
    if(user_input.upper() == "QUIT"):
        break

    tree = parse_caller.run_select_statement(user_input)
    print("Serial translator:", translate_speakql_to_sql(tree, verbose = False))
    print("Tree translator:", translate_speakql_to_sql_with_st(tree, verbose = True))
    
