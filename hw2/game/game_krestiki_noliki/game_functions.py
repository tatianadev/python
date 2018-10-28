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


# check input values or row and column of user
def check_range(x, y):
    avail_values = (1, 2, 3)
    try:
        x = int(x)
        y = int(y)
        if x in avail_values and y in avail_values:
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
