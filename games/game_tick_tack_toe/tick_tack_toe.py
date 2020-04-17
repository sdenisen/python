def isDefinedWinner(array):
    # TODO: need to check for winner.
    return False


def checkCorrectInput(cell_input_index, cell_array):
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

    if cell_array[cell_input_index] != "-":
        return False
    return True


def drawToOutput(array_field):
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


def cell_input(player_name, cell_array):
    """
    receive input from player and check it.
    :param player_name: player name.
    :param cell_array:
    :return: correct value that player typed.
    """
    while True:
        cell_id = input(f"{player_name}, please type number of cell: ")
        if checkCorrectInput(cell_id, cell_array):
            break
        print("incorrect input, please try again")

    return int(cell_id)


if __name__ == "__main__":
    print("you start new game, please input numner from [1--9]")
    print("player1 - X; player2 - O;")
    is_defined_winner = False
    array_field = ["-" for i in range(9)]
    drawToOutput(array_field)
    while not is_defined_winner:
        cell_index = cell_input("Player-1", array_field)
        array_field[cell_index] = "X"

        drawToOutput(array_field)
        if isDefinedWinner(array_field):
            print("You are winner!")
            break

        cell_index = cell_input("Player-2", array_field)
        array_field[cell_index] = "O"
        drawToOutput(array_field)
        if isDefinedWinner(array_field):
            print("You are winner!")
            break
