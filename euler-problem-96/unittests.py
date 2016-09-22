__author__ = 'Sergey'

from sudoku_solver import Sudoku
import unittest


class Test(unittest.TestCase):

    def setUp(self):
        str_sudoku = """003020600
                        900305001
                        001806400
                        008102900
                        700000008
                        006708200
                        002609500
                        800203009
                        005010300"""

        int_sudoku = []
        for line in str_sudoku.split("\n"):
            int_sudoku.append([int(i) for i in list(line.strip())])
        self.s = Sudoku(int_sudoku)

    def testColContent(self):
        result = self.s.colContent(0)
        self.assertListEqual(result, [9, 7, 8], "wrong expected list.")

    def testRowContent(self):
        result = self.s.rowContent(0)
        self.assertListEqual(result, [3, 2, 6], "wrong expected list.")

    def testSectContent(self):
        result = self.s.sectContent(0, 3)
        self.assertListEqual(result, [], "wrong expected list.")


if __name__ == "__main__":
    unittest.main()