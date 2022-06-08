from app import app
from flask import render_template, request
# https://flask-jwt-extended.readthedocs.io/en/stable/add_custom_data_claims/
from flask_jwt_extended import create_access_token, get_jwt, get_jwt_identity, unset_jwt_cookies, jwt_required, JWTManager
import flask
import base64
from .src.translator import *
from .src.speakql_speech_recognition.PollyVoice import *
from .src.speakql_speech_recognition.AsrStringProcessor import *
from .src.db_util.db_analyzer import *
from .src.db_util.db_connector import *

from flask_cors import CORS
#CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})
CORS(app, resources={r"/*": {"origins": "*"}})

db_connector = DbConnector()
study_db_connector = DbConnector(db_name = "speakql_study")
db_analyzer = DbAnalyzer(db_connector)
asr = AsrStringProcessor(db_analyzer)

jwt = JWTManager()
jwt.init_app(app)



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
    wav_blob = request.get_json()['wavBlob']
    count = request.get_json()['count']
    transcript = request.get_json()['transcript'].replace(" ", "-").replace(".", "")
    file = open('query_audio/user_recordings/' + "recording_test_" + str(count) + ".wav", 'wb')
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
    
    print(result_df)
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


if __name__ == '__main__':
    app.config["JWT_SECRET_KEY"] = 'insertsecretkeyhereforproduction'
    app.run(debug=True, port=5000)
    