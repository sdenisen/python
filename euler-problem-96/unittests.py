from Sudoku import Sudoku
import unittest
from CellData import CellData

__author__ = 'Sergey'


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

    def testHiddenLongerInRow_1(self):
        # 2 IS HIDDEN LONGER
        c1 = CellData(1)
        c2 = CellData(4)
        c3 = CellData(0)#
        c3.suggests = [3, 5, 8]
        c4 = CellData(6)
        c5 = CellData(7)
        c6 = CellData(0)#
        c6.suggests = [5, ]
        c7 = CellData(0)#
        c7.suggests = [2, 3, 8]
        c8 = CellData(9)
        c9 = CellData(0)#
        c9.suggests = [3, 8]
        cells = [c1, c2, c3, c4, c5, c6, c7, c8, c9]
        result = self.s.find_hidden_longer(cells)
        for cell in cells:
            print cell.suggests
        print result

    def testHiddenLongerInRow_2(self):
        # 4 IS HIDDEN LONGER
        c1 = CellData(0)
        c1.suggests = [7, ]
        c2 = CellData(0)
        c2.suggests = [3, 5]
        c3 = CellData(1)
        c4 = CellData(9)
        c5 = CellData(0)
        c5.suggests = [4, 5, 6]
        c6 = CellData(0)
        c6.suggests = [5, 6]
        c7 = CellData(2)
        c8 = CellData(8)
        c9 = CellData(0)
        c9.suggests = [3, 5, 7]
        cells = [c1, c2, c3, c4, c5, c6, c7, c8, c9]
        result = self.s.find_hidden_longer(cells)
        print result


    def testHiddenLongerInRow_3_Two_hidden_longer(self):
        # 4 IS HIDDEN LONGER
        c1 = CellData(0)
        c1.suggests = [7, 2]
        c2 = CellData(0)
        c2.suggests = [3, 5]
        c3 = CellData(1)
        c4 = CellData(9)
        c5 = CellData(0)
        c5.suggests = [4, 5, 6]
        c6 = CellData(0)
        c6.suggests = [5, 6]
        c7 = CellData(2)
        c8 = CellData(8)
        c9 = CellData(0)
        c9.suggests = [3, 5, 7]
        cells = [c1, c2, c3, c4, c5, c6, c7, c8, c9]
        result = self.s.find_hidden_longer(cells)
        print result

    def testHiddenLongerInRow_2_NOT_FOUND(self):
        c1 = CellData(0)
        c1.suggests = [7, 4]  # 4 TEST VALUE
        c2 = CellData(0)
        c2.suggests = [3, 5]
        c3 = CellData(1)
        c4 = CellData(9)
        c5 = CellData(0)
        c5.suggests = [4, 5, 6]
        c6 = CellData(0)
        c6.suggests = [5, 6]
        c7 = CellData(2)
        c8 = CellData(8)
        c9 = CellData(0)
        c9.suggests = [3, 5, 7]
        cells = [c1, c2, c3, c4, c5, c6, c7, c8, c9]
        result = self.s.find_hidden_longer(cells)
        print result

    def testSolveMethod(self):
        print "before"
        self.s.draw_sudoku()
        self.s.solve()
        print "after"
        self.s.draw_sudoku()