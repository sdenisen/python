__author__ = 'Sergey'


IN = "IN"
UNKNOWN = "UNKNOWN"
SOLVED = "SOLVED"


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

    @property
    def is_solved(self):
        pass

    @is_solved.getter
    def is_solved(self):
        for i in range(9):
            for j in range(9):
                if self.solved[i][j][1] == UNKNOWN:
                    return False
        return True

    def solve(self):
        # singleton.
        self.loner()

        if self.is_solved:
            return

        # hidden singleton.
        self.hiddenLoner()

    def hiddenLoner(self):
        # try to find single loner in row
        for i in range(9):
            hidden_value = [1,2,3,4,5,6,7,8,9]
            row = self.solved[i]
            cell_index = 0
            for cell in row:
                # find unique value in cell.
                if cell[1] == IN or cell[1] == SOLVED:
                    hidden_value.remove(cell[0])

                suggest_value = cell[2]
                # neeed to check whether some of the values meet to other cells in row.
                for cell_2 in row:
                    for v in cell_2[2]:
                        if v in suggest_value:
                            suggest_value.remove(v)

                if len(suggest_value) == 1:
                    # we found hidden loner
                    self.solved[i][cell_index][0] = suggest_value[0]
                    self.solved[i][cell_index][1] = SOLVED
                cell_index += 1


    def loner(self):
        while True:
            is_updated = False
            for i in range(9):
                for j in range(9):
                    if UNKNOWN != self.solved[i][j][1]:
                        continue
                    is_updated = is_updated or self.updateSuggests(i, j)

            if not is_updated:
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

