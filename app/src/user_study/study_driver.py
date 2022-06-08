from ..db_util.db_connector import *
import pandas as pd

class StudyDriver:

    def __init__(self, db_connector = DbConnector(db_name = "speakql_study")):
        self.db_connector = db_connector
    


    # Insert a row into participant session table to set the initial parameters
    # for the session including participant id, and query sequence id
    def register_participant_session(self, participant_id, sequence_id):
        pass



    # Retrieve participant session parameters
    def get_participant_session_params(self, participant_id):
        pass



    # Retrieve query sequence from database (ids ar a, b, p1 or p2)
    # Returns dataframe with columns idsequence, idquery, step, speakql_first
    def get_query_sequence(self, participant_id):
        query = """
        select * 
        from speakql_study.query_sequences
        where idsequence = '{sequence_id}';
        """
        result = self.db_connector.do_single_select_query_into_dataframe(query)
        return result


    # Submit attempt for review. Should go into a separate table with pending attempts.
    # Once the attempt is reviewed and marked correct or incorrect, then call save_attempt
    # to save it in validated attempt table.
    def submit_attempt(
        self, participant_id, query_id, step, transcript,
        audio_filename, time_taken, language, attempt_num
        ):
        pass



    # Log validated query attempt in database
    def save_attempt(
        self, participant_id, query_id, step, transcript, 
        audio_filename, time_taken, language, attempt_num, is_correct
        ):
        pass

    
    
    # Get the most recent attempt performed by the participant
    def get_last_attempt(self, participant_id):
        pass



    # Retrieve all commited attempts made by the participant
    def get_all_attempts(self, participant_id):
        pass



    # Retreive the next prompt in the sequence, or return the current prompt
    # if the last attempt is < 3 and not correct.
    def get_next_prompt(self, participant_id):
        pass







