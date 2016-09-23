__author__ = 'sdenisenko'
'''
https://projecteuler.net/problem=96
Problem 96
Su Doku (Japanese meaning number place) is the name given to a popular puzzle concept.
Its origin is unclear, but credit must be attributed to Leonhard Euler who invented a similar,
and much more difficult, puzzle idea called Latin Squares. The objective of Su Doku puzzles, however,
is to replace the blanks (or zeros) in a 9 by 9 grid in such that each row, column, and 3 by 3 box contains each of
 the digits 1 to 9. Below is an example of a typical starting puzzle grid and its solution grid.

A well constructed Su Doku puzzle has a unique solution and can be solved by logic, although it may be necessary to employ
"guess and test" methods in order to eliminate options (there is much contested opinion over this). The complexity of the
search determines the difficulty of the puzzle; the example above is considered easy because it can be solved by straight
forward direct deduction.

The 6K text file, sudoku.txt (right click and 'Save Link/Target As...'), contains fifty different Su Doku puzzles ranging in
difficulty, but all with unique solutions (the first puzzle in the file is the example above).

By solving all fifty puzzles find the sum of the 3-digit numbers found in the top left corner of each solution grid; for example,
 483 is the 3-digit number found in the top left corner of the solution grid above.
'''
import re

IN = "IN"
UNKNOWN = "UNKNOWN"
SOLVED = "SOLVED"


class SudokuSolver:
    def __init__(self, file_name):
        self.sudoku_list = []
        int_sudoku  = []
        with open(file_name, "r") as f:
            for line in f.readlines():
                if not re.match("Grid", line):
                    int_sudoku.append([int(i) for i in list(line.strip("\n"))])
                    continue
                if int_sudoku:
                    self.sudoku_list.append(Sudoku(int_sudoku))
                int_sudoku = []


class Sudoku:
    def __init__(self, int_input_array):
        self.suggest = [1,2,3,4,5,6,7,8,9]
        self.solved = [[0 for i in range(0,9)] for i in range(0,9)]
        for i in range(9):
            for j in range(9):
                if int_input_array[i][j]:
                    self.solved[i][j] = [int_input_array[i][j], IN, []]
                else:
                    self.solved[i][j] = [0, UNKNOWN, self.suggest]

    def solve(self):
        while True:
            is_updated = False
            for i in range(9):
                for j in range(9):
                    if UNKNOWN !=  self.solved[i][j][1]:
                        continue
                    is_updated = is_updated or self.updateSuggests(i, j)

            if is_updated == False:
                break


    def markSolved(self, i, j, solve_value):
        self.solved[i][j][0] = solve_value
        self.solved[i][j][1] = SOLVED

    def updateSuggests(self, i, j):
        self.solved[i][j][2] = list(set(self.solved[i][j][2]) - set(self.rowContent(i)))
        self.solved[i][j][2] = list(set(self.solved[i][j][2]) - set(self.colContent(j)))
        self.solved[i][j][2] = list(set(self.solved[i][j][2]) - set(self.sectContent(i, j)))
        if len(self.solved[i][j][2]) == 1:
            self.markSolved(i, j, self.solved[i][j][2][0])
            return True
        return False


    def rowContent(self, i):
        result = []
        for j in range(9):
            if UNKNOWN != self.solved[i][j][1]:
                result.append(self.solved[i][j][0])
        return result

    def colContent(self, j):
        result = []
        for i in range(9):
            if UNKNOWN != self.solved[i][j][1]:
                result.append(self.solved[i][j][0])
        return result

    def sectContent(self, i, j):
        result = []
        i_corner = 0
        j_corner = 0

        if 0 < i <=2:
            i_corner = 0
        elif 2 < i <=5:
            i_corner = 3
        elif 5 < i <=8:
            i_corner = 6

        if 0 < j <=2:
            j_corner = 0
        elif 2 < j <=5:
            j_corner = 3
        elif 5 < j <=8:
            j_corner = 6

        for i in range(i_corner, i_corner+3):
            for j in range(j_corner, j_corner+3):
                if UNKNOWN != self.solved[i][j][1]:
                    result.append(self.solved[i][j][0])
        return result

    def arrayDiff(self, param, param1):
        pass



    def draw_sudoku(self):
        for i in range(9):
            for j in range(9):
                print "|" + str(self.solved[i][j][0]),
            print ""


    def draw(self):
        for i in range(9):
            print self.solved[i]


file_path="p096_sudoku.txt"
s = SudokuSolver(file_path)

s.sudoku_list[0]
s.sudoku_list[0].draw()
print s.sudoku_list[0].solved[1][3][2]
