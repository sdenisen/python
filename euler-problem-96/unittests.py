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

    def testSolveMethod(self):
        print "before"
        self.s.draw_sudoku()
        self.s.solve()
        print "after"
        self.s.draw_sudoku()

    def testColContent(self):
        result = self.s.col_content(0)
        self.assertListEqual(result, [9, 7, 8], "wrong expected list.")

    def testRowContent(self):
        result = self.s.row_content(0)
        self.assertListEqual(result, [3, 2, 6], "wrong expected list.")

    def testSectContent(self):
        result = self.s.sect_content(2, 2)
        self.assertListEqual(result, [3,9,1], "wrong expected list.")

        result = self.s.sect_content(2, 5)
        self.assertListEqual(result, [2, 3, 5, 8, 6], "wrong expected list.")

        result = self.s.sect_content(2, 8)
        self.assertListEqual(result, [6, 1, 4], "wrong expected list.")

        result = self.s.sect_content(5, 2)
        self.assertListEqual(result, [8, 7, 6], "wrong expected list, actual:%s" % result)

        result = self.s.sect_content(5, 5)
        self.assertListEqual(result, [1, 2, 7, 8], "wrong expected list, actual:%s" % result)

        result = self.s.sect_content(5, 8)
        self.assertListEqual(result, [9, 8, 2], "wrong expected list, actual:%s" % result)

        result = self.s.sect_content(8, 2)
        self.assertListEqual(result, [2, 8, 5], "wrong expected list, actual:%s" % result)

        result = self.s.sect_content(8, 5)
        self.assertListEqual(result, [6, 9, 2, 3, 1], "wrong expected list, actual:%s" % result)

        result = self.s.sect_content(8, 8)
        self.assertListEqual(result, [5, 9, 3], "wrong expected list, actual:%s" % result)