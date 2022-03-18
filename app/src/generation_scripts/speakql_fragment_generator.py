import random

query_patterns = [
    "select _SE_ and _SE_ and _SE_ from table _TE_",
    "what is the _SE_ in _TE_",
    "join _TE_ with _TE_ on _TE_ dot _SE_ equals _TE_ dot _SE_",
    "group by _CN_ and _CN_",
    "group by automatic",
    "group by _CN_",
    "having _FUN_ equals _NUM_",
    "having _FUN_ greater than _NUM_"
]

select_element_patterns = [
    "_CN_",
    ]

function_patterns = [
    "sum ( _CN_ )",
    "count ( _CN_ )",
    "average ( _CN_ )",
    "the sum of ( _CN_ )",
    "the count of ( _CN_ )",
    "the average of ( _CN_ )"
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

def build_select_element(select_element_patterns, column_names, table_names):
    element_string = select_element_patterns[(random.randint(0, len(select_element_patterns) - 1))]
    if "_CN_" in element_string:
        element_string = element_string.replace(
            "_CN_", column_names[random.randint(0, len(column_names) - 1)]
            )
    if "_TN_" in element_string:
        element_string = element_string.replace(
            "_TN_", table_names[random.randint(0, len(table_names) - 1)]
            )
    return element_string

def build_table_element(table_element_patterns, table_names):
    element_string = table_element_patterns[(random.randint(0, len(table_element_patterns) - 1))]
    if "_TN_" in element_string:
        element_string = element_string.replace(
            "_TN_", table_names[random.randint(0, len(table_names) - 1)]
            )
    return element_string

def build_query(
    query_patterns, 
    select_element_patterns, 
    table_element_patterns, 
    column_names, 
    table_names
    ):
    query_string = query_patterns[(random.randrange(0, len(query_patterns)))]
    while "_SE_" in query_string:
        query_string = query_string.replace(
            "_SE_", 
            build_select_element(select_element_patterns, column_names, table_names),
            1
            )
    while "_TE_" in query_string:
        query_string = query_string.replace(
            "_TE_",
            build_table_element(table_element_patterns, table_names),
            1
        )
    return query_string


print(build_query(
    query_patterns, 
    select_element_patterns, 
    table_element_patterns, 
    column_names, 
    table_names
    ))
