__author__ = 'sdeni'
from threading import Thread, Event
import RPi.GPIO as GPIO


class Motor(Thread):

    def __init__(self, pin_forward, pin_backward, pin_pwm, name=""):
        """
        :param pin_forward:
        :param pin_backward:
        :param name:
        """
        Thread.__init__(self)
        self.name = name
        self.event_forward = Event()
        self.event_backward = Event()
        self.event_stop = Event()
        self.pin_forward = pin_forward
        self.pin_backward = pin_backward
        self.stop_thread = True
        self.pin_pwm = pin_pwm

        GPIO.setup(self.pin_pwm, GPIO.OUT)
        self.my_pwm = GPIO.PWM(self.pin_pwm, 100)

        self.calibration = 100

    def run(self):
        while True:
            if self.event_forward.is_set():
                self._stopAction()
                self._goForward()
                self.event_forward.clear()

            elif self.event_backward.is_set():
                self._stopAction()
                self._goBackWard()
                self.event_backward.clear()

            elif self.event_stop.is_set():
                self._stopAction()
                self.event_stop.clear()

            if not self.stop_thread:
                break

        self.my_pwm._stopAction()

    def _goForward(self):
        print ("[ %s ]: action 'go forward'" % self.name)
        self.my_pwm.start(100)
        self.my_pwm.ChangeDutyCycle(self.calibration)
        GPIO.output(self.pin_forward, GPIO.HIGH)


    def _goBackWard(self):
        print ("[ %s ]: action 'go backward'" % self.name)
        self.my_pwm.start(100)
        self.my_pwm.ChangeDutyCycle(self.calibration)
        GPIO.output(self.pin_backward, GPIO.HIGH)

    def _stopAction(self):
        print ("[ %s ]: action 'stop'" % self.name)
        GPIO.output(self.pin_forward, GPIO.LOW)
        GPIO.output(self.pin_backward, GPIO.LOW)

    def kill(self):
        self.stop_thread = False