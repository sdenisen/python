import unittest
from task13.task13_resolve import converToFloat, getMinimumDeltaOfSignal


class UnitTests(unittest.TestCase):
    def test_convert_1(self):
        str_float = "0.000003 0.000012 0.000081 0.000099 0.000076 0.000045 0.000092 0.000068 0.000047 "
        expected_values = [3e-06, 1.2e-05, 8.1e-05, 9.9e-05, 7.6e-05, 4.5e-05, 9.2e-05, 6.8e-05, 4.7e-05]
        res = converToFloat(str_float)
        self.assertEqual(res, expected_values)

    def test_convert_2_negative(self):
        str_float = "0.000002 0.000045 -0.000063 -0.000009 -0.000050 0.000048 0.000070 -0.000037 0.000056 -0.000008 "
        expected_values = [2e-06, 4.5e-05, -6.3e-05, -9e-06, -5e-05, 4.8e-05, 7e-05, -3.7e-05, 5.6e-05, -8e-06]
        res = converToFloat(str_float)
        self.assertEqual(res, expected_values)

    def test_delta_1(self):
        metabl = [1.000002, 0.000002]
        adduct = [0.500000, -0.500000]
        res = getMinimumDeltaOfSignal(metabl, adduct, 0.500001)
        expected_values = (1, 2)
        self.assertEqual(expected_values, res)

    def test_delta_2(self):
        metabl = [1.000002, 0.000002]
        adduct = [0.500000, -0.500000]
        res = getMinimumDeltaOfSignal(metabl, adduct, 0.000001)
        expected_values = (1, 2)
        self.assertEqual(expected_values, res)

    def test_delta_3(self):
        metabl = [1.000002, 0.000001]
        adduct = [0.500000, -0.500000]
        res = getMinimumDeltaOfSignal(metabl, adduct, 0.500001)
        expected_values = (2, 1)
        self.assertEqual(expected_values, res)

    def test_delta_4(self):
        metabl = [0.000001, 0.000002, 0.000003, 0.000004, 0.000005]
        adduct = [0.000002, 0.000010, 0.000001, -0.000001]
        res = getMinimumDeltaOfSignal(metabl, adduct, 0.000003)
        expected_values = (1, 1)
        self.assertEqual(expected_values, res)

    def test_delta_5(self):
        metabl = [0.000001, 0.000002, 0.000003, 0.000004, 0.000005]
        adduct = [0.000002, 0.000010, 0.000001, -0.000001]
        res = getMinimumDeltaOfSignal(metabl, adduct, 0.000010)
        expected_values = (1, 2)
        self.assertEqual(expected_values, res)

    def test_delta_6(self):
        metabl = [0.000001, 0.000002, 0.000003, 0.000004, 0.000005]
        adduct = [0.000002, 0.000010, 0.000001, -0.000001]
        res = getMinimumDeltaOfSignal(metabl, adduct, 0.000020)
        expected_values = (5, 2)
        self.assertEqual(expected_values, res)

    def test_delta_7(self):
        metabl = [0.000001, 0.000002, 0.000003, 0.000004, 0.000005]
        adduct = [0.000002, 0.000010, 0.000001, -0.000001]
        res = getMinimumDeltaOfSignal(metabl, adduct, 0.000005)
        expected_values = (3, 1)
        self.assertEqual(expected_values, res)

    def test_delta_8(self):
        metabl = [0.000001, 0.000002, 0.000003, 0.000004, 0.000005]
        adduct = [0.000002, 0.000010, 0.000001, -0.000001]
        res = getMinimumDeltaOfSignal(metabl, adduct, 0.000100)
        expected_values = (5, 2)
        self.assertEqual(expected_values, res)


    def test_delta_9(self):
        metabl = [0.000001, 0.000002, 0.000003, 0.000004, 0.000005]
        adduct = [0.000002, 0.000010, 0.000001, -0.000001]
        res = getMinimumDeltaOfSignal(metabl, adduct, 0.000002)
        expected_values = (1, 3)
        self.assertEqual(expected_values, res)


if __name__ == '__main__':
    unittest.main()
