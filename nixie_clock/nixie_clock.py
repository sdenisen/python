import RPi.GPIO as GPIO
from socket import AF_INET, SOCK_DGRAM
import socket
import struct, time


GPIO.setmode(GPIO.BOARD)

__author__ = 'Sergey'


class NixieClock(object):
    CHANNEL_HOUR_0 = 3
    CHANNEL_HOUR_1 = 5
    CHANNEL_MINUTE_0 = 7
    CHANNEL_MINUTE_1 = 11
    CHANNEL_SECOND_0 = 13
    CHANNEL_SECOND_1 = 15
    CHANNEL_SECONDS = [CHANNEL_SECOND_0, CHANNEL_SECOND_1]
    CHANNEL_HOURS = [CHANNEL_HOUR_0, CHANNEL_HOUR_1]
    CHANNEL_MINUTES = [CHANNEL_MINUTE_0, CHANNEL_MINUTE_1]

    channels_digits = [40, 38, 36, 32]  # 8 - 4 - 2 - 1
    TUBE_TYPE_SECONDS = "TUBE_TYPE_SECONDS"
    TUBE_TYPE_HOURS_MINUTES = "TUBE_TYPE_HOURS_MINUTES"

    def __init__(self):
        GPIO.setup(self.CHANNEL_HOURS + self.CHANNEL_MINUTES + self.CHANNEL_SECONDS, GPIO.OUT)
        GPIO.setup(self.channels_digits, GPIO.OUT)

    def _show(self, d_digit, tube_type):
        if d_digit > 9 or d_digit < 0:
            raise Exception("invalid passed parameter")

        digit_to_show = d_digit
        if tube_type == self.TUBE_TYPE_HOURS_MINUTES:
            convert_digit = {0:2, 1:1, 2:0, 3:9, 4:8, 5:7, 6:6, 7:5, 8:4, 9:3}
            digit_to_show = convert_digit[d_digit]

        b_array = [abs(int(i)) for i in '{0:0>4b}'.format(digit_to_show)]
        GPIO.output(self.channels_digits, b_array)

    def _convertToDigitArray(self, number):
        digits = []
        while True:
            d = number%10
            digits.append(d)
            number = (number - d)/10
            if number<=9:
                digits.append(number)
                break
        return list(reversed(digits))

    def _getNTPTime(self, host="pool.ntp.org"):
        port = 123
        buf = 1024
        address = (host, port)
        msg = '\x1b' + 47 * '\0'

        # reference time (in seconds since 1900-01-01 00:00:00)
        TIME1970 = 2208988800L  # 1970-01-01 00:00:00

        # connect to server
        client = socket.socket(AF_INET, SOCK_DGRAM)
        client.sendto(msg, address)
        msg, address = client.recvfrom(buf)

        t = struct.unpack("!12I", msg)[10]
        t -= TIME1970# - 3600 * 3
        return time.gmtime(t)


    def run(self):
        while True:
            struct_time = time.localtime() #(tm_year,tm_mon,tm_mday,tm_hour,tm_min, tm_sec,tm_wday,tm_yday,tm_isdst)
            hours = self._convertToDigitArray(struct_time[3])
            minutes = self._convertToDigitArray(struct_time[4])
            seconds = self._convertToDigitArray(struct_time[5])
            for channel, digit in zip(self.CHANNEL_HOURS + self.CHANNEL_MINUTES, hours + minutes):
                GPIO.output(channel, GPIO.HIGH)
                self._show(digit, self.TUBE_TYPE_HOURS_MINUTES)
                time.sleep(0.005)
                GPIO.output(channel, GPIO.LOW)

            for channel, digit in zip(self.CHANNEL_SECONDS, seconds):
                GPIO.output(channel, GPIO.HIGH)
                self._show(digit, self.TUBE_TYPE_SECONDS)
                time.sleep(0.002)
                GPIO.output(channel, GPIO.LOW)


nc = NixieClock()
nc.run()