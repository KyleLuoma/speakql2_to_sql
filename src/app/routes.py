from app import app
from flask import render_template
from flask import request
import flask
from src.speakql_translator import translator as tr
from flask_cors import CORS
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})


@app.route('/')

@app.route('/index')
def index():
    return "Hello, FAM team!"

@app.route('/test_query')
def test_query():
    speakql_query = "FROM TABLE ONE SHOW ME A, B AND C AND THEN FROM TABLE TWO T WHERE C = ONE.C SHOW ME C, D AND E"
    sql_query = tr.run_test_query_translation(speakql_query)
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
    sql_query = tr.run_test_query_translation(query)
    response = flask.jsonify({'query': sql_query})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return(response)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

