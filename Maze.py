import numpy as np
import random

def initMaze(L,w):
    """
    Initialize the maze

    IN: L(length), w(width)

    OUT: Maze(matrix Lxw)
    """
    return np.zeros((L,w))

def neighborsCheck(Maze, cellX, cellY):
    """
    Checks if a cell has only one visited neighbor

    IN: Maze(matrix), cellX, cellY

    OUT: boolean
    """
    # Fetching sums of neighbors cells
    lines, columns = Maze.shape
    l0, l1 = max(0, cellX-1), min(lines-1, cellX+1)
    c0, c1 = max(0, cellY-1), min(columns-1, cellY+1)
    ls = list({l0, cellX, l1})
    cs = [[c] for c in list({c0, cellY, c1})]
    # If the sum of the neighbors equals 1
    if Maze[ls, cs].sum() - Maze[cellX, cellY] == 1:
        return True
    # Else
    return False

def cellNeighbors(Maze, cellX, cellY):
    """
    Fetch neighbors of cell

    IN: Maze(matrix), cellX, cellY

    OUT: List of cells
    """
    # Initialize the matrix for the neighbors of cell
    listCells = [[cellX-1, cellY-1], [cellX-1, cellY], [cellX-1, cellY+1],
                  [cellX,   cellY-1],                   [cellX,   cellY+1],
                  [cellX+1, cellY-1], [cellX+1, cellY], [cellX+1, cellY+1]]
    # Initialize a matrix for removing any neighbors to not have any OutOfRange
    deletionCells = []
    # If cellX is in top of the Maze
    if cellX == 0:
        deletionCells.append((cellX-1, cellY-1))
        deletionCells.append((cellX-1, cellY))
        deletionCells.append((cellX-1, cellY+1))
    # If cellX is at the bottom of the Maze
    if cellX == len(Maze) - 1:
        deletionCells.append((cellX+1, cellY-1))
        deletionCells.append((cellX+1, cellY))
        deletionCells.append((cellX+1, cellY+1))
    # If cellY is at the left of the Maze
    if cellY == 0:
        deletionCells.append((cellX-1, cellY-1))
        deletionCells.append((cellX, cellY-1))
        deletionCells.append((cellX+1, cellY-1))
    # If cellY is at the right of the Maze
    if cellY == len(Maze[0]) - 1:
        deletionCells.append((cellX-1, cellY+1))
        deletionCells.append((cellX, cellY+1))
        deletionCells.append((cellX+1, cellY+1))
    # Removing any duplicates
    deletionCells = list(dict.fromkeys(deletionCells))
    # Removing the cells
    for delete in deletionCells:
        listCells.pop(listCells.index([delete[0], delete[1]]))
    return listCells

def validNeighborsCell(Maze, cellX, cellY):
    """
    Fetch neighbors of cell that are valid

    IN: Maze(matrix), cellX, cellY

    OUT: List of cells
    """
    # Fetching neighbors of cell
    listCells = cellNeighbors(Maze, cellX, cellY)
    # Initializing list of valid neighbors
    listValidCells = []
    # For each neighbors of cell
    for neighbor in listCells:
        # If the sum of the neighbor cells equals 1
        if neighborsCheck(Maze, neighbor[0], neighbor[1]) and Maze[neighbor[0]][neighbor[1]] == 0:
            # We add this cell to the valid cells
            listValidCells.append(neighbor)
    return listValidCells

def DFS(L, w):
    """
    Do the Depth-First Search (iterative implementation) in order to generate the maze

    IN: L(length), w(width)
    
    OUT: Maze(matrix), startingCell
    """
    # Initializing the Maze
    Maze = initMaze(L, w)
    # We randomly choose the starting cell
    startingCell = [random.randrange(L), random.randrange(w)]
    # Initializing the stack
    stack = []
    # Adding the starting cell to the start
    stack.append([startingCell[0], startingCell[1]])
    Maze[startingCell[0]][startingCell[1]] = 1
    # While the stack is not empty
    while len(stack) != 0:
        # We take the last cell of the stack
        currentCell = stack[-1]
        # We get the valid neighbors of the current cell
        listNextCells = validNeighborsCell(Maze, currentCell[0], currentCell[1])
        # If there are neighbors
        if len(listNextCells) > 0:
            nextCell = random.choice(listNextCells)
            Maze[nextCell[0]][nextCell[1]] = 1
            stack.append(nextCell)
        # Else we need to backtrack
        else:
            stack.pop()
            # We avoid a IndexOutOfRange
            if len(stack) != 0:
                currentCell = stack[-1]
    return Maze, startingCell