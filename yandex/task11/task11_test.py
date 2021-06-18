import unittest

from task11.task11_resolve import findPattern


class TestCases(unittest.TestCase):

    def test_1_unit_test(self):
        string = "QUICKQUICKQUICK"
        pattern = "QUICK"

        r = findPattern(pattern, string)
        self.assertEqual("1 6 11", r)

    def test_2_unit_test(self):
        string = "EQEQEQEQEQEQEQ"
        pattern = "EQE"

        r = findPattern(pattern, string)
        self.assertEqual("1 3 5 7 9 11", r)


def main():
    t = TestCases()
    t.run()


if __name__=='__main__':
    main()

