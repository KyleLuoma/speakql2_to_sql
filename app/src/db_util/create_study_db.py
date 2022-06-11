import db_connector
import mysql.connector


commands = []



participants_table = """CREATE TABLE IF NOT EXISTS participants (
                                idparticipant int NOT NULL AUTO_INCREMENT,
                                username varchar(32) NOT NULL UNIQUE,
                                primary key(idparticipant)
                            )"""
commands.append(participants_table)


# Include participant id, query sequence id, last completed step
participant_session_table = """CREATE TABLE IF NOT EXISTS session (
                                idsession int NOT NULL AUTO_INCREMENT,
                                idparticipant int NOT NULL,
                                idsequence varchar(8) NOT NULL,
                                primary key (idsession)
                            )"""
commands.append(participant_session_table)



query_sequences_table = """CREATE TABLE IF NOT EXISTS query_sequences (
                            idsequence varchar(8) NOT NULL,
                            step int NOT NULL,
                            idquery varchar(8) NOT NULL,
                            speakql_first int NOT NULL,
                            language varchar(16) NOT NULL
                        )"""
commands.append(query_sequences_table)



queries_table = """CREATE TABLE IF NOT EXISTS `queries` (
                        `idquery` int DEFAULT NULL,
                        `prompt` text,
                        `speakql_example_1` text,
                        `speakql_example_2` text,
                        `sql_example` text,
                        `synonym` int DEFAULT NULL,
                        `natural_functions` int DEFAULT NULL,
                        `exp_ordering` int DEFAULT NULL,
                        `mod_ordering` int DEFAULT NULL,
                        `unbundle_join` int DEFAULT NULL,
                        `unbundle_agg` int DEFAULT NULL,
                        `num_tables` int DEFAULT NULL,
                        `tables` text,
                        `num_proj` int DEFAULT NULL,
                        `projections` text,
                        `num_funcs` int DEFAULT NULL,
                        `functions` text,
                        `num_selections` int DEFAULT NULL,
                        `selection` text,
                        `num_joins` int DEFAULT NULL,
                        `joins` text,
                        `num_mods` int DEFAULT NULL,
                        `modifiers` text,
                        `complexity` double DEFAULT NULL,
                        `normalized` double DEFAULT NULL,
                        `is_complex` int DEFAULT NULL
                        )"""
commands.append(queries_table)



attempt_sumbission_table = """CREATE TABLE IF NOT EXISTS attemptsubmissions (
                                idattemptsubmission int NOT NULL AUTO_INCREMENT,
                                idparticipant int NOT NULL,
                                idsession int NOT NULL,
                                idquery int NOT NULL,
                                idstep int NOT NULL,
                                transcript varchar(1024) NOT NULL,
                                audiofilename varchar(256) NOT NULL,
                                time_taken int NOT NULL,
                                usedspeakql int NOT NULL,
                                attemptnum int NOT NULL,
                                reviewed int NOT NULL DEFAULT 0,
                                primary key(idattemptsubmission)
                            )"""
commands.append(attempt_sumbission_table)



attempt_committed_table = """CREATE TABLE IF NOT EXISTS attemptscommitted (
                                idattemptcommitted int NOT NULL AUTO_INCREMENT,
                                idattemptsubmission int NOT NULL UNIQUE,
                                iscorrect int NOT NULL,
                                primary key (idattemptcommitted)
                            )"""
commands.append(attempt_committed_table)

connector = db_connector.DbConnector()

for command in commands:
    try:
        cnx = connector.get_speakql_university_connector('speakql_study')
        cursor = cnx.cursor()
        result = cursor.execute(command)
        print("Table created successfully ")

    except mysql.connector.Error as error:
        # print(command)
        print("Failed to create table in MySQL: {}".format(error))
        
    finally:
        if cnx.is_connected():
            cursor.close()
            cnx.close()
            print("MySQL connection is closed")