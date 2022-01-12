from flask import Flask, render_template
from flask_cors import CORS
app = Flask(__name__, template_folder='./templates', static_folder='./react_app/build', static_url_path='/')
CORS(app)
from app import routes
