__author__ = 'sdeni'

from threading import Event
from HomeExplorerEngine.WSController.motor import Motor
from WSController.common_consts import *


class EngineController(object):

    def __init__(self):
        self.action_event = Event()
        self.motor_ahead_left = Motor(PIN_AHEAD_LEFT_FORWARD, PIN_AHEAD_LEFT_BACKWARD,
                                      PIN_AHEAD_LEFT_PWM, "ahead left", self.action_event)
        self.motor_ahead_right = Motor(PIN_AHEAD_RIGHT_FORWARD, PIN_AHEAD_RIGHT_BACKWARD,
                                       PIN_AHEAD_RIGHT_PWM, "ahead right", self.action_event)

        self.motor_behind_right = Motor(PIN_BEHIND_RIGHT_FORWARD, PIN_BEHIND_RIGHT_BACKWARD,
                                        PIN_BEHIND_RIGHT_PWM, "behind right", self.action_event)
        self.motor_ahead_left.start()
        self.motor_behind_right.start()

        self.motor_behind_left = Motor(PIN_BEHIND_LEFT_FORWARD, PIN_BEHIND_LEFT_BACKWARD,
                                       PIN_BEHIND_LEFT_PWM, "behind left", self.action_event)
        self.motor_ahead_right.start()
        self.motor_behind_left.start()


    def goForward(self):
        print ("launch FORWARD action...")
        self.motor_ahead_left.action = ACTION_GO_FORWARD
        self.motor_ahead_right.action =ACTION_GO_FORWARD
        self.motor_behind_right.action = ACTION_GO_FORWARD
        self.motor_behind_left.action = ACTION_GO_FORWARD
        self.action_event.set()
        print ("set events")


    def goBackward(self):
        print ("launch BACKWARD action...")
        self.motor_ahead_left.action = ACTION_GO_BACKWARD
        self.motor_ahead_right.action = ACTION_GO_BACKWARD
        self.motor_behind_right.action = ACTION_GO_BACKWARD
        self.motor_behind_left.action = ACTION_GO_BACKWARD
        self.action_event.set()
        print ("set events")

    def goLeft(self):
        print ("launch LEFT action...")
        self.motor_ahead_left.action = ACTION_GO_BACKWARD
        self.motor_ahead_right.action = ACTION_GO_FORWARD
        self.motor_behind_right.action = ACTION_GO_BACKWARD
        self.motor_behind_left.action = ACTION_GO_FORWARD
        self.action_event.set()
        print ("set events")

    def goRight(self):
        print ("launch RIGHT action...")
        self.motor_ahead_left.action = ACTION_GO_FORWARD
        self.motor_ahead_right.action = ACTION_GO_BACKWARD
        self.motor_behind_right.action = ACTION_GO_FORWARD
        self.motor_behind_left.action = ACTION_GO_BACKWARD
        self.action_event.set()
        print ("set events")

    def stop(self):
        print ("launch STOP action...")
        self.motor_ahead_left.action = ACTION_STOP
        self.motor_ahead_right.action = ACTION_STOP
        self.motor_behind_right.action = ACTION_STOP
        self.motor_behind_left.action = ACTION_STOP
        self.action_event.set()
        print ("set events")

    def calibrate(self):
        pass

    def cleanup(self):
        self.motor_ahead_left.kill()
        self.motor_ahead_right.kill()
        self.motor_behind_left.kill()
        self.motor_behind_right.kill()