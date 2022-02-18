import mysql.connector
import json
import pandas as pd

class DbConnector:

    def __init__(self, db_engine = "mysql", db_name = "speakql_university", config_dir = ""):
        
        print("Initializing DbConnector class for a", db_engine, " connection to", db_name)

        self.db_name = db_name
        self.db_engine = db_engine
        self.config_dir = config_dir
        self.connection = self.get_mysql_database_connector(db_name)

        print("DBCONNECTOR: Connected to", self.connection.get_server_info())



    def do_single_select_query_into_dataframe(self, query):

        print("DBCONNECTOR: Executing query '", query, "' in database", self.db_name)

        query.replace(";", "")
        
        if self.db_engine == "mysql":
            cursor = self.connection.cursor()
            cursor.execute(query)
            print(cursor.fetchall())
            cursor.close()



    def get_mysql_database_connector(self, db_name):

        print("Attempting to connect to", db_name)

        filepath = './app/src/db_util/'

        if len(self.config_dir) > 0:
            filepath = self.config_dir + filepath.replace("./", "/")

        db_info = json.load(open(filepath + db_name + "_db_info.json"))

        config = {
            'user': db_info["user"],
            'password': db_info["password"],
            'host': db_info["host"],
            'database': db_info["database"],
            'raise_on_warnings': True
        }

        return mysql.connector.connect(**config)

    #Static method (deprecated) keeps insert_data_into_db.py happy until we refactor that.
    def get_speakql_university_connector():
        db_info = json.load(open('./app/src/db_util/db_info.json'))

        config = {
            'user': db_info["user"],
            'password': db_info["password"],
            'host': db_info["host"],
            'database': db_info["database"],
            'raise_on_warnings': True
        }
        
        cnx = mysql.connector.connect(**config)
        return cnx


dbc = DbConnector(db_name = "speakql_university")
dbc.do_single_select_query_into_dataframe("select * from speakql_university.building")