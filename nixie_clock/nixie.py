import unittest
from RPi import GPIO

__author__ = 'Sergey'


class NixieTube(object):
    TUBE_TYPE_SECONDS = "TUBE_TYPE_SECONDS"
    TUBE_TYPE_HOURS_MINUTES = "TUBE_TYPE_HOURS_MINUTES"

    def __init__(self, tube_type, channels_digits):
        self.tube_type = tube_type
        self.channels_digits = channels_digits

    def show(self, d_digit):
        digit_to_show = d_digit
        if self.tube_type == self.TUBE_TYPE_HOURS_MINUTES:
            convert_digit = {0:2, 1:1, 2:0, 3:9, 4:8, 5:7, 6:6, 7:5, 8:4, 9:3}
            digit_to_show = convert_digit[d_digit]
        b_array = self._convertToBinaryArray(digit_to_show)
        GPIO.output(self.channels_digits, b_array)

    def _convertToBinaryArray(self, digit):
        """
            The method converts digit to binary array of digits  GPIO.LOW/GPIO.HIGH
            param digit: params 0...9
            :return: list of [GPIO.LOW....GPIO.HIGH] that represent digit to binary
        """
        if digit > 9 or digit < 0:
            raise Exception("invalid passed parameter")
        return [abs(int(i)) for i in '{0:0>4b}'.format(digit)]


class Tests (unittest.TestCase):

    def test_convertToBinaryArray(self):
        #  0 - 0000; 4 - 0100; 8 - 1000
        #  1 - 0001; 5 - 0101; 9 - 1001
        #  2 - 0010; 6 - 0110
        #  3 - 0011; 7 - 0111
        msg_str = "wrong convertions of %s"
        expected_dict = [[0, 0, 0, 0], [0, 0, 0, 1],
                         [0, 0, 1, 0], [0, 0, 1, 1], [0, 1, 0, 0],
                         [0, 1, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1],
                         [1, 0, 0, 0], [1, 0, 0, 1]]
        nt = NixieTube(None, None)
        for i in range(9):
            self.assertListEqual(expected_dict[i], nt._convertToBinaryArray(i), msg_str%str(i))


if __name__ == "__main__":
    unittest.main()