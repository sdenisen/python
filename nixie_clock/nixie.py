__author__ = 'Sergey'


def convertToBinaryArray(digit):
        """
            The method converts digit to binary array of digits  GPIO.LOW/GPIO.HIGH
            param digit: params 0...9
            :return: list of [GPIO.LOW....GPIO.HIGH] that represent digit to binary
        """
        if digit > 9 or digit < 0:
            raise Exception("invalid passed parameter")
        return [abs(int(i)-1) for i in '{0:0>4b}'.format(digit)]