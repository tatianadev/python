from game_krestiki_noliki import game_functions, file_functions
import sys

field = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

players = [["Player 1", "X"], ["Player 2", "0"]]

print("Welcome to game krestiki-noliki!")

# load saved data from file
saved_data = file_functions.load_from_file()
if len(saved_data) > 0:
    field = saved_data

# remove saved file
file_functions.remove_file()

# find user, who should choose cell now
n, counter = game_functions.check_turn(field)  # n is id of user; counter shows, how many steps were already done
user = players[n][0]
symbol = players[n][1]

for i in range(counter, 9):
    while True:
        try:
            row_val = input("%s, please input value for row, where %s should be set!" % (user, symbol))
            col_val = input("%s, please input value for column, where %s should be set!" % (user, symbol))
            if not game_functions.check_range(row_val, col_val):
                print("Please enter correct value for row and column: from 1 - till 3!")
                continue
            if not game_functions.make_turn(field, int(row_val), int(col_val), symbol):
                continue
            else:
                game_functions.print_field(field)
            if not game_functions.check_field(field, symbol):
                if n == 0:
                    n = 1
                else:
                    n = 0
                user = players[n][0]
                symbol = players[n][1]
            else:
                print("%s, You are the winner!" % user)
                sys.exit()
            break

        except EOFError:  # Ctrl+D
            if not file_functions.dump_to_file(field):
                print("Game is not saved!")
            else:
                print("Game is saved! Try again!")
            sys.exit()
        except Exception:
            print("Something went wrong.")
            sys.exit()

else:
    print("No one is a winner!")
