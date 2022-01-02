from flask import Flask, render_template
from flask_cors import CORS
app = Flask(__name__, template_folder='./templates')
CORS(app)
from app import routes
