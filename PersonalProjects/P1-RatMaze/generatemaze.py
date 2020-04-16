#Prim's algorithm
import random
import numpy as np

def generateMaze():
    size = int(input("Choose the size of a maze: "))
    maze = np.full((size,size), "◼")
    print(F"Initial array:\n{maze}\n")

    moves = [(2, 0), (0, -2), (-2, 0), (0, 2)] #Moves (y,x) in the opposite direction than stated due to arrays indexing - (1,0) -> 1 down, 0 to side
    crush_wall = [(1, 0), (0, -1), (-1, 0), (0, 1)]

    start_pos = (0, 0)

    path = []
    walls = []

    initMaze(start_pos, moves, maze, walls, path, crush_wall)

def initMaze(start_pos, moves, maze, walls, path, crush_wall):
    maze[start_pos] = "❑"
    path.append(start_pos)
    for move in moves:
        frontier_pos = (start_pos[0] + move[0], start_pos[1] + move[1])
        if checkWall(maze, frontier_pos):
            maze[frontier_pos] = "▣"
            walls.append(frontier_pos)
    
    #print(F"Maze with inital step created:\n{maze}")

    if createMaze(moves, maze, walls, path, crush_wall):
        print(F"Final maze:\n{maze}")

def findrandAdjacent(position, crush_wall, moves, maze, path, search = True):
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

def checkPath(maze, position):
    if position[0] not in range(len(maze)) or position[1]  not in range(len(maze)) or maze[position] != "❑":
        return False
    else:
        return True

def checkWall(maze, position):
    if position[0] not in range(len(maze)) or position[1]  not in range(len(maze)) or maze[position] == "❑" or maze[position] == "▣":
        return False
    else:
        return True

def createMaze(moves, maze, walls, path, crush_wall):
    if len(walls) == 0:
        print(F"Maze:\n{maze}")
        return True
    
    new_path = walls[random.randrange(0, len(walls), 1)]
    maze[new_path] = "❑"

    #print(F"Random wall chosen:\n{maze}")

    findrandAdjacent(new_path, crush_wall, moves, maze, path)

    #print(F"Connection created:\n{maze}")

    for move in moves:
        frontier_pos = (new_path[0] + move[0], new_path[1] + move[1])
        if checkWall(maze, frontier_pos):
            maze[frontier_pos] = "▣"
            walls.append(frontier_pos)

    #print(F"New frontier added:\n{maze}")

    walls.remove(new_path)

    # print(F"Remaining walls:{walls}")

    createMaze(moves, maze, walls, path, crush_wall)
    

if __name__ == "__main__":
    generateMaze()