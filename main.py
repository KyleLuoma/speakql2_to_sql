import gen.SpeakQlParseCaller
from speakql_to_sql import *

verbose = False

user_input = ""
while user_input.upper() != "QUIT":
    print("SpeakQl2>", end = ' ')
    user_input = input()
    if(user_input.upper() == "QUIT"):
        break
    
    f = open("query.txt", "w")
    f.write(user_input.upper())
    f.close()

    parser_output = str(gen.SpeakQlParseCaller.run_select_statement())

    tree_start = parser_output.find("stdout=b'") + len("stdout=b'")
    tree_end = parser_output.find("\\r\\n")

    tree = parser_output[tree_start:tree_end]
    reordered_tree = reorder((tree))
    replaced_synonym_tree = replace_synonyms(reordered_tree, SQL_KEYWORDS)
    removed_antlr_words = remove_antlr_words(replaced_synonym_tree, antlr_words)
    no_antlr_parens = remove_antlr_parens(removed_antlr_words)

    if(verbose):
        print("---- Parser returned ----")
        print(tree)
        print("---- Setting back to SQL Select - From - Where ----")
        print(reordered_tree)
        print ("---- Replacing SpeakQL Synonyms with SQL Keywords ----")
        print(replaced_synonym_tree)
        print ("---- Removing ANTLR-specific keywords ----")
        print(removed_antlr_words)
        print ("---- Removing ANTLR parens and extra white space ----")
    print(no_antlr_parens)
