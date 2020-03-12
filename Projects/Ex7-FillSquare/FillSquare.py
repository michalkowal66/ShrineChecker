import numpy as np
import random

def runFill():
    table = np.zeros((4,4))

    move_x = [1, 0, -1, 0]
    move_y = [0, -1, 0, 1]

    start_pos_x = 0
    start_pos_y = 0

    move = 1

    if fillSquare(move, table, start_pos_x, start_pos_y, move_x, move_y):
        print("Here's generated path")
        print(table)
    else:
        print("Error")

def checkMove(check_x, check_y, table):
    if (check_x < 0 or check_y < 0 or check_x > 3 or check_y > 3 or table[check_x][check_y] != 0.0):
        return False
    else:
        return True

def fillSquare(move, table, curr_x, curr_y, move_x, move_y):
    if move == 16:
        return True

    for u in range(4):
        new_x = curr_x + move_x[i]
        new_y = curr_y + move_y[i]
        if checkMove(new_x, new_y, table):
            table[new_x][new_y] = move
            print(table)
            if fillSquare(move + 1, table, new_x, new_y, move_x, move_y):
                return True

            table[new_x][new_y] = 0.0
            
    return False

runFill()