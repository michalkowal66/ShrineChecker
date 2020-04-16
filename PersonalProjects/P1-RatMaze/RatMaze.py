import random
import numpy as np

def initMaze(start_pos, moves, maze, walls, path, crush_wall): #Initializes the maze creation process according to Prim's algorithm
    maze[start_pos] = "❑"  #We choose starting point we make a part of path
    path.append(start_pos)
    for move in moves:  #We check if it's possible to make any new move from the initial position, if yes we add it's position to wall list
        frontier_pos = (start_pos[0] + move[0], start_pos[1] + move[1])
        if checkWall(maze, frontier_pos):
            maze[frontier_pos] = "▣"
            walls.append(frontier_pos)
    
    #print(F"Maze with inital step created:\n{maze}")

    if createMaze(moves, maze, walls, path, crush_wall): #We run main function to create maze from that intial set up
        print(F"Final maze:\n{maze}")

def findrandAdjacent(position, crush_wall, moves, maze, path, search = True):   #Function to find adjacent path cell and break the wall to create passage
    while search:
        index = random.randrange(0, 4, 1)
        #print(F"Checking {index}")
        checked_pos = (position[0] + moves[index][0], position[1] + moves[index][1])
        if checkPath(maze, checked_pos):
            new_path = (position[0] + crush_wall[index][0], position[1] + crush_wall[index][1])
            maze[new_path] = "❑"
            path.append(new_path)
            #print("Found adjacent path cell")
            search = False

def checkPath(maze, position):  #Function checking if desired new position is a path cell
    if position[0] not in range(len(maze)) or position[1]  not in range(len(maze)) or maze[position] != "❑":
        return False
    else:
        return True

def checkWall(maze, position):  #Function checking if desired new position is a wall cell
    if position[0] not in range(len(maze)) or position[1]  not in range(len(maze)) or maze[position] == "❑" or maze[position] == "▣":
        return False
    else:
        return True

def createMaze(moves, maze, walls, path, crush_wall):   #Main function generating the maze
    if len(walls) == 0: #Finish condition according to Prim's algorithm
        print(F"Maze:\n{maze}\n")
        findWay(maze, start_pos, rat_moves)
        return True
    
    new_path = walls[random.randrange(0, len(walls), 1)]    #We choose random wall from the wall cell list
    maze[new_path] = "❑"   #Make that chosen wall a path cell

    #print(F"Random wall chosen:\n{maze}")

    findrandAdjacent(new_path, crush_wall, moves, maze, path)   #We run path finder to create a passage

    #print(F"Connection created:\n{maze}")

    for move in moves:  #We check if it's possible to make any new move from the new path cell, if yes we add it's position to wall list
        frontier_pos = (new_path[0] + move[0], new_path[1] + move[1])
        if checkWall(maze, frontier_pos):
            maze[frontier_pos] = "▣"
            walls.append(frontier_pos)

    #print(F"New frontier added:\n{maze}")

    walls.remove(new_path)  #We remove the wall from the walls list as it has become a path cell now

    # print(F"Remaining walls:{walls}")

    createMaze(moves, maze, walls, path, crush_wall) #Run the main function again, after there are no walls it will finish returning True

def findWay(maze, start_pos, rat_moves):    #Function initializing path finder from the initial point
    visited = "o"
    maze[start_pos] = visited

    if solveMaze(visited, maze, start_pos, rat_moves):  #Running main path finding utility
        print(F"Solved maze:\n{maze}")
    else:
        print("Error")

def checkMove(check_pos, maze):
    if check_pos[0] == len(maze) - 1 and check_pos[1] == len(maze) - 1:
        return True
    elif check_pos[0] not in range(len(maze)) or check_pos[1] not in range(len(maze)) or maze[check_pos] != "❑":
        return False
    else:
        return True    
       
def solveMaze(visited, maze, curr_pos, rat_moves):  #Main path finding utility
    if curr_pos[0] == len(maze) - 1 and curr_pos[1] == len(maze) - 1:   #Condition of finding way out
        maze[curr_pos] = "x"
        return True

    for i in range(4):  #Finding possible move from current position
        new_pos = (curr_pos[0] + rat_moves[i][0], curr_pos[1] + rat_moves[i][1])
        if checkMove(new_pos, maze):    #If move is possible we mark the cell as visited
            maze[new_pos] = visited
            if solveMaze(visited, maze, new_pos, rat_moves): #If next runs of the function lead to fulfilling main condition
                return True

            maze[new_pos] = "❑"    #If previous combination/s didn't lead to finding way out it moves back one move and looks for another solution
            
    return False #If it's not possible to find a way out of maze the function returns False

size = int(input("Choose the size of a maze: "))    #Defining maze size
maze = np.full((size,size), "◼")    #Creating maze as np.array
print(F"Initial array:\n{maze}\n")

rat_moves = [(1, 0), (0, -1), (-1, 0), (0, 1)]  #Rat's possible moves in the maze
moves = [(2, 0), (0, -2), (-2, 0), (0, 2)]  #Moves (y,x) in the opposite direction than stated due to arrays indexing - (1,0) -> 1 down, 0 to side
crush_wall = [(1, 0), (0, -1), (-1, 0), (0, 1)] #Returning moves that crush wall to create a passage

start_pos = (0, 0)

path = []
walls = []

initMaze(start_pos, moves, maze, walls, path, crush_wall)