import unittest

from task10.task10_resolve import revers_words


class TestCases(unittest.TestCase):
    def test_1_unit_test(self):
        t = "QUICK FOX JUMPS"
        r = revers_words(t)
        self.assertEqual(r, "KCIUQ XOF SPMUJ")

    def test_2_unit_test(self):
        t = "  QUICK FOX   JUMPS "
        r = revers_words(t)
        self.assertEqual(r, "  KCIUQ XOF   SPMUJ ")

    def test_3_unit_test(self):
        r = revers_words("")
        self.assertEqual(r, "")

    def test_4_unit_test(self):
        r = revers_words("   ")
        self.assertEqual(r, "   ")

    def test_5_unit_test(self):
        with self.assertRaises(Exception):
            revers_words(",")

    def test_6_unit_test(self):
        with self.assertRaises(Exception):
            revers_words("test")

    def test_7_unit_test(self):
        with self.assertRaises(Exception):
            revers_words("123")

def main():
    t = TestCases()
    t.run()


if __name__=='__main__':
    main()

