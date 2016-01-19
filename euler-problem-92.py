import unittest

__author__ = 'Sergey'
'''
A number chain is created by continuously adding the square of the digits in a number to form a new number
until it has been seen before.

For example,

44 ? 32 ? 13 ? 10 ? 1 ? 1
85 ? 89 ? 145 ? 42 ? 20 ? 4 ? 16 ? 37 ? 58 ? 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop.
What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
'''

def split_number_to_digits(number):
    result = []
    while number != 0:
        digit = number%10
        result.append(digit)
        number = (number-digit)/10
    return list(reversed(result))



def is_endless_loop(result_array):
    digits = split_number_to_digits(result_array[-1])
    new_number = sum([i*i for i in digits])
    if new_number in result_array or len(result_array)>=100:
        result_array.append(new_number)
        return result_array
    result_array.append(new_number)
    return is_endless_loop(result_array)

count = 0
for i in range(2, 10000001):
        result = is_endless_loop([i,])
        if result[-1] == 89:
            count += 1

print count


class UnitTests(unittest.TestCase):
    def setUp(self):
        pass

    def test_endless_loop_2(self):
        result_array = [85, ]
        result = is_endless_loop(result_array)
        print result
        self.assertEqual(result[-1], 89)

    def test_endless_loop(self):
        result_array = [44, ]
        result = is_endless_loop(result_array)
        print result
        self.assertEqual(result[-1], 1)


    def test_split_function(self):
        number = 10
        array_result = split_number_to_digits(number)
        self.assertEqual(1, array_result[0])
        self.assertEqual(0, array_result[1])

        number = 123
        array_result = split_number_to_digits(number)
        self.assertEqual(1, array_result[0])
        self.assertEqual(2, array_result[1])
        self.assertEqual(3, array_result[2])
