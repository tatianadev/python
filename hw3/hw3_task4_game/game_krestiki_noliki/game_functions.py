# print fields

def print_field(field):
    print('+---+---+---+---+')
    print('|   | 1 | 2 | 3 |')
    print('+---+---+---+---+')
    print('| 1 | %s |' % ' | '.join(field[0]))
    print('+---+---+---+---+')
    print('| 2 | %s |' % ' | '.join(field[1]))
    print('+---+---+---+---+')
    print('| 3 | %s |' % ' | '.join(field[2]))
    print('+---+---+---+---+')


# check, whose turn is now
def check_turn(field):
    count_x = 0
    count_zero = 0
    for i in field:
        for j in i:
            if j == 'X':
                count_x += 1
            elif j == '0':
                count_zero += 1

    if count_x <= count_zero:
        n = 0  # id of first user, who sets X values
    else:
        n = 1  # id of second user, who sets 0 values
    return n, count_x + count_zero


# check input values or row and column of user
def check_range(x, y):
    try:
        x = int(x)
        y = int(y)
        if 1 <= x <= 3 and 1 <= y <= 3:
            return True
        else:
            return False
    except:
        return False


# check, if corresponding cell is available
def make_turn(field, row_val, col_val, val):
    if field[row_val - 1][col_val - 1] != ' ':
        return False
    else:
        field[row_val - 1][col_val - 1] = val
        return True


def check_field(field, symbol):
    if check_row(field, symbol):
        return True
    elif check_cols(field, symbol):
        return True
    else:
        return check_diagonals(field, symbol)


def check_row(field, symbol):
    result = False
    for i in range(len(field)):
        for j in range(len(field[i])):
            if not result:
                if field[i][j] != symbol:
                    break
                else:
                    if j == 2:
                        result = True
                        print("Row is filled with %s!" % symbol)
            else:
                break
    return result


def check_cols(field, symbol):
    result = False
    for i in range(len(field)):
        for j in range(len(field[i])):
            if not result:
                if field[j][i] != symbol:
                    break
                else:
                    if j == 2:
                        result = True
                        print("Column is filled with %s!" % symbol)
            else:
                break

    return result


def check_diagonals(field, symbol):
    result = False

    # check first diagonal
    for i in range(3):
        if field[i][i] != symbol:
            break
        else:
            if i == 2:
                result = True
                print("Diagonal is filled with %s!" % symbol)
                break

    if not result:
        # check second diagonal
        k = 2
        for i in range(3):
            if field[k][i] != symbol:
                break
            else:
                k -= 1
                if i == 2:
                    result = True
                    print("Diagonal is filled with %s!" % symbol)

    return result
