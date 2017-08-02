import unittest

from sudoku import Sudoku
from CellData import CellData


__author__ = 'Sergey'


class Test(unittest.TestCase):

    def setUp(self):
        str_sudoku = """043980250
                        600425000
                        200001094
                        900004070
                        300608000
                        410209003
                        820500000
                        000000005
                        534890710"""



        int_sudoku = []
        for line in str_sudoku.split("\n"):
            int_sudoku.append([int(i) for i in list(line.strip())])
        self.s = Sudoku(int_sudoku)

    def testFindOpenPairs(self):
        # 2 IS HIDDEN LONGER
        c1 = CellData(0) #
        c1.suggests = [2, 3, 5, 7]
        c2 = CellData(9)
        c3 = CellData(4)
        c4 = CellData(0)
        c4.suggests = [1, 2, 5]
        c5 = CellData(0)
        c5.suggests = [1, 5]
        c6 = CellData(8)
        c7 = CellData(6)
        c8 = CellData(0)
        c8.suggests = [1, 3, 5, 7]
        c9 = CellData(0)
        c9.suggests = [1, 5]
        cells = [c1, c2, c3, c4, c5, c6, c7, c8, c9]
        pair, positions = self.s.find_open_pairs(cells)
        print pair
        print positions
