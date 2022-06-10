from operator import is_
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
        audio_filename, time_taken, used_speakql
        ):

        last_committed_attempt = self.get_last_committed_attempt(participant_id)
        attemptnum = 1
        if last_committed_attempt.shape[0] == 1:
            attemptnum = last_committed_attempt['attemptnum'][0] + 1

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
            str(time_taken), str(used_speakql), str(attemptnum)
        )

        result = self.db_connector.do_single_insert_query_into_dataframe(query)
        return result



    # Log validated query attempt in database
    def save_attempt(
        self, submission_id, is_correct
        ):
        correct = 0
        if is_correct:
            correct = 1
        query = """
        insert into attemptscommitted (
            idattemptcommitted, idattemptsubmission, iscorrect
            ) 
        values(
            default, {}, {}
            )
        """.format(
            str(submission_id), str(correct)
        )

        result = self.db_connector.do_single_insert_query_into_dataframe(query)
        return result

    
    
    # Get the most recent attempt submitted by the participant
    def get_last_submitted_attempt(self, participant_id):
        query = """
        select * 
        from attemptsubmissions
        where idattemptsubmission in (
            select max(idattemptsubmission) as idattemptsubmission
            from attemptsubmissions
            where idparticipant = {}
        )
        """.format(str(participant_id))
        result = self.db_connector.do_single_select_query_into_dataframe(query)
        return result


    # Get the most recent attempt committed by the researcher for a participant
    def get_last_committed_attempt(self, participant_id):
        query = """
        select max(c.idattemptcommitted), c.*, s.*
        from speakql_study.attemptscommitted c
        natural join speakql_study.attemptsubmissions s
        where 
            s.idparticipant = {}
		group by 
			c.idattemptcommitted,
            c.idattemptsubmission,
            c.iscorrect,
            s.idattemptsubmission,
            s.idparticipant,
            s.idquery,
            s.idstep,
            s.transcript,
            s.audiofilename,
            s.time_taken,
            s.usedspeakql,
            s.attemptnum,
            s.reviewed
        """.format(str(participant_id))
        result = self.db_connector.do_single_select_query_into_dataframe(query)
        return result



    # Retrieve all submitted attempts made by the participant
    def get_all_submitted_attempts(self, participant_id):
        query = """
        select s.*, c.idattemptcommitted, c.iscorrect
        from attemptsubmissions s
        left join attemptscommitted c 
        on s.idattemptsubmission = c.idattemptsubmission
        where s.idparticipant = {};
        """.format(str(participant_id))
        result = self.db_connector.do_single_select_query_into_dataframe(query)
        result.fillna(value = '', inplace = True)
        return result



    def get_attempt_submissions_since_last_commit(self, participant_id):
        query = """
        select *
        from attemptsubmissions
        where 
            idparticipant = {} 
            and idattemptsubmission > (
                select max(idattemptsubmission) 
                from attemptscommitted c
                natural join attemptsubmissions s
                where idparticipant = {}
            )
        """.format(str(participant_id), str(participant_id))
        result = self.db_connector.do_single_select_query_into_dataframe(query)
        result.fillna(value = '', inplace = True)
        return result



    # Retrieve all committed attempts made by the participant
    def get_all_comitted_attempts(self, participant_id):
        query = """
        select s.*, c.idattemptcommitted, c.iscorrect
        from attemptsubmissions s
        natural join attemptscommitted c
        where idparticipant = {}
        """.format(str(participant_id))
        result = self.db_connector.do_single_select_query_into_dataframe(query)
        return result



    # Retreive the next prompt in the sequence, or return the current prompt
    # if the last attempt is < 3 and not correct.
    def get_next_prompt(self, participant_id):
        last_attempt = self.get_last_committed_attempt(participant_id)
        step = last_attempt.iloc[0]['idstep']
        iscorrect = last_attempt.iloc[0]['iscorrect']
        attempt_num = last_attempt.iloc[0]['attemptnum']

        session_id = self.get_most_recent_session_id(participant_id)
        session_params = self.get_session_params(session_id)
        sequence_id = session_params.iloc[0]['idsequence']

        sequences = self.get_query_sequence(sequence_id)

        if iscorrect or attempt_num >= 3:
            step += 1

        sequence = sequences.where(sequences.step == step).dropna(how = 'all').reset_index(drop = True)

        query_id = sequence.iloc[0]['idquery']

        queries_query = """
        select *
        from queries
        where idquery = {}
        """.format(str(query_id))
        prompt_df = self.db_connector.do_single_select_query_into_dataframe(queries_query)
        joined_df = prompt_df.join(sequence, rsuffix = "_sequence")        

        return joined_df
        

        






