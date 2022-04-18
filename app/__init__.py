from flask import Flask, render_template, session
from flask_cors import CORS

app = Flask(
    __name__, template_folder='./templates', 
    static_folder='./react_app/build', 
    static_url_path='/'
    )
app.secret_key = "placeholder"
SESSION_TYPE = 'redis'
app.config.from_object(__name__)
CORS(app)
from app import routes
