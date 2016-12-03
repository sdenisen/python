import RPi.GPIO as GPIO
import time
from nixie import convertToBinaryArray

GPIO.setmode(GPIO.BOARD)

__author__ = 'Sergey'

class NixieClock():
    channels_nixie = [3, 5, 7, 11, 13, 15]
    channels_digits = [40, 38, 36, 32]  # 8 - 4 - 2 - 1
    def setupPins(self):
        GPIO.setup(self.channels_nixie, GPIO.OUT)
        GPIO.setup(self.channels_digits, GPIO.OUT)

    def resetNixiePins(self):
        GPIO.output( self.channels_nixie, map(int, str(GPIO.LOW)*len(self.channels_nixie)) )

    def resetChannelPins(self):
            GPIO.output( self.channels_digits, map(int, str(GPIO.LOW)*len(self.channels_digits)) )

nc = NixieClock()

nc.setupPins()
nc.resetChannelPins()
nc.resetNixiePins()

for channel in nc.channels_nixie:
    GPIO.output(channel, GPIO.HIGH)
    for i in range(10):
        b_array = convertToBinaryArray(i)
        print "digit = %s - %s" % (i, b_array)
        GPIO.output(nc.channels_digits, b_array)
        time.sleep(1)
    time.sleep(1)
    GPIO.output(channel, GPIO.LOW)