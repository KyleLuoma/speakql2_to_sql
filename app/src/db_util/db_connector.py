import mysql.connector
import json

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
