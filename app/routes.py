from app import app
from flask import render_template
from flask import request
import flask
import base64
from .src.translator import *
from .src.speakql_speech_recognition.PollyVoice import *
from flask_cors import CORS
#CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})
CORS(app, resources={r"/*": {"origins": "*"}})



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
    print("Wav file payload received from requestor.")
    wav_blob = request.get_json()['wavBlob']
    count = request.get_json()['count']
    transcript = request.get_json()['transcript'].replace(" ", "-").replace(".", "")
    file = open('query_audio/user_recordings/' + "recording_test_" + transcript + ".wav", 'wb')
    file.write(base64.b64decode(wav_blob))
    file.close()
    response = flask.jsonify({"status" : "blank"})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return(response)


if __name__ == '__main__':
    app.run(debug=True, port=5000)

