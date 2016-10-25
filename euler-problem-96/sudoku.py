from CellData import CellData

__author__ = 'Sergey'


class Sudoku:
    def __init__(self, int_input_array):
        self.solved = [[0 for i in range(0, 9)] for i in range(0, 9)]
        for i in range(9):
            for j in range(9):
                self.solved[i][j] = CellData(int_input_array[i][j])

    @property
    def is_solved(self):
        for i in range(9):
            for j in range(9):
                if not self.solved[i][j].is_solved:
                    return False
        return True

    def solve(self):
        # singleton.
        self.loner()
        if self.is_solved:
            return

        # hidden singleton.
        self.hidden_loner()

    def hidden_loner(self):
        # try to find single loner in row
        for i in range(9):
            hidden_value = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            row = self.solved[i]
            cell_index = 0
            for cell in row:
                # find unique value in cell.
                if cell.state == CellData.IN or cell.state == CellData.SOLVED:
                    hidden_value.remove(cell.value)

                suggest_value = cell.suggests
                # neeed to check whether some of the values meet to other cells in row.
                for cell_2 in row:
                    for v in cell_2.suggests:
                        if v in suggest_value:
                            suggest_value.remove(v)

                if len(suggest_value) == 1:
                    # we found hidden loner
                    self.solved[i][cell_index].value = suggest_value[0]
                    self.solved[i][cell_index].state = CellData.SOLVED
                cell_index += 1

    def loner(self):
        while True:
            is_updated = False
            for i in range(9):
                for j in range(9):
                    if self.solved[i][j].is_solved:
                        continue
                    is_updated = is_updated or self.update_suggests(i, j)
            if not is_updated:
                break

    def update_suggests(self, i, j):
        self.solved[i][j].suggests = list(set(self.solved[i][j].suggests) - set(self.row_content(i)))
        self.solved[i][j].suggests = list(set(self.solved[i][j].suggests) - set(self.col_content(j)))
        self.solved[i][j].suggests = list(set(self.solved[i][j].suggests) - set(self.sect_content(i, j)))
        return self.solved[i][j].mark_solved()

    def row_content(self, i):
        result = []
        for j in range(9):
            if self.solved[i][j].is_solved:
                result.append(self.solved[i][j].value)
        return result

    def col_content(self, j):
        result = []
        for i in range(9):
            if self.solved[i][j].is_solved:
                result.append(self.solved[i][j].value)

        return result

    def sect_content(self, i, j):
        result = []
        i_corner = 0
        j_corner = 0

        if 0 < i <= 2:
            i_corner = 0
        elif 2 < i <= 5:
            i_corner = 3
        elif 5 < i <= 8:
            i_corner = 6

        if 0 < j <= 2:
            j_corner = 0
        elif 2 < j <= 5:
            j_corner = 3
        elif 5 < j <= 8:
            j_corner = 6

        for i in range(i_corner, i_corner+3):
            for j in range(j_corner, j_corner+3):
                if self.solved[i][j].is_solved:
                    result.append(self.solved[i][j].value)
        return result

    def draw_sudoku(self):
        for i in range(9):
            for j in range(9):
                print "|" + str(self.solved[i][j].value),
            print ""

    def draw(self):
        for i in range(9):
            print self.solved[i]
