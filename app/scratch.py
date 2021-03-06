import pandas as pd

query_xl = pd.read_excel('./artifacts/queries/user_study_master_query_list.xlsx')
for column in query_xl.columns:
    print(column)
    query_xl[column] = query_xl.apply(
        lambda row: row[column].replace('\n', ' ') if type(row[column]) == str else row[column],
        axis = 1
        )
query_xl.to_csv('./artifacts/queries/user_study_master_query_list.csv', sep='|')