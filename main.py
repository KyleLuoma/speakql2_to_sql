import SpeakQlParseCaller as spc
from speakql_to_sql import *

verbose = True

user_input = ""
while user_input.upper() != "QUIT":
    print("SpeakQl2>", end = ' ')
    user_input = input()
    if(user_input.upper() == "QUIT"):
        break
    
    f = open("query.txt", "w")
    f.write(user_input.upper())
    f.close()

    parser_output = str(spc.run_select_statement('gen_parens'))

    tree_start = parser_output.find("stdout=b'") + len("stdout=b'")
    tree_end = parser_output.find("\\r\\n")

    tree = parser_output[tree_start:tree_end]
    print(translate_speakql_to_sql(tree))

    
