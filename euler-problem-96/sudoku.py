
import copy
from CellData import CellData

__author__ = 'Sergey'


class Sudoku(object):
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
        for i in range(20):
            self.loner()
            if self.is_solved:
                return

            # hidden singleton.
            self.hidden_loner()
            if self.is_solved:
                return

    def hidden_loner(self):
        # row.
        while True:
            is_updated = False
            for i in range(9):
                result = self.find_hidden_longer(self.get_row_cells(i))
                if result is None:
                    continue
                for (value, place) in result:
                    # r (value, <cell place>)
                    self.solved[i][place].suggests = [value, ]
                    self.solved[i][place].mark_solved()
                is_updated = True

            # col
            for j in range(9):
                result = self.find_hidden_longer(self.get_col_cells(j))
                if result is None:
                    continue
                for (value, place) in result:
                    # r (value, <cell place>)
                    self.solved[place][j].suggests = [value, ]
                    self.solved[place][j].mark_solved()
                is_updated = True

            # sect
            for i in range(0, 9, 3):
                for j in range(0, 9, 3):
                    result = self.find_hidden_longer(self.get_sect_cells(i, j))
                    # mark hidden longer
                    if result is None:
                        continue
                    for (value, place) in result:
                        # r (value, <cell place>)
                        (x, y) = self.get_cell_position_in_sect(i, j, place)
                        self.solved[x][y].suggests = [value, ]
                        self.solved[x][y].mark_solved()
                    is_updated = True

            if not is_updated:
                break



    def get_cell_position_in_sect(self, i_delta, j_delta, cell_place):
        """
        cell_place:             0,1,2
        0,1,2,3,4,5,6,7,8  -->> 3,4,5 -->>
                                6,7,8
        :param i_delta:
        :param j_delta:
        :param cell_place:
        :return:
        """
        i_result = 0
        j_result = 0
        if 0 <= cell_place < 3:
            # i = 0, j = [0,1,2]
            i_result = 0 + i_delta
            j_result = cell_place + j_delta
        elif 3 <= cell_place < 6:
            # i=1, j = [0,1,2]
            i_result = 1 + i_delta
            j_result = cell_place + j_delta - 3
        elif 6 <= cell_place <=8:
            # i=2 j = [0,1,2]
            i_result = 2 + i_delta
            j_result = cell_place + j_delta - 6

        return (i_result, j_result)

    def find_hidden_longer(self, cells):
        _cells = copy.deepcopy(cells)
        expected_hidden_value = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        remaining_list = list(set(expected_hidden_value) - set([cell.value for cell in _cells if cell.is_solved]))
        suggested_lists = [cell.suggests for cell in _cells if not cell.is_solved]
        # remove from suggested lists already found.
        solved_cells_value = [cell.value for cell in cells if cell.is_solved]
        for s_list in suggested_lists:
            for value in solved_cells_value:
                if value in s_list:
                    s_list.remove(value)

        for remain_digit in remaining_list:
            digits_count = len([1 for l in suggested_lists if remain_digit in l])
            # need to remove from suggested_lists not  satisfying digit
            if digits_count > 1:
                [s_list.remove(remain_digit) for s_list in suggested_lists if remain_digit in s_list]

        found_hidden_longer_list = [s[0] for s in suggested_lists if len(s) == 1]
        # We DIDN'T fIND hidden longer in given cells.
        if len([1 for s in suggested_lists if len(s) == 1]) == 0:
            return None

        result = []
        for hidden_longer in found_hidden_longer_list:
            for i in range(9):
                if hidden_longer in cells[i].suggests:
                    result.append((hidden_longer, i))
        return result

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

        self.solved[i][j].suggests = list(set(self.solved[i][j].suggests) - set([cell.value for cell in self.get_row_cells(i) if cell.is_solved]))
        self.solved[i][j].suggests = list(set(self.solved[i][j].suggests) - set([cell.value for cell in self.get_col_cells(j) if cell.is_solved]))
        self.solved[i][j].suggests = list(set(self.solved[i][j].suggests) - set([cell.value for cell in self.get_sect_cells(i, j) if cell.is_solved]))
        return self.solved[i][j].mark_solved()

    def get_row_cells(self, i):
        cell_list = []
        for j in range(9):
            cell_list.append(self.solved[i][j])
        return cell_list

    def get_col_cells(self, j):
        cell_list = []
        for i in range(9):
            cell_list.append(self.solved[i][j])
        return cell_list

    def get_sect_cells(self, i, j):
        sect_list = []
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
                    sect_list.append(self.solved[i][j])
        return sect_list

    def draw_sudoku(self):
        for i in range(9):
            for j in range(9):
                print "|" + str(self.solved[i][j].value),
            print ""

    def draw(self):
        for i in range(9):
            print self.solved[i]
