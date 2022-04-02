from ntpath import join
import random
from numpy import where
import pandas as pd
import SpeakqlKeywords as sk
import JoinPair as jp
import english_words as ew
from sys import platform
import time

if "linux" in platform:
    working_directory = "/home/kyle/repos"
else:
    working_directory = "C:/research_projects"

schema_df = pd.read_excel(working_directory + "/speakql2_to_sql/artifacts/query_gen_schemas/query_gen_schemas.xlsx")

select_query_patterns = [
    "_KW_SELECT_ _SE_ and _SE_ and _SE_ _KW_FROM_ _TE_",
    "_KW_SELECT_ _SE_ _KW_FROM_ _TE_",
    "_KW_FROM_ _TE_ _KW_SELECT_ _SE_ , _SE_ , _SE_",
    "_KW_SELECT_ _SE_ , _SE_ and _SE_ _KW_FROM_ _TE_"
]

join_query_patterns = [
    "join _JTE_1_ with _JTE_2_ on _JTE_1_ . _JSE_1_ = _JTE_2_ . _JSE_2_",
    "natural join _JTE_1_ with _JTE_2_"
]

modifier_query_patterns = [
    "group by _CN_ and _CN_",
    "group by automatic",
    "group by _CN_",
    "having _FUN_ = _NUM_",
    "having _FUN_ > _NUM_",
    "having _FUN_ < _NUM_"
]

query_patterns = select_query_patterns #+ join_query_patterns + modifier_query_patterns

select_element_patterns = [
    "_CN_",
    "_TN_ . _TNCN_",
    "_FUN_",
    ]

function_patterns = [
    "count ( _CN_ )",
    "count ( distinct _CN_ )",
    "count of ( _CN_ )",
    "the count ( _CN_ )",
    "the count of ( _CN_ )"
]

num_function_patterns = [
    "sum ( _CN_INT_ )",
    "avg ( _CN_INT_ )",
    "the sum of ( _CN_INT_ )",
    "the avg of ( _CN_INT_ )",
    "max ( _CN_INT_ )",
    "min ( _CN_INT_ )"
]

table_element_patterns = [
    "_TN_ table",
    "the _TN_ table",
    "the _TN_ table as _ALIAS_",
    "table _TN_",
    "table _TN_ as _ALIAS_",
    "_TN_",
    "_TN_ as _ALIAS_"
]

where_expression_patterns = [
    "where _CN_ _COMP_OP_ _VALUE_",
    "where _CN_ _COMP_OP_ _VALUE_ and _CN_ _COMP_OP_ _VALUE_",
    "where _CN_ _COMP_OP_ _VALUE_ or _CN_ _COMP_OP_ _VALUE_"
]

random.seed()

select_query_patterns = [
    "_KW_SELECT_ _SE_ and _SE_ and _SE_ _KW_FROM_ _TE_",
    "_KW_SELECT_ _SE_ _KW_FROM_ _TE_",
    "_KW_FROM_ _TE_ _KW_SELECT_ _SE_ , _SE_ , _SE_",
    "_KW_SELECT_ _SE_ , _SE_ and _SE_ _KW_FROM_ _TE_"
]

def build_select_query_pattern(table_element_patterns, where_expression_patterns):
    select_string = "_KW_SELECT_ _SE_"
    from_string = "_KW_FROM_ _TE_"
    if random.randint(0, 1) == 1:
        where_string = "_WHERE_EXPR_"
    else:
        where_string = ""
    query = ""

    num_elements = 0
    rand_num = random.randint(0,100)
    if rand_num < 40:
        num_elements = 1
    elif rand_num < 70:
        num_elements = 2
    elif rand_num < 90:
        num_elements = 3
    else:
        num_elements = random.randint(4, 6)

    for i in range(0, random.randint(1, num_elements)):
        delim = ["and", ","][random.randrange(0,2)]
        select_string = select_string + " " + delim + " _SE_ "

    rand_number = random.randint(1,4)

    if rand_number == 1:
        query = select_string.strip() + " " + from_string.strip() + " " + where_string.strip() + " "
    if rand_number == 2:
        query = from_string.strip() + " " + select_string.strip() + " " + where_string.strip() + " "
    if rand_number == 3:
        query = select_string.strip() + " " + where_string.strip() + " " + from_string.strip() + " "
    if rand_number == 4:
        query = from_string.strip() + " " + where_string.strip() + " " + select_string.strip() + " "

    return query


    


