# True = cell is blocked; False = cell is open

import random
import turtle

# Constants
horizontal, vertical = 0, 1
south, east = 0, 1

# Utilities
def init_grid(grid_size):
  """
  Return a 2D boolean list with all values set to false.

  grid_size = size of grid : int
  """
  grid = [[False] * grid_size for i in range(grid_size)]
  return grid

def get_orientation(width, height):
  """
  Return the orientation of the wall that should be drawn.

  width = width of the current division : int
  height = height of the current division : int
  """
  if (width < height):
    return horizontal
  elif (height < width):
    return vertical
  else:
    return horizontal if random.randint(0, 1) == 0 else vertical 

def generate_maze(grid_size):
  """
  Return a 2D boolean list maze with blocked cells as True and open cells as False.

  grid_size = size of grid : int 
  """
  maze = init_grid(grid_size)
  divide(maze, 0, 0, grid_size, grid_size, get_orientation(grid_size, grid_size))
  return maze

# Possible source of error...
# new walls can still be drawn perpendicular to holes in other walls
# new walls can still be drawn parallel and directly adjacent to other walls

# Main function
def divide(grid, x, y, width, height, orientation):
  """
  Recursively divide a grid with maze walls.

  grid = maze list : 2D boolean list
  x = x-offset of current division from origion of grid : int
  y = y-offset of current division from origion of grid : int
  width = width of current division : int
  height = height of current division : int
  orientation =  horizontal or vertical orientation of wall being drawn : int (0 or 1)
  """
  print(width, height)
  if (width < 10 or height < 10): # If the area is too small to divide
    return

  # Wall opening position
  px = (random.randint(0, width) if orientation == horizontal else 1)
  py = (random.randint(0, height) if orientation == vertical else 1)

  # Wall starting position
  wx = x + (0 if orientation == horizontal else random.randint(0, width - 2)) # Subtract 2 to ensure wall isn't drawn at edge
  wy = y + (0 if orientation == vertical else random.randint(0, height - 2))
  print(px, wx)


  # Direction the wall is drawn
  dx = (1 if orientation == horizontal else 0)
  dy = (1 if orientation == vertical else 0)

  wall_length = (width if orientation == horizontal else height)

  # Draw wall
  for i in range(wall_length):
    grid[wy][wx] = (True if wx != px and wy != py else False) # Don't block the cell if it is the position of the opening
    wx += dx
    wy += dy

  # Recurse
  nx, ny = x, y
  # w = width if orientation == horizontal else wx - x + 1
  # h = wy - y + 1 if orientation == horizontal else height
  w, h = [width, wy - y + 1] if orientation == horizontal else [wx - x + 1, height]
  divide(grid, nx, ny, w, h, get_orientation(w, h))

  # nx = x if orientation == horizontal else wx + 1
  # ny = wy + 1 if orientation == horizontal  else y
  nx, ny = [x, wy + 1] if orientation == horizontal else [wx + 1, y]
  # w = width if orientation == horizontal else x + width - wx - 1
  # h = y + height - wy - 1 if orientation == horizontal else height
  w, h = [width, y + height - wy - 1] if orientation == horizontal else [x + width - wx - 1, height]
  divide(grid, nx, ny, w, h, get_orientation(w, h))

# print(maze)

maze_drawer = turtle.Turtle()
maze_drawer.shape("square")
maze_drawer.fillcolor("blue")
maze_drawer.shapesize(1)
maze_drawer.penup()
maze_drawer.speed("fastest")

offset = 300
maze_size = 31
maze = generate_maze(maze_size)

def draw_maze(maze):
  maze_drawer.clear
  for x in range(0, maze_size):
    for y in range(0, maze_size):
      maze_drawer.goto(x * 20 - offset, y * 20 - offset)
      if maze[x][y]:
        maze_drawer.stamp()
        maze_drawer.penup()

draw_maze(maze)

wn = turtle.Screen()
wn.mainloop()

"""
Traceback (most recent call last):
  File "main.py", line 111, in <module>
    current_maze = maze.generate_maze(maze_size)
  File "/home/runner/Turtle-Escape/maze.py", line 44, in generate_maze
    divide(maze, 0, 0, grid_size, grid_size, get_orientation(grid_size, grid_size))
  File "/home/runner/Turtle-Escape/maze.py", line 95, in divide
    divide(grid, nx, ny, w, h, get_orientation(w, h))
  File "/home/runner/Turtle-Escape/maze.py", line 95, in divide
    divide(grid, nx, ny, w, h, get_orientation(w, h))
  File "/home/runner/Turtle-Escape/maze.py", line 95, in divide
    divide(grid, nx, ny, w, h, get_orientation(w, h))




Traceback (most recent call last):
  File "main.py", line 116, in <module>
    current_maze = maze.generate_maze(maze_size)
  File "/home/runner/Turtle-Escape/maze.py", line 44, in generate_maze
    divide(maze, 0, 0, grid_size, grid_size, get_orientation(grid_size, grid_size))
  File "/home/runner/Turtle-Escape/maze.py", line 95, in divide
    divide(grid, nx, ny, w, h, get_orientation(w, h))
  File "/home/runner/Turtle-Escape/maze.py", line 84, in divide
    grid[wy][wx] = (True if wx != px and wy != py else False) # Don't block the cell if it is the position of the opening
IndexError: list assignment index out of range
"""