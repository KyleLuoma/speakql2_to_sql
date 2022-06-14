from app import app
from flask import render_template, request
# https://flask-jwt-extended.readthedocs.io/en/stable/add_custom_data_claims/
from flask_jwt_extended import create_access_token, get_jwt, get_jwt_identity, unset_jwt_cookies, jwt_required, JWTManager
import flask
import base64
import random
from .src.translator import *
from .src.speakql_speech_recognition.PollyVoice import *
from .src.speakql_speech_recognition.AsrStringProcessor import *
from .src.db_util.db_analyzer import *
from .src.db_util.db_connector import *
from sys import platform
import os
from .src.user_study.study_driver import StudyDriver 

from flask_cors import CORS
#CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})
CORS(app, resources={r"/*": {"origins": "*"}})

study_db_connector = DbConnector(db_name = "speakql_study", verbose = True)
study_driver = StudyDriver(study_db_connector)

db_connector = DbConnector(db_name = "speakql_university")
db_analyzer = DbAnalyzer(db_connector)
asr = AsrStringProcessor(db_analyzer)

jwt = JWTManager()
jwt.init_app(app)

cwd = os.getcwd().replace('\\', '/')
print('Current working directory:', cwd)



@app.route('/')
def index():
    return app.send_static_file('index.html')



@app.route('/test_query')
def test_query():
    speakql_query = "FROM TABLE ONE SHOW ME A, B AND C AND THEN FROM TABLE TWO T WHERE C = ONE.C SHOW ME C, D AND E"
    sql_query = full_query_translation(speakql_query)
    response = flask.jsonify({'sql_query': sql_query, 'speakql_query': speakql_query})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return (
        response
    )



@app.route('/do_query', methods = ['POST'])
def do_query():
    print("Data payload received from requestor", request.get_data(as_text = True))
    query = request.get_json()['query']
    print("Query Received from requestor:", query)
    translator_results = full_query_translation(query)
    print("Returning translator results for query", query)
    response = flask.jsonify({'query': translator_results['sql_query'], 'speakql_tree_json': translator_results['speakql_tree_json']})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return(response)



@app.route('/do_progressive_query', methods = ['POST'])
def do_progressive_query():
    print("Data payload received from requestor", request.get_data(as_text = True))
    query = request.get_json()['query']
    print("Query Received from requestor:", query)
    translator_results = full_query_translation_with_intermediate_steps(query)
    print("Returning translator results for query", query)
    response = flask.jsonify(translator_results)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return(response)



@app.route('/wav_data', methods = ['POST'])
def wav_data():

    recording_dir = cwd + '/query_audio/user_recordings/'
    if 'linux' in platform:
        recording_dir = '/root/srv/www/speakql2_to_sql/query_audio/user_recordings/'

    wav_blob = request.get_json()['wavBlob']
    username = request.get_json()['username']
    idparticipant = request.get_json()['idparticipant']
    idquery = request.get_json()['idquery']
    language = request.get_json()['language']
    transcript = request.get_json()['transcript'].replace(" ", "-").replace(".", "")

    attemptnum = study_driver.get_last_committed_attempt(idparticipant)
    if attemptnum.shape[0] > 0:
        attemptnum = attemptnum['attemptnum'][0]
    else:
        attemptnum = 1

    filename = (
        username + '_' + 'queryid-' + str(idquery) 
        + '_' + language + '-' + 'attempt-' + str(attemptnum) + '-{}.wav')

    counter = 1
    while os.path.exists(recording_dir + '/' + filename.format(str(counter))):
        counter += 1

    print("WAV DATA:", username, idparticipant, idquery, language, transcript)

    file = open(recording_dir + '/' + filename.format(str(counter)), 'wb')
    file.write(base64.b64decode(wav_blob))
    file.close()

    print("TRANSCRIPT OBJECT:", request.get_json()['transcript'], "END", str(len(request.get_json()['transcript'])))
    
    if not len(request.get_json()['transcript']) <= 1:
        response = flask.jsonify(
            asr.process_asr_string(request.get_json()['transcript'])
            )
        response.headers.add('Access-Control-Allow-Origin', '*')
    else: 
        response = flask.jsonify({})
    
    return(response)



@app.route('/study/get_next_prompt', methods = ['POST'])
def get_next_prompt():
    idparticipant = request.json.get('idparticipant', None)
    prompt = study_driver.get_next_prompt(int(idparticipant))
    prompt = prompt[['idquery', 'prompt', 'step', 'language']]
    response_dict = {'random': str(random.randint(0, 10000))}
    if prompt.shape[0] == 1:
        for column in prompt.columns:
            response_dict[column] = str(prompt[column][0])
    else:
        response_dict = {'error': 'Unable to retrieve next prompt'}
    response = flask.jsonify(response_dict)
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Cache-Control', 'no-store')
    return response



# Attempt submission. Payload:
#   idparticipant, idquery, idstep, transcript, audio_filename,
#   time_taken, used_speakql
@app.route('/study/submit_attempt', methods = ['POST'])
def submit_attempt():

    response_dict = {'msg': 'unable to submit'}

    if len(request.json['transcript']) == 0 or request.json['time_taken'] == 0:
        response_dict['msg'] = 'empty submission, did not save to database!'
    elif request.json['idsession'] > 0:
        study_driver.submit_attempt(
            session_id      = request.json['idsession'],
            participant_id  = request.json['idparticipant'],
            query_id        = request.json['idquery'],
            step            = request.json['idstep'],
            transcript      = request.json['transcript'],
            audio_filename  = request.json['audio_filename'],
            time_taken      = request.json['time_taken'],
            used_speakql    = request.json['used_speakql']
        )
        response_dict = {'msg': 'submission complete'}

    print(response_dict)
    response = flask.jsonify(response_dict)
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Cache-Control', 'no-store')

    return response



