from sudoku import Sudoku
import unittest
from CellData import CellData

__author__ = 'Sergey'


class Test(unittest.TestCase):

    def setUp(self):
        str_sudoku = """200080300
                        060070084
                        030500209
                        000105408
                        000000000
                        402706000
                        301007040
                        720040060
                        004010003"""

        int_sudoku = []
        for line in str_sudoku.split("\n"):
            int_sudoku.append([int(i) for i in list(line.strip())])
        self.s = Sudoku(int_sudoku)

    def testUseHiddenLongerMethod(self):
        self.s.draw_sudoku()
        print ""
        self.s.loner()
        self.s.draw_sudoku()
        print ""
        self.s.hidden_loner()
        self.s.draw_sudoku()
        print ""
        self.s.loner()
        self.s.draw_sudoku()