def build_select_element(
    select_element_patterns, 
    column_names, 
    table_names, 
    column_names_in_query,
    function_patterns,
    num_function_patterns,
    int_columns,
    schema_df
    ):
    timeout_counter = 10
    element_string = select_element_patterns[(random.randint(0, len(select_element_patterns) - 1))]

    while "_TN_" in element_string and timeout_counter > 0:
        table_name = table_names[random.randrange(0, len(table_names))]
        column_name = column_names[random.randint(0, len(column_names) - 1)]
        if column_name not in column_names_in_query:
            element_string = element_string.replace(
                "_TN_", table_name
                )
            
            element_string = element_string.replace(
                "_TNCN_", column_name
            )
            column_names_in_query.append(column_name)
        else:
            timeout_counter = timeout_counter - 1

    while "_CN_" in element_string and timeout_counter > 0:
        column_name = column_names[random.randint(0, len(column_names) - 1)]
        if column_name not in column_names_in_query:
            element_string = element_string.replace(
                "_CN_", column_name
                )
            column_names_in_query.append(column_name)
        else:
            timeout_counter = timeout_counter - 1

    while "_FUN_" in element_string and timeout_counter > 0:
        do_num_function = random.randint(0, 1) == 1
        if len(int_columns) > 0 and do_num_function:
            fun_string = num_function_patterns[random.randrange(0, len(num_function_patterns))]
            while "_CN_INT_" in fun_string:
                fun_string = fun_string.replace("_CN_INT_", int_columns[random.randrange(0, len(int_columns))])
            element_string = element_string.replace(
                "_FUN_", fun_string
            )

        elif len(int_columns) == 0 or not do_num_function:
            fun_string = function_patterns[random.randrange(0, len(function_patterns))]
            while "_CN_" in fun_string:
                fun_string = fun_string.replace("_CN_", column_names[random.randrange(0, len(column_names))])
            element_string = element_string.replace(
                "_FUN_", fun_string
            )
        else:
            timeout_counter = timeout_counter - 1


    return element_string, column_names_in_query

def build_table_element(table_element_patterns, table_name, table_alias):
    element_string = table_element_patterns[(random.randint(0, len(table_element_patterns) - 1))]
    if "_TN_" in element_string:
        element_string = element_string.replace(
            "_TN_", table_name
            )
    if "_ALIAS_" in element_string:
        element_string = element_string.replace(
            "_ALIAS_", table_alias
        )
    return element_string

def build_where_expression(where_expression_patterns, columns_in_query, int_columns, tables_in_query, alias_dict):
    where_expr_string = where_expression_patterns[random.randrange(0, len(where_expression_patterns))]
    while "_CN_" in where_expr_string and len(columns_in_query) > 0:
        column = columns_in_query[random.randrange(0, len(columns_in_query))]
        where_expr_string = where_expr_string.replace("_CN_", column, 1)
        if column in int_columns:
            value = random.randint(0, 2100)
            operator = ["=", ">", "<", "<>", "<=", ">="][random.randrange(0, 6)]
        elif "date" in column.lower():
            value = (
                "'" + str(random.randrange(1910, 2023)) + "-" + 
                str(random.randint(1, 12)) + "-" + 
                str(random.randint(1, 28)) + "'"
                )
            operator = ["=", ">", "<", "<>", "<=", ">="][random.randrange(0, 6)]
        elif random.randrange(0, 100) < 80:
            value = "'" + ew.english_words_alpha_set.pop() + "'"
            ew.english_words_alpha_set.add(value)
            operator = ["=", "<>"][random.randrange(0, 2)]
        else:
            value = (
                "( " + ["SELECT", "FIND", "DISPLAY"][random.randrange(0, 3)] +
                " " + columns_in_query[random.randrange(0, len(columns_in_query))] +
                " " + ["FROM", "FROM TABLE", "IN TABLE"][random.randrange(0, 3)] +
                " " + tables_in_query[random.randrange(0, len(tables_in_query))] + " ) "
                )
            operator = "IN"
        where_expr_string = where_expr_string.replace("_VALUE_", str(value), 1)
        where_expr_string = where_expr_string.replace("_COMP_OP_", operator, 1)
    return where_expr_string
        

