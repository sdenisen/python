__author__ = 'sdeni'

from WSController.engine_controller import EngineController
from flask import Flask

# TODO: how to escape exceptions and run EngineController object as singleton???

app = Flask(__name__)
engine_controller = EngineController()

@app.route("/")
def index():
    return "Hello World!"

@app.route('/action/v1.0/go/forward')
def action_go_forward():
    engine_controller.goForward()
    return "action_go_forward: success!"

@app.route('/action/v1.0/go/backward')
def action_go_backward():
    engine_controller.goBackward()
    return "action_go_backward: success!"

@app.route('/action/v1.0/go/left')
def action_go_left():
    engine_controller.goLeft()
    return "action_go_left: success!"

@app.route('/action/v1.0/go/right')
def action_go_right():
    engine_controller.goRight()
    return "action_go_right: success!"

@app.route('/action/v1.0/stop')
def action_stop():
    engine_controller.stop()
    return "action_stop: success!"


