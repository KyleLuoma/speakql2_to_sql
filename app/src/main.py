import speakql_translator.SpeakQlParseCaller as spc
import speakql_translator.SpeakQlTree as st
import json
from speakql_translator.speakql_to_sql import *

from speakql_speech_recognition.SpeakQlPredictorCaller import *
from speakql_speech_recognition.SpeakqlKeywords import *

from db_util.db_analyzer import *
from db_util.db_connector import *

from sys import platform
import time
import random




def main():

    parse_engine = spc.JavaSpeakQlParseEngine("gen_simple_reorder_modifiers", simple_speakql= True)
    parse_caller = spc.SpeakQlParseCaller(parse_engine)

    py_parse_engine = spc.PythonSpeakQlParseEngine("pySpeakQl")
    py_parse_caller = spc.SpeakQlParseCaller(py_parse_engine)

    tree = ""
    user_input = ""
    speakql_query = ""

    verbose = False
    connect = False
    predict = False

    speakql_tree = st.SpeakQlTree(tree)
    predictor = SpeakQlPredictorCaller()


    while user_input.upper() != "QUIT":
        print("SpeakQl2>", end = ' ')
        user_input = input()
        if(user_input.upper() == "QUIT"):
            break
        elif(user_input.upper() == "CONNECT"):
            connection = DbConnector(db_engine = "mysql", db_name="speakql_university")
            connect = True
        elif(user_input.upper() == "PREDICT ON"):
            predict = True
        elif(user_input.upper() == "PREDICT OFF"):
            predict = False
        elif(user_input.upper() == "PRINT PARSE TREE"):
            print(speakql_tree.get_parse_tree())
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
            speakql_tree._bundle_select_elements()
        elif(user_input.upper() == "TEST AGGREGATE TABLES"):
            speakql_tree._bundle_tables()
        elif(user_input.upper() == "TEST AGGREGATE WHERE"):
            speakql_tree._bundle_where_statements()
        elif(user_input.upper() == "TEST AGGREGATE ALL"):
            speakql_tree.rebundle_query()
        elif(user_input.upper() == "PRINT JSON"):
            print(speakql_tree.as_json())
        elif(user_input.upper() in ["PRINT SERIAL TREE", "PRINT SQL"]):
            print(
                remove_unwanted_white_space(speakql_tree.preorder_serialize_tokens(0))
            )
        elif(user_input.upper() in ["PRINT SPEAKQL", "PRINT SPEAKQL QUERY"]):
            print(speakql_query)  
        elif(user_input.upper() == "TRANSLATE EXCEL FILE"):
            translate_from_excel("/home/kyle/repos/speakql2_to_sql/artifacts/queries/generated_queries_02_translated.xlsx", parse_caller)
        elif(user_input.upper() == "ADD SPOKEN TO EXCEL"):
            speakql_to_spoken_query("generated_queries_02_translated.xlsx", "generated_translated_spoken_script_queries_02.xlsx")
        else:
            speakql_query = user_input
            tree = parse_caller.run_select_statement(speakql_query)
            speakql_tree = st.SpeakQlTree(tree, verbose)
            #print("Serial translator:", translate_speakql_to_sql(tree, verbose = verbose))
            sql_query = translate_speakql_to_sql_with_st(speakql_tree, verbose = verbose)
            print("Tree translator:", sql_query)
            if connect:
                print(connection.do_single_select_query_into_dataframe(sql_query))
            if predict:
                print("Next valid keywords:", predictor.getNextWordsFromQuery(speakql_query))

        

