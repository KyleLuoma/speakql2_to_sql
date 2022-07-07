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
        if result.shape[0] > 0:
            return result.iloc[0]['idsession']
        else:
            return -1



    def get_all_participant_sessions(self, participant_id):
        query = """
        select * from session where idparticipant = {}
        """.format(str(participant_id))
        result = self.db_connector.do_single_select_query_into_dataframe(query)
        return result



    # Retrieve session parameters
    def get_session_params(self, session_id):
        query = """
        select * from session where idsession = {}
        """.format(str(session_id))
        result = self.db_connector.do_single_select_query_into_dataframe(query)
        return result



    def get_all_sequence_ids(self):
        query = """
        select distinct idsequence from query_sequences
        """
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
        self, session_id, participant_id, query_id, step, transcript,
        audio_filename, time_taken, used_speakql
        ):

        last_committed_attempt = self.get_last_committed_attempt(participant_id)
        attemptnum = 1
        if last_committed_attempt.shape[0] == 1:
            last_attempt_step = last_committed_attempt['idstep'][0]
            if float(last_attempt_step) == float(step):
                attemptnum = last_committed_attempt['attemptnum'][0] + 1

        transcript = transcript.replace("'", "''")
        transcript = transcript.replace(";", " semicolon ")

        query = """
        insert into attemptsubmissions (
            idattemptsubmission, idsession, idparticipant, idquery,
            idstep, transcript, audiofilename,
            time_taken, usedspeakql, attemptnum,
            reviewed
            ) 
        values(
            default, {}, {}, {},
            {}, '{}', '{}',
            {}, {}, {},
            default
            )
        """.format(
            str(session_id), str(participant_id), str(query_id),
            str(step), str(transcript), str(audio_filename),
            str(time_taken), str(used_speakql), str(attemptnum)
        )

        self.db_connector.do_single_insert_query_into_dataframe(query)

        attempt_id_query = """
        select max(idattemptsubmission) as idattemptsubmission
        from attemptsubmissions
        where idparticipant = {}
        """.format(str(participant_id))

        result = self.db_connector.do_single_select_query_into_dataframe(attempt_id_query)

        return result



    # Update the filename for an attempt after 
    def update_attempt_filename(self, audiofilename, idattemptsubmission):
        query = """
        update attemptsubmissions
        set audiofilename = '{}'
        where idattemptsubmission = '{}'
        """.format(audiofilename, idattemptsubmission)
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



    def revert_attempt(self, submission_id):
        query = """
        delete from attemptscommitted where idattemptsubmission = {}
        """.format(submission_id)
        result = self.db_connector.do_single_insert_query_into_dataframe(query)
        return result

    
    
    # Get the most recent attempt submitted by the participant
    def get_last_submitted_attempt(self, participant_id, session_id = None):
        if session_id == None:
            session_id = self.get_most_recent_session_id(participant_id)

        query = """
        select * 
        from attemptsubmissions
        where idattemptsubmission in (
            select max(idattemptsubmission) as idattemptsubmission
            from attemptsubmissions
            where idparticipant = {} and idsession = {}
        )
        """.format(str(participant_id), str(session_id))

        result = self.db_connector.do_single_select_query_into_dataframe(query)
        return result


    # Get the most recent attempt committed by the researcher for a participant
    def get_last_committed_attempt(self, participant_id, session_id = None):
        if session_id == None:
            session_id = self.get_most_recent_session_id(participant_id)

        attempt_id = self.get_last_committed_attempt_submission_id(participant_id, session_id)
        if attempt_id.shape[0] > 0:
            attempt_id = attempt_id['idattemptsubmission'][0]

        else:
            attempt_id = -1

        # if attempt_id == None:
        #     attempt_id = -1

        query = """
        select max(s.idattemptsubmission), c.iscorrect, c.idattemptcommitted, s.*
        from speakql_study.attemptscommitted c
        natural join speakql_study.attemptsubmissions s
        where 
            s.idparticipant = {} and idattemptsubmission = {}
		group by 
			c.idattemptcommitted,
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
        """.format(str(participant_id), str(attempt_id))
        result = self.db_connector.do_single_select_query_into_dataframe(query)
        return result



    def get_last_committed_attempt_submission_id(self, participant_id, session_id = None):
        if session_id == None:
            session_id = self.get_most_recent_session_id(participant_id)

        query = """
        select max(s.idattemptsubmission) as idattemptsubmission
        from speakql_study.attemptscommitted c
        natural join speakql_study.attemptsubmissions s
        where s.idparticipant = {} and s.idsession = {}
        """.format(str(participant_id), str(session_id))

        result = self.db_connector.do_single_select_query_into_dataframe(query)
        return result



    # Retrieve all submitted attempts made by the participant
    def get_all_submitted_attempts(self, participant_id, session_id = None):
        if session_id == None:
            session_id = self.get_most_recent_session_id(participant_id)

        query = """
        select s.*, c.idattemptcommitted, c.iscorrect
        from attemptsubmissions s
        left join attemptscommitted c 
        on s.idattemptsubmission = c.idattemptsubmission
        where s.idparticipant = {} and s.idsession = {};
        """.format(str(participant_id), str(session_id))

        result = self.db_connector.do_single_select_query_into_dataframe(query)
        result.fillna(value = '', inplace = True)
        return result



    def get_attempt_submissions_since_last_commit(self, participant_id, session_id = None):
        if session_id == None:
            session_id = self.get_most_recent_session_id(participant_id)

        query = """
        select *
        from attemptsubmissions
        where 
            idparticipant = {} 
            and idattemptsubmission > (
                select max(idattemptsubmission) 
                from attemptscommitted c
                natural join attemptsubmissions s
                where idparticipant = {} and idsession = {}
            )
        """.format(str(participant_id), str(participant_id), str(session_id))
        result = self.db_connector.do_single_select_query_into_dataframe(query)

        if result.shape[0] == 0:
            result = self.get_all_submitted_attempts(participant_id, session_id)
            last_commit = self.get_last_committed_attempt_submission_id(participant_id, session_id)
            print("DEBUG:", last_commit)
            if last_commit.shape[0] == 1 and last_commit['idattemptsubmission'][0] != None:
                result = result.where(
                    result.idattemptsubmission > last_commit['idattemptsubmission'][0]
                    ).dropna(how = 'all')
        result.fillna(value = '', inplace = True)
        return result



    # Retrieve all committed attempts made by the participant
    def get_all_comitted_attempts(self, participant_id, session_id = None):
        if session_id == None:
            session_id = self.get_most_recent_session_id(participant_id)
        query = """
        select s.*, c.idattemptcommitted, c.iscorrect
        from attemptsubmissions s
        natural join attemptscommitted c
        where idparticipant = {} and idsession = {}
        """.format(str(participant_id), str(session_id))
        result = self.db_connector.do_single_select_query_into_dataframe(query)
        return result




    def get_session_sequence_and_attempts(self, session_id):

        session_params = self.get_session_params(session_id)

        query = """
        select qs.*, 
            asub.idattemptsubmission, 
            asub.idparticipant,
            asub.idsession,
            asub.transcript,
            asub.audiofilename,
            asub.time_taken,
            asub.attemptnum,
            ac.idattemptcommitted,
            ac.iscorrect
        from query_sequences as qs
        left join (select * from attemptsubmissions where idsession = {}) as asub
            on asub.idstep = qs.step
            and asub.idquery = qs.idquery
        left join attemptscommitted ac on asub.idattemptsubmission = ac.idattemptsubmission
        where qs.idsequence = '{}'
        order by qs.step, asub.idattemptsubmission
        """.format(
            str(session_id),
            str(session_params['idsequence'][0])
        )
        result = self.db_connector.do_single_select_query_into_dataframe(query)
        return result



    # Retreive the next prompt in the sequence, or return the current prompt
    # if the last attempt is < 3 and not correct.
    def get_next_prompt(self, participant_id, session_id = None):
        last_attempt = self.get_last_committed_attempt(participant_id)
        step = 1
        iscorrect = 0
        attempt_num = 1
        if last_attempt.shape[0] > 0:
            step = last_attempt.iloc[0]['idstep']
            iscorrect = last_attempt.iloc[0]['iscorrect']
            attempt_num = last_attempt.iloc[0]['attemptnum']

        if session_id == None:
            session_id = self.get_most_recent_session_id(participant_id)
        session_params = self.get_session_params(session_id)
        sequence_id = session_params.iloc[0]['idsequence']

        sequences = self.get_query_sequence(sequence_id)

        if iscorrect == 1 or attempt_num >= 3:
            step += 1
            attempt_num = 1

        sequence = sequences.where(sequences.step == step).dropna(how = 'all').reset_index(drop = True)

        query_id = sequence.iloc[0]['idquery']

        prompt_df = self.get_query_data(query_id)
        joined_df = prompt_df.join(sequence, rsuffix = "_sequence")        

        return joined_df



    def get_query_data(self, idquery):
        query = """
        select *
        from queries
        where idquery = {}
        """.format(str(idquery))
        prompt_df = self.db_connector.do_single_select_query_into_dataframe(query)
        return prompt_df



    def get_all_participants(self):
        query = """
        select * from participants
        """
        result = self.db_connector.do_single_select_query_into_dataframe(query)
        return result



    def get_participant_id_from_username(self, username):
        query = """
        select idparticipant from participants
        where username = '{}'
        """.format(username)
        result = self.db_connector.do_single_select_query_into_dataframe(query)
        return result
        

        






