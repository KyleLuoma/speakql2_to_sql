import random
import pandas as pd
import SpeakqlKeywords as sk

schema_df = pd.read_excel("C:/research_projects/speakql2_to_sql/artifacts/query_gen_schemas/query_gen_schemas.xlsx")

select_query_patterns = [
    "_KW_SELECT_ _SE_ and _SE_ and _SE_ _KW_FROM_ _TE_",
    "_KW_SELECT_ _SE_ _KW_FROM_ _TE_",
    "_KW_SELECT_ _SE_ _KW_FROM_ the _TE_ table",
    "_KW_FROM_ _TE_ _KW_SELECT_ _SE_ , _SE_ , _SE_",
    "_KW_SELECT_ _SE_ , _SE_ and _SE_ _KW_FROM_ _TE_"

]

join_query_patterns = [
    "join _JTE_1_ with _JTE_2_ on _JTE_1_ dot _JSE_1_ equals _JTE_2_ dot _JSE_2_"
]

modifier_query_patterns = [
    "group by _CN_ and _CN_",
    "group by automatic",
    "group by _CN_",
    "having _FUN_ equals _NUM_",
    "having _FUN_ greater than _NUM_"
]

query_patterns = select_query_patterns #+ join_query_patterns + modifier_query_patterns

select_element_patterns = [
    "_CN_",
    "_TN_ dot _TNCN_",
    "_FUN_",
    ]

function_patterns = [
    "count ( _CN_ )",
    "the count of ( _CN_ )"
]

num_function_patterns = [
    "sum ( _CN_INT_ )",
    "average ( _CN_INT_ )",
    "the sum of ( _CN_INT_ )",
    "the average of ( _CN_INT_ )"
]

table_element_patterns = [
    "_TN_"
]

column_names = [
    "capacity",
    "id",
    "salary",
    "firstname",
    "lastname",
    "city",
    "state",
    "ssn"
]

table_names = [
    "customer",
    "building",
    "room",
    "employee",
    "course",
    "courseoffering"
]


random.seed()

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
        if len(int_columns) > 0:
            element_string = element_string.replace(
                "_FUN_", num_function_patterns[random.randrange(0, len(num_function_patterns))]
            )
        elif len(int_columns) == 0:
            element_string = element_string.replace(
                "_FUN_", function_patterns[random.randrange(0, len(function_patterns))]
            )
        else:
            timeout_counter = timeout_counter - 1


    return element_string, column_names_in_query

def build_table_element(table_element_patterns, table_name):
    element_string = table_element_patterns[(random.randint(0, len(table_element_patterns) - 1))]
    if "_TN_" in element_string:
        element_string = element_string.replace(
            "_TN_", table_name
            )
    return element_string

def build_query(
    query_patterns, 
    select_element_patterns, 
    table_element_patterns,
    function_patterns,
    num_function_patterns, 
    schema_df
    ):
    schema_names = schema_df.SCHEMA.unique()
    keywords = sk.SpeakQlKeywords()

    # Random selection of a query pattern:
    query_string = query_patterns[(random.randrange(0, len(query_patterns)))]

    # Random selection of a database schema:
    schema_name = schema_names[(random.randrange(0, len(schema_names)))]
    schema_df = schema_df.where(schema_df.SCHEMA == schema_name).dropna(how = "all")
    tables_in_schema = schema_df.where(schema_df.SCHEMA == schema_name).dropna(how = "all").TABLE_NAME.unique()
    

    select_kws = keywords.get_select_kws()
    from_kws = keywords.get_from_kws()
    
    while "_KW_SELECT_" in query_string:
        query_string = query_string.replace("_KW_SELECT_", select_kws[random.randrange(0, len(select_kws))])

    while "_KW_FROM_" in query_string:
        query_string = query_string.replace("_KW_FROM_", from_kws[random.randrange(0, len(from_kws))])

    tables_in_query = []
    columns_in_query = []
    

    while "_TE_" in query_string:
        table_name = tables_in_schema[random.randrange(0, len(tables_in_schema))]
        if table_name not in tables_in_query:
            query_string = query_string.replace(
                "_TE_",
                build_table_element(table_element_patterns, table_name),
                1
            )
            tables_in_query.append(table_name)

    available_columns = []
    int_columns = []
    int_column_df = schema_df.where(schema_df.IS_NUMBER).dropna(how = "all")
    for table in tables_in_query:
        available_columns = available_columns + schema_df.where(schema_df.TABLE_NAME == table).dropna(how = "all").COLUMN_NAME.to_list()
        int_columns = int_columns + int_column_df.where(int_column_df.TABLE_NAME == table).dropna(how = "all").COLUMN_NAME.to_list()

    column_names_in_query = []

    while "_SE_" in query_string:
        select_element, column_names_in_query = build_select_element(
            select_element_patterns, 
            available_columns, 
            tables_in_query, 
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
    
    return query_string


print(build_query(
    query_patterns, 
    select_element_patterns, 
    table_element_patterns, 
    function_patterns,
    num_function_patterns,
    schema_df
    ))


