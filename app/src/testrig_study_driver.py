from user_study.study_driver import *
from db_util.db_connector import *

driver = StudyDriver(DbConnector(db_name='speakql_study'))

driver.register_participant_session(25, 'a')