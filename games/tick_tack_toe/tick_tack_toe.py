def isDefinedWinner(array):
    # TODO: need to check for winner.
    return False


def checkCorrectInput(cell_index):
    # TODO: check that it's a digit,
    # TODO: check correct input,
    # TODO: check that array with cell index is empty.
    cell_index = int(cell_index)
    return 0 < cell_index or cell_index <= 9


def drawToOutput(array_field):
    for i in range(9):
        if i != 0 and i % 3 == 0:
            print(" - 0, 1, 2 ")
        print(array_field[i], end=" ")
    print(" - 0, 1, 2 ")


def cell_input(player_name):
    cell_id = input(f"{player_name}, please type number of cell: ")
    while not checkCorrectInput(cell_id):
        print("incorrect input, please try use cell id number from 1 to 9")
        cell_id = input(f"{player_name}, please type number of cell: ")

        if not checkCorrectInput(cell_id):
            print("incorrect input, please try use cell id number from 1 to 9")
            continue


if __name__ == "__main__":
    print("you start new game, please input numner from [1--9]")
    print("player1 - X; player2 - O;")
    is_defined_winner = False
    array_field = ["-" for i in range(9)]
    drawToOutput(array_field)
    while not is_defined_winner:
        cell_id = input("player1, please type number of cell: ")
        if not checkCorrectInput(cell_id):
            print("incorrect input, please try use cell id number from 1 to 9")
            continue
        cell_id = int(cell_id)
        array_field[cell_id] = "X"
        drawToOutput(array_field)
        if isDefinedWinner(array_field):
            print("You are winner!")
            break

        cell_id = input("player2, please type number of cell: ")
        if not checkCorrectInput(cell_id):
            print("Incorrect input, please use number between 1 and 9")
            continue
        cell_id = int(cell_id)
        array_field[cell_id] = "O"
        drawToOutput(array_field)
