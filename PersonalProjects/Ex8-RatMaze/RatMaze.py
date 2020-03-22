def findWay():
    init_x = 0
    init_y = 0

    move = "*"

    move_x = [1, 0, -1, 0]
    move_y = [0, -1, 0, 1]

    maze = [ [1, 1, 0, 0], 
             [0, 1, 0, 1], 
             [0, 1, 1, 1], 
             [1, 1, 0, 3] ] 
    print("Initial maze:",maze)

    if solveMaze(move, maze, init_x, init_y, move_x, move_y):
        print("Solved maze:",maze)
    else:
        print("Error")

def checkMove(check_x, check_y, maze):
    if check_x == 3 and check_y == 3:
        return True
    elif (check_x not in range(4) or check_y not in range(4) or maze[check_x][check_y] != 1):
        return False
    else:
        return True    
       
def solveMaze(move, maze, curr_x, curr_y, move_x, move_y):
    if curr_x == 3 and curr_y == 3:
        maze[curr_x][curr_y] = "x"
        return True

    for i in range(4):
        new_x = curr_x + move_x[i]
        new_y = curr_y + move_y[i]
        if checkMove(new_x, new_y, maze):
            maze[new_x][new_y] = move
            if solveMaze(move, maze, new_x, new_y, move_x, move_y):
                return True

            maze[new_x][new_y] = 1
            
    return False

findWay()

