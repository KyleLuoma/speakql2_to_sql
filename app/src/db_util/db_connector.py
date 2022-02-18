import mysql.connector
import json

class DbConnector:

    def __init__(self, db_engine = "mysql", db_name = "speakql_university"):

        self.db_engine = db_engine

        if self.db_engine == "mysql" :
            self.connection = self.get_mysql_database_connector()


    def get_mysql_database_connector(self, db_name):
        db_info = json.load(open('./app/src/dbutil/' + db_name + "_db_info.json"))

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
