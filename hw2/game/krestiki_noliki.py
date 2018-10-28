import game_functions

field = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

players = [["Player 1", "X"], ["Player 2", "0"]]

n = 0
user = players[n][0]
symbol = players[n][1]

print("Welcome to game krestiki-noliki!")

while True:
    continue_check = True
    try:
        row_val = input("%s, please input value for row, where %s should be set!" % (user, symbol))
        col_val = input("%s, please input value for column, where %s should be set!" % (user, symbol))
        if not game_functions.check_range(row_val, col_val):
            print("Please enter correct value for row and column: from 1 - till 3!")
            continue_check = False

        if continue_check:
            if game_functions.make_turn(field, int(row_val), int(col_val), symbol):
                game_functions.print_field(field)
            else:
                print("This cell is not empty. Please choose other cell!")
                continue_check = False

        if continue_check:
            if not game_functions.check_field(field, symbol):
                if n == 0:
                    n = 1
                else:
                    n = 0
                user = players[n][0]
                symbol = players[n][1]
            else:
                print("%s, You are the winner!" % user)
                break

    except Exception:
        print("Something went wrong.")
        break
