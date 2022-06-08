import sys
sys.path.append("..") # Adds higher directory to python modules path.

# from ..db_util.db_connector import *
import pandas as pd

class StudyDriver:

    def __init__(self, db_connector):
        self.db_connector = db_connector
    


    # Insert a row into participant session table to set the initial parameters
    # for the session including participant id, and query sequence id
    def register_participant_session(self, participant_id, sequence_id):
        query = """
        insert into speakql_study.session (idsession, idparticipant, idsequence) values(default, {}, '{}')
        """.format(str(participant_id), str(sequence_id))
        result = self.db_connector.do_single_insert_query_into_dataframe(query)
        return result



    def get_most_recent_session_id(self, participant_id):
        query = """
        select max(idsession) as idsession 
        from session
        where idparticipant = {}
        """.format(str(participant_id))
        result = self.db_connector.do_single_select_query_into_dataframe(query)
        return result.iloc[0]['idsession']



    # Retrieve session parameters
    def get_session_params(self, session_id):
        query = """
        select * from session where idsession = {}
        """.format(str(session_id))
        result = self.db_connector.do_single_select_query_into_dataframe(query)
        return result


    # Retrieve query sequence from database (ids ar a, b, p1 or p2)
    # Returns dataframe with columns idsequence, idquery, step, speakql_first
    def get_query_sequence(self, sequence_id):
        query = """
        select * 
        from query_sequences
        where idsequence = '{}';
        """.format(str(sequence_id))
        result = self.db_connector.do_single_select_query_into_dataframe(query)
        return result


    # Submit attempt for review. Should go into a separate table with pending attempts.
    # Once the attempt is reviewed and marked correct or incorrect, then call save_attempt
    # to save it in validated attempt table.
    def submit_attempt(
        self, participant_id, query_id, step, transcript,
        audio_filename, time_taken, used_speakql, attempt_num
        ):
        query = """
        insert into attemptsubmissions (
            idattemptsubmission, idparticipant, idquery,
            idstep, transcript, audiofilename,
            time_taken, usedspeakql, attemptnum,
            reviewed
            ) 
        values(
            default, {}, {},
            {}, '{}', '{}',
            {}, {}, {},
            default
            )
        """.format(
            str(participant_id), str(query_id),
            str(step), str(transcript), str(audio_filename),
            str(time_taken), str(used_speakql), str(attempt_num)
        )

        result = self.db_connector.do_single_insert_query_into_dataframe(query)
        return result



    # Log validated query attempt in database
    def save_attempt(
        self, participant_id, query_id, step, transcript, 
        audio_filename, time_taken, used_speakql, attempt_num, is_correct
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






