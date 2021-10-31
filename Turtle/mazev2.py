# Recurive backtracking - https://weblog.jamisbuck.org/2010/12/27/maze-generation-recursive-backtracking

import turtle
import random

def init_grid(grid_size):
  """
  Return a 2D boolean list with all values set to false.

  grid_size = size of grid : int
  """
  grid = [[False] * grid_size for i in range(grid_size)]
  return grid

def add_frontier(x, y, grid, frontier):
    if x >= 0 and y >= 0 and y < grid.length and x < grid[y].length and grid[y][x] == 0:
        grid[y][x] |= 32
        frontier << [x][y]

def mark(x, y, grid, frontier):
    grid[y][x] |= 16
    add_frontier(x - 1, y, grid, frontier)
    add_frontier(x + 1, y, grid, frontier)
    add_frontier(x, y - 1, grid, frontier)
    add_frontier(x, y + 1, grid, frontier)

def get_neighbors(x, y, grid):
    n = []

    if x > 0 and grid[y][x - 1] != 0: n << [x - 1, y]
    if x + 1 < grid[y].length << [x + 1, y] 
    if y > 0 and grid[y - 1]n << [x, y - 1]
    n << [x, y + 1]

    return n
    
