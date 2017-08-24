__author__ = 'sdeni'
from threading import Thread, Event
import RPi.GPIO as GPIO
from WSController.common_consts import ACTION_GO_FORWARD, ACTION_GO_BACKWARD, ACTION_STOP


class Motor(Thread):

    def __init__(self, pin_forward, pin_backward, pin_pwm, name="", event=None):
        """
        :param pin_forward:
        :param pin_backward:
        :param name:
        """
        Thread.__init__(self)
        self.name = name
        self.event = event
        self.pin_forward = pin_forward
        self.pin_backward = pin_backward
        self.stop_thread = True
        self.pin_pwm = pin_pwm
        self.action = None
        self.params = None
        GPIO.setup(self.pin_pwm, GPIO.OUT)
        self.my_pwm = GPIO.PWM(self.pin_pwm, 100)

        self.calibration = 100

    def run(self):
        while True:
            self.event.wait()
            self.doAction()

            if not self.stop_thread:
                break
            self.event.clear()

        self.my_pwm._stopAction()

    def doAction(self):
        print ("Action [%s] starts; use the following params: [%s] " % (self.action, self.params))
        self.my_pwm.start(100)
        if self.action == ACTION_GO_FORWARD:
            self.my_pwm.ChangeDutyCycle(self.calibration)
            GPIO.output(self.pin_forward, GPIO.HIGH)

        elif self.action == ACTION_GO_BACKWARD:
            self.my_pwm.ChangeDutyCycle(self.calibration)
            GPIO.output(self.pin_backward, GPIO.HIGH)

        elif self.action == ACTION_STOP:
            GPIO.output(self.pin_forward, GPIO.LOW)
            GPIO.output(self.pin_backward, GPIO.LOW)

    def kill(self):
        self.stop_thread = False