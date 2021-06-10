import unittest
from task9.task9_resolve import compress


class UnitTests(unittest.TestCase):
    def test_common(self):
        a = [1, 4, 5, 2, 3, 9, 8, 11, 0]
        r = "0-5,8-9,11"
        res = compress(a)
        self.assertEqual(r, res)

    def test_common_2(self):
        a = [1, 4, 3, 2]
        r = "1-4"
        res = compress(a)
        self.assertEqual(r, res)

    def test_common_3(self):
        a = [1, 4]
        r = "1,4"
        res = compress(a)
        self.assertEqual(r, res)

    def test_options_1(self):
        r = ""
        res = compress([])
        self.assertEqual(r, res)

    def test_options_2(self):
        r = "1-7"
        res = compress([1,2,3,4,5,6,7])
        self.assertEqual(r, res)

    def test_options_3(self):
        r = "1-3,5-7"
        res = compress([1,2,3,5,6,7])
        self.assertEqual(r, res)


if __name__ == '__main__':
    unittest.main()
