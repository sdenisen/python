import unittest

from sudoku import Sudoku


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

    def testGetRowCells(self):
        print "-------------"
        for i in range(9):
            result = self.s.get_row_cells(i)
            for cell in result:
                print cell.value,
            print ""

    def testGetColCells(self):
        print "-------------"
        for j in range(9):
            result = self.s.get_col_cells(j)
            for cell in result:
                print cell.value,
            print ""

    def testGetColCells(self):
        print "-------------"
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                result = self.s.get_sect_cells(i, j)
                for cell in result:
                    print cell.value,
                print ""

    def testGetCellPositionInSect(self):
        print "-------------"
        print "testGetCellPositionInSect"
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                for cell_place in range(9):
                    print "i, j, cell_place --> result: %s, %s, %s, %s" % (i, j, cell_place, self.s.get_cell_position_in_sect(i, j, cell_place))
        print "-------------"
