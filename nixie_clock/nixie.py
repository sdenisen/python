import unittest

__author__ = 'Sergey'


def convertToBinaryArray(digit):
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
        for i in range(9):
            self.assertListEqual(expected_dict[i], convertToBinaryArray(i), msg_str%str(i))


if __name__ == "__main__":
    unittest.main()