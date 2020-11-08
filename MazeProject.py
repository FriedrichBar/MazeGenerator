from Display import *

Maze, startingCell = DFS(50, 50)
pixelsMaze = mazeToPixels(Maze, startingCell)
savingMaze('Maze.png', pixelsMaze)