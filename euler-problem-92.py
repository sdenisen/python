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

result = 8581146
{1: [1, 1], 4: [2, 4, 16, 37, 58, 89, 145, 42, 20, 4]}
{1: 1418854, 4: 8581146}
0

'''

import unittest

chain_number_dict = {}

def split_number_to_digits(number):
    result = []
    while number != 0:
        digit = number%10
        result.append(digit)
        number = (number-digit)/10
    return list(reversed(result))


def set_loop(loop):
    chain_number_dict[loop[-1]] = loop


def check_number_in_loop(number):
    for k, v in chain_number_dict.iteritems():
        if number in v:
            return k
    return -1


def is_endless_loop(result_array):
    digits = split_number_to_digits(result_array[-1])
    new_number = sum([i*i for i in digits])
    loop_value = check_number_in_loop(new_number)
    if loop_value != -1:
        return loop_value
    if new_number in result_array or len(result_array)>=10000:
        result_array.append(new_number)
        set_loop(result_array)
        return new_number

    result_array.append(new_number)
    return is_endless_loop(result_array)

count = 0
count_numbers = {}
for i in range(1, 10000001):
        result = is_endless_loop([i,])
        if result in count_numbers.keys():
            count_numbers[result] += 1
        else:
            count_numbers[result] = 1

        if result == 89:
            count += 1

print chain_number_dict
print count_numbers
print count


class UnitTests(unittest.TestCase):

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
