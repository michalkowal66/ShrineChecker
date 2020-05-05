import random
import numpy as np

class RatsMaze():
    def __init__(self, size, start_pos = (0,0)):
        self.start_pos = start_pos
        self.rat_moves = [(1, 0), (0, -1), (-1, 0), (0, 1)] #Rat's possible moves in the maze
        self.moves = [(2, 0), (0, -2), (-2, 0), (0, 2)] #Moves (y,x) in the opposite direction than stated due to arrays indexing - (1,0) -> 1 down, 0 to side
        self.path = []
        self.walls = []
        self.crush_wall = [(1, 0), (0, -1), (-1, 0), (0, 1)] #Returning moves that crush wall to create a passage
        self.size = size #Defining maze size
        self.init_array = np.full((self.size + self.size-1, self.size + self.size-1), "◼")
        self.maze = []

    def help(self):
        print("To initialize the maze creator run 'initCreator' method.\nTo find way out of the maze run 'findWay' method.")


    def initCreator(self): #Initializes the maze creation process according to Prim's algorithm    
        maze = np.full((self.size + self.size-1, self.size + self.size-1), "◼")    #Creating maze as np.array
        print(F"Initial array:\n{maze}\n")

        maze[self.start_pos] = "❑"  #We choose starting point we make a part of path
        self.path.append(self.start_pos)
        for move in self.moves:  #We check if it's possible to make any new move from the initial position, if yes we add it's position to wall list
            frontier_pos = (self.start_pos[0] + move[0], self.start_pos[1] + move[1])
            if self.checkWall(maze, frontier_pos):
                maze[frontier_pos] = "▣"
                self.walls.append(frontier_pos)
        
        #print(F"Maze with inital step created:\n{maze}")

        if self.createMaze(maze): #We run main function to create maze from that intial set up
            print(F"Final maze:\n{maze}\n")
            self.maze = maze
        else:
            print("Error")

    def createMaze(self, maze):   #Main function generating the maze
        if len(self.walls) == 0: #Finish condition according to Prim's algorithm
            return True
        
        new_path = self.walls[random.randrange(0, len(self.walls), 1)]    #We choose random wall from the wall cell list
        maze[new_path] = "❑"   #Make that chosen wall a path cell

        #print(F"Random wall chosen:\n{maze}")

        self.findrandAdjacent(new_path, maze)   #We run path finder to create a passage

        #print(F"Connection created:\n{maze}")

        for move in self.moves:  #We check if it's possible to make any new move from the new path cell, if yes we add it's position to wall list
            frontier_pos = (new_path[0] + move[0], new_path[1] + move[1])
            if self.checkWall(maze, frontier_pos):
                maze[frontier_pos] = "▣"
                self.walls.append(frontier_pos)

        #print(F"New frontier added:\n{maze}")

        self.walls.remove(new_path)  #We remove the wall from the walls list as it has become a path cell now

        # print(F"Remaining walls:{walls}")

        if self.createMaze(maze):
            return True #Run the main function again, after there are no walls it will finish returning True

        return False

    def findrandAdjacent(self, position, maze, search = True):   #Function to find adjacent path cell and break the wall to create passage
        while search:
            index = random.randrange(0, 4, 1)
            #print(F"Checking {index}")
            checked_pos = (position[0] + self.moves[index][0], position[1] + self.moves[index][1])
            if self.checkPath(maze, checked_pos):
                new_path = (position[0] + self.crush_wall[index][0], position[1] + self.crush_wall[index][1])
                maze[new_path] = "❑"
                self.path.append(new_path)
                #print("Found adjacent path cell")
                search = False

    def checkPath(self, maze, position):  #Function checking if desired new position is a path cell
        if position[0] not in range(len(maze)) or position[1]  not in range(len(maze)) or maze[position] != "❑":
            return False
        else:
            return True

    def checkWall(self, maze, position):  #Function checking if desired new position is a wall cell
        if position[0] not in range(len(maze)) or position[1]  not in range(len(maze)) or maze[position] == "❑" or maze[position] == "▣":
            return False
        else:
            return True

    def findWay(self):    #Function initializing path finder from the initial point
        visited = "o"
        self.maze[self.start_pos] = visited

        if self.solverUtil(visited, self.maze, self.start_pos):  #Running main path finding utility
            print(F"Solved maze:\n{self.maze}")
        else:
            print("Error")
        
    def solverUtil(self, visited, maze, curr_pos):  #Main path finding utility
        if curr_pos[0] == len(maze) - 1 and curr_pos[1] == len(maze) - 1:   #Condition of finding way out
            maze[curr_pos] = "x"
            return True

        for _ in range(4):  #Finding possible move from current position
            new_pos = (curr_pos[0] + self.rat_moves[_][0], curr_pos[1] + self.rat_moves[_][1])
            if self.checkMove(new_pos, maze):    #If move is possible we mark the cell as visited
                maze[new_pos] = visited
                if self.solverUtil(visited, maze, new_pos): #If next runs of the function lead to fulfilling main condition
                    return True

                maze[new_pos] = "❑"    #If previous combination/s didn't lead to finding way out it moves back one move and looks for another solution
                
        return False #If it's not possible to find a way out of maze the function returns False

    def checkMove(self, check_pos, maze):
        if check_pos[0] == len(maze) - 1 and check_pos[1] == len(maze) - 1:
            return True
        elif check_pos[0] not in range(len(maze)) or check_pos[1] not in range(len(maze)) or maze[check_pos] != "❑":
            return False
        else:
            return True    


if __name__ == "__main__":
    inst = RatsMaze(9)

    inst.help()

    inst.initCreator()

    inst.findWay()