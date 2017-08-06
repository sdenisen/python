__author__ = 'sdeni'
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

@app.route('/action/v1.0/goforward')
def action_go_forward():
    return "go forward action"

@app.route('/action/v1.0/stop')
def action_stop():
    return "stop action"

app.run(debug=True)