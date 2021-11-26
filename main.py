import gen.SpeakQlParseCaller
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

    parser_output = str(gen.SpeakQlParseCaller.run_select_statement())

    tree_start = parser_output.find("stdout=b'") + len("stdout=b'")
    tree_end = parser_output.find("\\r\\n")

    tree = parser_output[tree_start:tree_end]
    reordered_tree = reorder((tree))
    replaced_synonym_tree = replace_synonyms(reordered_tree, SQL_KEYWORDS)
    tagged_function_parens_tree = tag_function_arg_parens(replaced_synonym_tree, paren_tags)
    removed_antlr_words = remove_antlr_words(tagged_function_parens_tree, antlr_words)
    no_antlr_parens = remove_antlr_parens(removed_antlr_words)
    function_parens_added = replace_paren_tags(no_antlr_parens, paren_tags)

    if(verbose):
        print("---- Parser returned ----")
        print(tree)
        print("---- Setting back to SQL Select - From - Where ----")
        print(reordered_tree)
        print ("---- Replacing SpeakQL Synonyms with SQL Keywords ----")
        print(replaced_synonym_tree)
        print ("---- Tagging function parentheses prior to removing all ANTLR parentheses ----")
        print(tagged_function_parens_tree)
        print ("---- Removing ANTLR-specific keywords ----")
        print(removed_antlr_words)
        print ("---- Removing ANTLR parens and extra white space ----")
        print(no_antlr_parens)
        print("---- Replacing PAREN tags with ( and ) ----")
    print(function_parens_added)
