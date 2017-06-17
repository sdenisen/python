__author__ = 'sdeni'

from HomeExplorerEngine.Motor import Motor
from HomeExplorerEngine.common_consts import *


class EngineController(object):

    def __init__(self):
        self.motor_ahead_left = Motor(PIN_AHEAD_LEFT_FORWARD, PIN_AHEAD_LEFT_BACKWARD, PIN_AHEAD_LEFT_PWM, "ahead left")
        self.motor_ahead_right = Motor(PIN_AHEAD_RIGHT_FORWARD, PIN_AHEAD_RIGHT_BACKWARD, PIN_AHEAD_RIGHT_PWM, "ahead right")

        self.motor_behind_right = Motor(PIN_BEHIND_RIGHT_FORWARD, PIN_BEHIND_RIGHT_BACKWARD, PIN_BEHIND_RIGHT_PWM, "behind right")
        self.motor_ahead_left.start()
        self.motor_behind_right.start()

        self.motor_behind_left = Motor(PIN_BEHIND_LEFT_FORWARD, PIN_BEHIND_LEFT_BACKWARD, PIN_BEHIND_LEFT_PWM, "behind left")
        self.motor_ahead_right.start()
        self.motor_behind_left.start()


    def goForward(self):
        print ("launch FORWARD action...")
        self.motor_ahead_left.event_forward.set()
        self.motor_ahead_right.event_forward.set()
        self.motor_behind_right.event_forward.set()
        self.motor_behind_left.event_forward.set()
        print ("set events")


    def goBackward(self):
        print ("launch BACKWARD action...")
        self.motor_ahead_left.event_backward.set()
        self.motor_ahead_right.event_backward.set()
        self.motor_behind_right.event_backward.set()
        self.motor_behind_left.event_backward.set()
        print ("set events")

    def goLeft(self):
        pass

    def goRight(self):
        pass

    def stop(self):
        print ("launch STOP action...")
        self.motor_ahead_left.event_stop.set()
        self.motor_ahead_right.event_stop.set()
        self.motor_behind_right.event_stop.set()
        self.motor_behind_left.event_stop.set()
        print ("set events")

    def calibrate(self):
        pass

    def cleanup(self):
        self.motor_ahead_left.kill()
        self.motor_ahead_right.kill()
        self.motor_behind_left.kill()
        self.motor_behind_right.kill()