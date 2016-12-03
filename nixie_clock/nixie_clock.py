import RPi.GPIO as GPIO
import time
from nixie import NixieTube

GPIO.setmode(GPIO.BOARD)

__author__ = 'Sergey'


class NixieClock(object):
    channels_tube_sec = [13, 15]
    channels_tube_hm = [3, 5, 7, 11]
    channels_digits = [40, 38, 36, 32]  # 8 - 4 - 2 - 1

    def setupPins(self):
        GPIO.setup(self.channels_tube_hm, GPIO.OUT)
        GPIO.setup(self.channels_tube_sec, GPIO.OUT)
        GPIO.setup(self.channels_digits, GPIO.OUT)

    def resetNixiePins(self):
        GPIO.output(self.channels_tube_hm, map(int, str(GPIO.LOW) * len(self.channels_tube_hm)))
        GPIO.output(self.channels_tube_sec, map(int, str(GPIO.LOW) * len(self.channels_tube_sec)))

    def resetChannelPins(self):
        GPIO.output(self.channels_digits, map(int, str(GPIO.LOW) * len(self.channels_digits)))


nc = NixieClock()
nt_h = NixieTube(NixieTube.TUBE_TYPE_HOURS_MINUTES, nc.channels_digits)
nt_s = NixieTube(NixieTube.TUBE_TYPE_SECONDS, nc.channels_digits)

nc.setupPins()
nc.resetChannelPins()
nc.resetNixiePins()

for channel in nc.channels_tube_hm:
    GPIO.output(channel, GPIO.HIGH)
    for i in range(10):
        nt_h.show(i)
        time.sleep(1)
    time.sleep(1)
    GPIO.output(channel, GPIO.LOW)

for channel in nc.channels_tube_sec:
    GPIO.output(channel, GPIO.HIGH)
    for i in range(10):
        nt_s.show(i)
        time.sleep(1)
    time.sleep(1)
    GPIO.output(channel, GPIO.LOW)
