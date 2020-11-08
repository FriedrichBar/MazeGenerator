from ImagesUtils import empty_img, write_img
from Maze import *

def mazeToPixels(Maze, startingCell):
    """
    Transforms a maze(matrix) into pixels

    IN: Maze(matrix)

    OUT: pixels
    """
    startingCellX = startingCell[0]
    startingCellY = startingCell[1]
    # Fetching size of the maze
    pixels = empty_img(len(Maze), len(Maze[0]))
    for x in range(len(pixels)):
        for y in range(len(pixels[x])):
            for z in range(len(pixels[x][y])):
                # If it's a wall
                if Maze[x][y] == 0:
                    pixels[x][y][z] = 0
                # If it's a path
                if Maze[x][y] == 1:
                    pixels[x][y][z] = 255
    # Painting the goal cell in red
    pixels[startingCellX][startingCellY][0] = 255
    pixels[startingCellX][startingCellY][1] = 0
    pixels[startingCellX][startingCellY][2] = 0
    return pixels

def savingMaze(file, pixels):
    """
    Saves a maze into a .png file
    
    IN: file(file's name), pixels

    OUT: N/A
    """
    write_img(file, pixels)