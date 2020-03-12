import numpy as np

def solveKT():
    gameboard = np.zeros((8,8))

    move = 1

    move_x = [1, 2, 2, 1, -1, -2, -2, -1]
    move_y = [2, 1, -1, -2, -2, -1, 1, 2]

    start_x = 0
    start_y = 0

    gameboard[start_x][start_y] = 0

    if KTPsolver(move, start_x, start_y, move_x, move_y, gameboard):
        print(gameboard)
    else:
        print("Error")
    

def isSafe(x, y, board):
    if (x < 0 or x > 7 or y < 0 or y > 7 or board[x][y] != 0.0):
        return False
    else:
        return True

def KTPsolver(move, curr_x, curr_y, move_x, move_y, gameboard):
    if move == 64:
        return True

    for i in range(8):
        new_x = curr_x + move_x[i]
        new_y = curr_y + move_y[i]
        if isSafe(new_x, new_y, gameboard):
            gameboard[new_x][new_y] = move
            print(gameboard)
            if KTPsolver(move + 1, new_x, new_y, move_x, move_y, gameboard):
                return True

            gameboard[new_x][new_y] = 0.0
            
    return False

solveKT()
