import random
import maze_utilities as util

# Initial setup
n, s, e, w = 1, 2, 4, 8
dx = { e : 1, w : -1, n : 0, s : 0 }
dy = { e : 0, w : 0, n : -1, s : 1 }
opposite = { e : w, w :  e, n :  s, s : n }

# Dictionary for converting ascii to a grid
char_to_cell = { "|" : (True, True), "_" : (False, True), " " : (False, False) }

def init_grid(grid_size):
  """
  Return a 2D boolean list with all values set to false.

  grid_size = size of grid : int
  """
  grid = [[False] * grid_size for i in range(grid_size)]
  return grid

def generate_maze(grid_size):
  maze = init_grid(grid_size)
  carve_passage(0, 0, maze)
  return maze

def carve_passage(cx, cy, grid):
  """
  Recursively carve passages to create a maze with one solution

  cx = current x-axis position : int
  cy = current y-axis position : int
  """
  directions = [n, s, e, w]
  random.shuffle(directions)

  for dir in directions:
    nx, ny = cx + dx[dir], cy + dy[dir]

    if ny in range(0, len(grid) - 1) and nx in range(0, len(grid[ny]) - 1) and grid[ny][nx] == 0:
      grid[cy][cx] |= dir
      grid[ny][nx] |= opposite[dir]
      carve_passage(nx, ny, grid)

def draw_maze_ascii(maze):
  """
  Return a 2D string list with ascii characters representing a maze.

  maze = representation of a maze using edges around cells : 2D list
  """
  ascii_maze = []
  for y in range(len(maze)):
    row_string = ""
    row_string += "|"
    for x in range(len(maze)):
      row_string += (" " if maze[y][x] & s != 0 else "_")
      if (maze[y][x] & e != 0):
        row_string += (" " if (maze[y][x] | maze[y][x+1]) & s != 0 else "_")
      else:
        row_string += "|"
    ascii_maze.append(row_string)
  
  return ascii_maze

def string_to_maze(string):
  """
  Return a boolean 2D list representing a maze.

  string = maze converted to ascii output : 2D string list
  """
  maze = []

  for y in range(len(string)):
    cur_row = []
    next_row = []
    for x in range(len(string[0])):
      chars = char_to_cell[string[y][x]]
      cur_row.append(chars[0])
      next_row.append(chars[1])
    maze.append(cur_row)
    maze.append(next_row)
  
  # Remove unwanted edge patterns
  for y in range(len(string)):
    for i in range(3):
      maze[y].pop()
  for i in range(3):
    maze.pop()
  
  return maze  

def draw_maze(maze, trtl, cell_scale=0.5, offset=100, maze_size=30):
  """
  Draws the maze specified.

  Keyword Arguments:
  maze -- maze with True = blocked : 2D boolean list
  trtl -- turtle used to draw maze : Turtle
  cell_scale -- the size of each cell : float
  offset -- the offset of the cells from the origin : int
  """
  trtl.speed("fastest")
  trtl.shape("square")
  trtl.fillcolor("blue")
  trtl.shapesize(cell_scale)
  trtl.penup()
  for y in range(0, len(maze)):
    for x in range(0, len(maze[0])):
      util.move(trtl, (y, x), cell_scale, offset)
      if maze[y][x] == True:
        # Stamp the turtle to represent a blocked cell
        trtl.stamp()
  
  # Draw start and end squares
  trtl.fillcolor("red")
  util.move(trtl, (0,0), cell_scale, offset)
  trtl.stamp()
  trtl.fillcolor("green")
  util.move(trtl, (maze_size-4, maze_size-3), cell_scale, offset)
  trtl.stamp()