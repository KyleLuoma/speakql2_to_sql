from app import app
from flask import render_template
from .speakql_src import translator as tr

@app.route('/')

@app.route('/index')
def index():
    return "Hello, FAM team!"

@app.route('/test_query')
def test_query():
    return tr.run_test_query_translation("SELECT A FROM ONE WHERE A = 1")

if __name__ == '__main__':
    app.run(debug=True, port=5000)