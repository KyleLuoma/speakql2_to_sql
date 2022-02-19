
from .db_connector import *
import pandas as pd

class DbAnalyzer:

    def __init__(self, db_connector):

        self.db_connector = db_connector
        self.table_names = self._get_table_names()
        self.column_names = self._get_column_names()
        self.distinct_values = self._get_distinct_values()



    def get_column_names(self):
        return self.column_names

    def get_table_names(self):
        return self.table_names

    def get_distinct_values(self):
        return self.distinct_values

    

    def _get_distinct_values(self):

        values = pd.DataFrame(columns = {"tab_name", "col_name", "val"})

        query = """select "{}" as tab_name, "{}" as col_name, val 
                   from (select distinct({}) as val from {}) vals
                """

        for column in self.column_names.itertuples():
            if column.DATA_TYPE == "varchar":
                print(column.COLUMN_NAME)
                new_values = self.db_connector.do_single_select_query_into_dataframe(
                    query.format(
                        column.TABLE_NAME, 
                        column.COLUMN_NAME, 
                        column.COLUMN_NAME, 
                        column.TABLE_NAME
                    )
                )
                values = pd.concat([values, new_values])
        
        return values



    def _get_column_names(self):

        query = ""

        if self.db_connector.get_db_engine() == "mysql":
            query = """select table_name, column_name, data_type, column_key
                        from information_schema.columns 
                        where table_name in (
                            select table_name 
                            from information_schema.columns 
                            where table_schema = "{}" 
                        )
                    """
        
        return self.db_connector.do_single_select_query_into_dataframe(
            query.format(self.db_connector.get_db_name())
        )



    def _get_table_names(self):

        query = ""

        if self.db_connector.get_db_engine() == "mysql":
            query = """select table_name
                       from information_schema.tables
                       where table_schema = "{}"
            """

        return self.db_connector.do_single_select_query_into_dataframe(
            query.format(self.db_connector.get_db_name())
        ) 

