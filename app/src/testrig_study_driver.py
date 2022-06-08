from user_study.study_driver import *
from db_util.db_connector import *
import pandas as pd

driver = StudyDriver(DbConnector(db_name='speakql_study', verbose=True))


# Register new session:
driver.register_participant_session(25, 'p1')


# Get most recent session:
user_id = 25
session_id = driver.get_most_recent_session_id(user_id)
session_params = driver.get_session_params(session_id)
print(session_params)

# Get query sequence used in current session:
query_sequence = driver.get_query_sequence(session_params.iloc[0]['idsequence'])
print(query_sequence)

# Insert query attempt into attempt table:
driver.submit_attempt(
    25, 1, 1, "select everything from room", "dummy01.wav", 24, 0, 1
)

