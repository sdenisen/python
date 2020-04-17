EMPTY_CELL = "-"


def isDefinedWinner(array):
    # TODO: need to check for winner.
    return False


def checkCorrectInput(cell_input_index, cells_array):
    """
    Check that cell_index is satisfied of criteria: digit / cell of array is not filled / and index between 0 and 9.
    :param cell_input_index: index cell that have to be verified (typed from player).
    :param array_field:
    :return: True/False
    """
    if not cell_input_index.isdigit():
        return False

    cell_input_index = int(cell_input_index)
    if cell_input_index < 0 or cell_input_index >= 9:
        return False

    if cells_array[cell_input_index] != EMPTY_CELL:
        return False
    return True


def draw(array_field):
    """
    Print tick tack toe field.
    :param array_field: array of field.
    :return:  None
    """
    _help = "| "
    for i in range(9):
        _help = _help + f"{i}, "
        print(array_field[i], end=" ")
        if i % 3 == 2:
            print(_help)
            _help = "| "


def cell_input(player_name, cells_array):
    """
    Receive input from player and check it.
    :param player_name: player name.
    :param cells_array:
    :return: correct value that player typed.
    """
    while True:
        cell_id = input(f"{player_name}, please type number of cell: ")
        if checkCorrectInput(cell_id, cells_array):
            break
        print("incorrect input, please try again")

    return int(cell_id)


def playerStep(player_name, cells_array, cell_name):
    """

    :param player_name:
    :param cells_array:
    :param cell_name:
    :return:
    """
    _index = cell_input(player_name, cells_array)
    cells_array[_index] = cell_name
    draw(cells_array)
    if isDefinedWinner(cells_array):
        print(f"{player_name}, you are winner!")
        return True
    return False


if __name__ == "__main__":
    print("You start new game, please input number from [1--9]")
    print("Player-1 - 'X'; Player-2 - 'O';")
    playing_field = [EMPTY_CELL for i in range(9)]
    draw(playing_field)
    while True:
        is_win = playerStep("Player-1", playing_field, "X")
        if is_win:
            break

        is_win = playerStep("Player-2", playing_field, "O")
        if is_win:
            break