def speakql_to_spoken_query(input_filename, output_filename):
    spqkw = SpeakQlKeywords()
    if "linux" in platform:
        path = "/home/kyle/repos/speakql2_to_sql/artifacts/queries/"
    else:
        path = "./artifacts/queries/"
    queries = pd.read_excel(path + input_filename)
    spoken_queries = []
    for row in queries.itertuples():
        speakql_query = row.SPEAKQL
        if type(speakql_query) != str:
            continue
        speakql_query = speakql_query.lower()
        tokens = speakql_query.split(" ")
        for i in range(0, len(tokens)):
            token = tokens[i]
            try:
                token = spqkw.symbols_to_word_list_dict[token][
                    random.randrange(0, len(spqkw.symbols_to_word_list_dict[token]))
                    ]
            except KeyError:
                pass
            if len(token.split("-")) == 3:
                date_time = token.replace("'", "").strip().split("-")
                year = date_time[0]
                month = ["january", "february", "march", "april", "may", 
                         "june", "july", "august", "september", "october",
                         "november", "december"][int(date_time[1]) - 1]
                day = date_time[2]
                print(month, day, year)
                token = month + " " + day + " " + year
            if "'" in token:
                token = token.replace("'", " " + spqkw.symbols_to_word_list_dict["'"][
                    random.randrange(0, len(spqkw.symbols_to_word_list_dict["'"]))
                ] + " ")
            if "id" in token:
                token = token.replace("id", " I D ")
            if token == "as" and len(tokens[i + 1]) == 2:
                alias_acronym = ""
                for character in tokens[i + 1]:
                    alias_acronym = alias_acronym + character.upper() + " "
                tokens[i + 1] = alias_acronym.strip()
            tokens[i] = token
        spoken_query = " ".join(tokens)
        spoken_query = spoken_query.replace(" and", ", and")
        spoken_queyr = spoken_query.replace(" comma", ", comma")
        spoken_query = spoken_query.replace(", and then", ". and then")
        for token in tokens:
            if token.upper() in spqkw.get_start_kws():
                spoken_query = spoken_query.replace(" " + token, ". " + token)
        spoken_query = spoken_query.replace("..", ".")
        spoken_query = spoken_query.replace("natural.", "natural")
        spoken_query = spoken_query.replace("quote quote", "quote")
        
        spoken_queries.append(spoken_query)
    queries["SPOKEN_SPEAKQL"] = spoken_queries
    queries.to_excel(path + output_filename)
        

def translate_from_excel(filename, parse_caller):
    if "linux" in platform:
        queries = pd.read_excel("/home/kyle/repos/speakql2_to_sql/artifacts/queries/generated_queries_02.xlsx")
    else:
        queries = pd.read_excel("./generated_queries.xlsx")
    print(queries.head())
    speakql_queries = []
    sql_queries = []
    status = []
    time_to_translate = []
    numrows = queries.shape[0]
    onrow = 0
    query_list = queries[0].to_list()
    num_queries = len(query_list)
    start_all_time = time.time()
    num_translated = 0
    for speakql_query in query_list:
        #speakql_query = row[1][0]
        start_time = time.time()
        try:
            tree = parse_caller.run_select_statement(speakql_query)
            speakql_tree = st.SpeakQlTree(tree, False)
            sql_query = translate_speakql_to_sql_with_st(speakql_tree, False)
            sql_queries.append(sql_query)
            speakql_queries.append(speakql_query)
            if(sql_query.split(" ")[0] == "SELECT"):
                status.append("TRANSLATED")
            else:
                status.append("PARTIAL ERROR")
        except KeyError:
            print("Handling KeyError exception")
            speakql_queries.append(speakql_query)
            sql_queries.append("")
            status.append("KEY ERROR")
            
        except IndexError:
            print("Handling IndexError exception")
            speakql_queries.append(speakql_query)
            sql_queries.append("")
            status.append("INDEX ERROR")

        except ValueError:
            print("Handling ValueError exception")
            speakql_queries.append(speakql_query)
            sql_queries.append("")
            status.append("VALUE ERROR")
            
        num_translated = num_translated + 1
        end_time = time.time()
        elapsed_time = end_time - start_all_time
        translation_time = end_time - start_time
        avg_translation_time = elapsed_time / num_translated
        time_to_translate.append(translation_time)
        remaining_time = avg_translation_time * (num_queries - num_translated)
        if onrow % 100 == 0:
            print("Translated", str(onrow), "of", str(num_queries),"queries.", str((onrow/numrows)*100), "percent complete.")
            print("Elapsed time:", str(int(elapsed_time/60)), "min", str(int(elapsed_time % 60)), "sec")
            print("Remaining time:", str(int(remaining_time/60)), "min", str(int(remaining_time % 60)), "sec")
            print("Average translation time:", str(avg_translation_time))
            print(str(len(speakql_queries)), str(len(sql_queries)), str(len(time_to_translate)), str(len(status)))
        onrow = onrow + 1
        if onrow % 1000 == 0:
            print("Writing intermediate results to DF", (filename.replace(".xlsx", (str(onrow) + ".xlsx"))))
            pd.DataFrame({
                "SPEAKQL" : speakql_queries, 
                "SQL" : sql_queries, 
                "TRANSLATION_SECONDS" : time_to_translate,
                "STATUS" : status
                }).to_excel((filename.replace(".xlsx", (str(onrow) + ".xlsx"))))

    pd.DataFrame({
        "SPEAKQL" : speakql_queries, 
        "SQL" : sql_queries, 
        "TRANSLATION_SECONDS" : time_to_translate,
        "STATUS" : status
        }).to_excel(filename)



if __name__ == "__main__":
    main()