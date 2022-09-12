from flask import Flask

# initialize app

app = Flask(__name__)

# routes
@app.route("/")
def welcome():
    return "Hello World!"

@app.route('/home')
def home():
    return " this is home."

from controllers import *