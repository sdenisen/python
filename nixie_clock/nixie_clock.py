import RPi.GPIO as GPIO
import time
from nixie import convertToBinaryArray

__author__ = 'Sergey'


GPIO.setmode(GPIO.BOARD)

channels_nixie = [3, 5, 7, 11, 13, 15]
channels_digits = [40, 38, 36, 32]  # 8 - 4 - 2 - 1

GPIO.setup(channels_nixie, GPIO.OUT)
GPIO.setup(channels_digits, GPIO.OUT)


for channel in channels_nixie:
    GPIO.output(channel, GPIO.LOW)

for channel in channels_digits:
    GPIO.output(channel, GPIO.LOW)

while True:
    for channel in channels_nixie:
        GPIO.output(channel, GPIO.HIGH)
        for digit in range(9):
            b_array = convertToBinaryArray(digit)
            for i in range(4):
                GPIO.output(channels_digits[i], b_array[i])
            time.sleep(1)

            for channel in channels_digits:
                GPIO.output(channel, GPIO.LOW)

        time.sleep(1)
        GPIO.output(channel, GPIO.LOW)

        for channel in channels_nixie:
            GPIO.output(channel, GPIO.LOW)