@app.route('/register_participant', methods = ['POST'])
def register_participant():
    participant = request.json.get('participant', None)
    if len(participant) == 0:
        return flask.jsonify({"msg": "No data in the participant field."})

    result_df = study_db_connector.do_select_from_parameters(
        # schema = 'speakql_study',
        columns = ['*'],
        table = ['participants']
        )
    result_df = result_df.where(result_df.username == participant).dropna(how = 'all')
    
    if result_df.shape[0] == 1:
        access_token = create_access_token(participant)
        response =  flask.jsonify(
            {
                'idparticipant': result_df['idparticipant'].to_list()[0],
                'username': result_df['username'].to_list()[0],
                'token': access_token
            }
        )
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    else:
        #Do create participant id here
        return flask.jsonify({'error': 'No participant id exists or created.'})



@app.route('/study/get_most_recent_session_id', methods = ['POST'])
def get_most_recent_session_id():
    idparticipant = request.json['idparticipant']
    response_dict = {'msg': 'unable to retrieve session for participant'}
    if str(idparticipant).isdigit():
        idsession = study_driver.get_most_recent_session_id(idparticipant)
        response_dict = {
            'idsession': int(idsession),
            'idparticipant' : int(idparticipant)
            }
    response = flask.jsonify(response_dict)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response



@app.route('/study/get_all_participant_attempts', methods = ['POST'])
def get_all_participant_attempts():
    attempts = study_driver.get_all_submitted_attempts(
        request.json['idparticipant'],
        request.json['idsession']
    )
    response_dict = {'msg': 'no submissions exist for this user'}
    if attempts.shape[0] > 0:
        response_dict = attempts.set_index('idattemptsubmission').transpose().to_dict()
    # print("GET ALL PARTICIPANT ATTEMPTS:\n", response_dict)
    response = flask.jsonify(response_dict)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response



@app.route('/study/get_attempt_submissions_since_last_commit', methods = ['POST'])
def get_attempt_submissions_since_last_commit():
    attempts = study_driver.get_attempt_submissions_since_last_commit(
        request.json['idparticipant'],
        request.json['idsession']
    )
    response_dict = {'msg': 'no submissions exist for this user'}
    if attempts.shape[0] > 0:
        response_dict = attempts.set_index('idattemptsubmission').transpose().to_dict()
    # print("GET ALL PARTICIPANT ATTEMPTS:\n", response_dict)
    response = flask.jsonify(response_dict)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response



@app.route('/study/get_all_committed_attempts', methods = ['POST'])
def get_all_committed_attempts():
    attempts = study_driver.get_all_comitted_attempts(
        request.json['idparticipant'],
        request.json['idsession']
    )
    print(attempts)
    print(request.json)
    response_dict = {'msg': 'no committed attempts exist for this user'}
    if attempts.shape[0] > 0:
        response_dict = attempts.set_index('idattemptsubmission').transpose().to_dict()
    # print("GET ALL PARTICIPANT ATTEMPTS:\n", response_dict)
    response = flask.jsonify(response_dict)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response



@app.route('/study/save_attempt', methods = ['POST'])
def save_attempt():

    is_correct = request.json['iscorrect'].lower() == 'true'

    study_driver.save_attempt(
        request.json['idattemptsubmissions'], 
        is_correct
    )
    response = flask.jsonify({'msg': 'Response saved and committed to db'})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response    



@app.route('/study/revert_attempt', methods = ['POST'])
def revert_attempt():

    study_driver.revert_attempt(
        request.json['idattemptsubmissions']
    )
    response = flask.jsonify({'msg': 'attempt reverted'})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response



@app.route('/study/get_all_participant_usernames', methods = ['POST'])
def get_all_participants():
    print("GETALLPARTICIPANTS!!!")
    participants = study_driver.get_all_participants()
    response = flask.jsonify(participants['username'].to_list())
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response



@app.route('/study/get_participant_id_from_username', methods = ['POST'])
def get_participant_id_from_username():
    id = study_driver.get_participant_id_from_username(request.json['username'])
    response = flask.jsonify({
        'idparticipant': int(id['idparticipant'][0]),
        'username': request.json['username']
        })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response



@app.route('/study/get_sequence_ids', methods = ["POST"])
def get_sequence_ids():
    print("GETSEQUENCEIDS!!!")
    sequence_ids = study_driver.get_all_sequence_ids()
    response = flask.jsonify(sequence_ids['idsequence'].to_list())
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response



@app.route('/study/register_participant_session', methods = ["POST"])
def register_participant_session():
    idparticipant = request.json['idparticipant']
    idsequence = request.json['idsequence']

    print('DEBUG', idparticipant, idsequence)

    response = {'msg': 'unable to register session, check parameters and try again.'}

    if str(idparticipant).isdigit() and idsequence in ['a', 'b', 'p1', 'p2']:
        study_driver.register_participant_session(idparticipant, idsequence)
        session_id = study_driver.get_most_recent_session_id(idparticipant)
        response = {'idsession': int(session_id)}
    
    response = flask.jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response



@app.route('/study/get_participant_sessions', methods = ['POST'])
def get_participant_sessions():
    idparticipant = request.json['idparticipant']

    response = {'msg': 'no sessions appear to exist for this participant'}
    if str(idparticipant).isdigit():
        sessions = study_driver.get_all_participant_sessions(idparticipant)
        response = flask.jsonify(sessions.transpose().to_dict())
        
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response



if __name__ == '__main__':
    app.config["JWT_SECRET_KEY"] = 'insertsecretkeyhereforproduction'
    app.run(debug=True, port=5000)
    