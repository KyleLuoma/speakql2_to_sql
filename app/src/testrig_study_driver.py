from user_study.study_driver import *
from db_util.db_connector import *
import pandas as pd

driver = StudyDriver(DbConnector(db_name='speakql_study', verbose=False))


# Register new session:
# driver.register_participant_session(25, 'p1')


# Get most recent session:
user_id = 25
# session_id = driver.get_most_recent_session_id(user_id)
# session_params = driver.get_session_params(session_id)
# print(session_params)

# Get query sequence used in current session:
# query_sequence = driver.get_query_sequence(session_params.iloc[0]['idsequence'])
# print(query_sequence)

# Insert query attempt into attempt table:
# driver.submit_attempt(
#     participant_id = user_id, 
#     query_id = 1, 
#     step = 1, 
#     transcript = "select everything from room", 
#     audio_filename = "dummy01.wav", 
#     time_taken = 24, 
#     used_speakql = 0, 
#     attempt_num = 1
# )

# Get last attempt submission
# result = driver.get_last_submitted_attempt(
#     user_id
# )
# print(result)

# Insert query commit into attempt table. Sparse table because we can reference
# the attempt submission table for remaining information.
# driver.save_attempt(
#     1, True
# )

# Get last attempt commit:
# result = driver.get_last_committed_attempt(
#     user_id
# )
# print(result)


next_prompt = driver.get_next_prompt(user_id)
print(next_prompt)