def build_query(
    query_patterns, 
    select_element_patterns, 
    table_element_patterns,
    function_patterns,
    num_function_patterns, 
    where_expression_patterns,
    schema_df,
    force_single_relation = False,
    allow_subquery = True
    ):
    schema_names = schema_df.SCHEMA.unique()
    keywords = sk.SpeakQlKeywords()


    # Random selection of a database schema:
    schema_name = schema_names[(random.randrange(0, len(schema_names)))]
    schema_df = schema_df.where(schema_df.SCHEMA == schema_name).dropna(how = "all")
    tables_in_schema = schema_df.where(schema_df.SCHEMA == schema_name).dropna(how = "all").TABLE_NAME.unique()

    num_relations = random.randint(1, 3)
    if num_relations > len(tables_in_schema):
        num_relations = len(tables_in_schema)

    join_pairs = schema_df.dropna(subset = ["FK_REF_TABLE", "FK_REF_COL"])[["TABLE_NAME", "COLUMN_NAME", "FK_REF_TABLE", "FK_REF_COL"]]
    #join_pairs.reset_index(inplace = True)
    #print(join_pairs)

    tables_in_query = []
    joins_in_query = []
    columns_in_query = []
    alias_dict = {}

    # Create a list of join pairs:
    for i in range(0, num_relations):
        if len(joins_in_query) == 0:
            rand_join = random.randrange(0, join_pairs.shape[0])
            available_pairs = join_pairs

        else:
            available_pairs = join_pairs.where(
                join_pairs["TABLE_NAME"] == joins_in_query[
                    len(joins_in_query) - 1
                    ].get_right_table_name()).dropna(how = "all")
            if len(available_pairs) > 0:
                rand_join = random.randrange(0, available_pairs.shape[0])

        if len(available_pairs) > 0:
            joins_in_query.append(
                jp.JoinPair(
                    available_pairs.iloc[rand_join]["TABLE_NAME"],
                    available_pairs.iloc[rand_join]["FK_REF_TABLE"],
                    available_pairs.iloc[rand_join]["COLUMN_NAME"],
                    available_pairs.iloc[rand_join]["FK_REF_COL"]
                )
            )
            if available_pairs.iloc[rand_join]["TABLE_NAME"] not in tables_in_query:
                tables_in_query.append(available_pairs.iloc[rand_join]["TABLE_NAME"])
            if available_pairs.iloc[rand_join]["FK_REF_TABLE"] not in tables_in_query:
                tables_in_query.append(available_pairs.iloc[rand_join]["FK_REF_TABLE"])

    select_kws = keywords.get_select_kws()
    from_kws = keywords.get_from_kws()

    #Create select project queries for each relation in join pairs
    join_queries = []

    for pair in joins_in_query:
        join_queries.append(pair.to_string())

    sel_proj_queries = []

    #print("Tables in query:", tables_in_query)

    # We don't want every single query to have a join, so we'll randomly reduce tables_in_query down
    # to just one table.
    if random.randrange(0, 100) < 50 or force_single_relation:
        tables_in_query = [tables_in_query[0]]
        join_queries = []

    for table_name in tables_in_query:

        # Random selection of a query pattern:
        #query_string = query_patterns[(random.randrange(0, len(query_patterns)))]
        query_string = build_select_query_pattern(table_element_patterns, where_expression_patterns)
        #print("Randomly generated query template:", query_string)
        
        while "_KW_SELECT_" in query_string:
            query_string = query_string.replace("_KW_SELECT_", select_kws[random.randrange(0, len(select_kws))])

        while "_KW_FROM_" in query_string:
            query_string = query_string.replace("_KW_FROM_", from_kws[random.randrange(0, len(from_kws))])

        while "_TE_" in query_string:
            table_alias = table_name[0] + table_name[len(table_name) - 1]
            alias_dict[table_name] = table_alias
            if random.randrange(0, 100) < 90 or not allow_subquery:
                query_string = query_string.replace(
                    "_TE_",
                    build_table_element(table_element_patterns, table_name, table_alias),
                    1
                )
            else: #Insert a subquery:
                query_string = query_string.replace(
                    "_TE_",
                    "( " + build_query(
                        query_patterns, 
                        select_element_patterns, 
                        table_element_patterns,
                        function_patterns,
                        num_function_patterns, 
                        where_expression_patterns,
                        schema_df,
                        force_single_relation = True,
                        allow_subquery=False
                    ) + " ) as " + table_name
                )

        available_columns = []
        int_columns = []
        int_column_df = schema_df.where(schema_df.IS_NUMBER).dropna(how = "all")
        available_columns = available_columns + schema_df.where(schema_df.TABLE_NAME == table_name).dropna(how = "all").COLUMN_NAME.to_list()
        int_columns = int_columns + int_column_df.where(int_column_df.TABLE_NAME == table_name).dropna(how = "all").COLUMN_NAME.to_list()

        column_names_in_query = []

        while "_SE_" in query_string:
            select_element, column_names_in_query = build_select_element(
                select_element_patterns, 
                available_columns, 
                [table_name], 
                column_names_in_query,
                function_patterns,
                num_function_patterns,
                int_columns,
                schema_df
                )

            query_string = query_string.replace(
                "_SE_", 
                select_element,
                1
                )

        while "_WHERE_EXPR_" in query_string:
            query_string = query_string.replace("_WHERE_EXPR_",  build_where_expression(
                where_expression_patterns,
                available_columns,
                int_columns,
                tables_in_query,
                alias_dict
            ))

        sp_query = query_string.replace("_CN_ _COMP_OP_ _VALUE_", "")
        sel_proj_queries.append(sp_query)
    
    if random.randint(0, 1) == 1 and len(join_queries) > 0:
        query_string = " AND THEN ".join(sel_proj_queries)
        query_string = query_string + " AND THEN " + " AND THEN ".join(join_queries)
    elif len(join_queries) > 0:
        query_string = " AND THEN ".join(join_queries)
        query_string = query_string + " AND THEN " + " AND THEN ".join(sel_proj_queries)
    else:
        query_string = sel_proj_queries[0]

    modifier_added = False
    group_string = ""
    order_string = ""
    limit_string = ""
    having_string = ""

    if " count " in query_string or " sum " in query_string or " avg " in query_string:
        group_string = [
            "GROUP BY AUTOMATIC", 
            "GROUP AUTOMATIC", 
            "GROUP AUTOMATICALLY", 
            "GROUP BY AUTOMATICALLY"
            ][random.randrange(0,4)]
        modifier_added = True

    if len(column_names_in_query) > 0:

        if random.randrange(0, 100) < 10:
            order_string = " ORDER BY " + column_names_in_query[random.randrange(0, len(column_names_in_query))] + [" ASC ", " DESC ", ""][random.randrange(0, 3)]
            modifier_added = True

        if random.randrange(0, 100) < 20:
            limit_string = " LIMIT " + str(random.randrange(1, 50)) 
            modifier_added = True

        if random.randrange(0, 100) < 30:
            having_string = (
                " HAVING " + 
                ["AVG", "SUM", "COUNT", "MAX", "MIN"][random.randrange(0, 5)] + " ( " +
                column_names_in_query[random.randrange(0, len(column_names_in_query))] + 
                " ) " + 
                ["< ", "> ", "= ", "<> "][random.randrange(0, 4)] + 
                str(random.randrange(0, 200))
            )
            modifier_added = True

    modifier_strings = [group_string, order_string, limit_string, having_string]

    if modifier_added:
        if len(tables_in_query) > 1:
            query_string = query_string + " AND THEN "

        while len(modifier_strings)> 0:
            query_string = query_string + " " + modifier_strings.pop(random.randrange(0, len(modifier_strings)))

    while "  " in query_string:
        query_string = query_string.replace("  ", " ")

    return query_string.strip()


def get_query():
    return build_query(
                query_patterns, 
                select_element_patterns, 
                table_element_patterns, 
                function_patterns,
                num_function_patterns,
                where_expression_patterns,
                schema_df
            )


# print(build_query(
#     query_patterns, 
#     select_element_patterns, 
#     table_element_patterns, 
#     function_patterns,
#     num_function_patterns,
#     where_expression_patterns,
#     schema_df
#     ))

queries = []

start_time = time.time()
queries_to_generate = 50000

for i in range (0, queries_to_generate):

    queries.append(build_query(
    query_patterns, 
    select_element_patterns, 
    table_element_patterns, 
    function_patterns,
    num_function_patterns,
    where_expression_patterns,
    schema_df
    ))

    end_time = time.time()
    elapsed_time = end_time - start_time
    avg_time_per_translation = elapsed_time / (i + 1)
    time_remaining = avg_time_per_translation * (queries_to_generate - i)

    if i % 1000 == 0:
        print("Completed", str(i), "queries")
        print("Elapsed time", str(elapsed_time), "seconds")
        print("Time remaining", str(int(time_remaining / 60)), "min", str(time_remaining % 60), "sec")


pd.Series(queries).to_excel("./generated_queries_01.xlsx")


