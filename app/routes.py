from app import app
from flask import render_template
from .speakql_src import translator as tr

@app.route('/')

@app.route('/index')
def index():
    return "Hello, FAM team!"

@app.route('/test_query')
def test_query():
    speakql_query = "FROM TABLE ONE SHOW ME A, B AND C AND THEN FROM TABLE TWO T WHERE C = ONE.C SHOW ME C, D AND E"
    sql_query = tr.run_test_query_translation(speakql_query)
    return (
        "<H1>SpeakQl Query</H1>"
        + speakql_query
        +"<H1>SQL Translation</H1>"
        + sql_query
    )

if __name__ == '__main__':
    app.run(debug=True, port=5000)