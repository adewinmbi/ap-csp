# True = cell is blocked, False = cell is open

import random

# Constants

horizontal, vertical = 0, 1
south, east = 0, 1

grid_size = 10
min_passage_size = 1

# Utilities

def init_grid(): # Return 2D array of size grid_size by grid_size with all values equal to false
    grid = [[False] * grid_size for i in range(grid_size)]
    return grid

def get_orientation(width, height): # Unnecessary for a square grid
    if (width < height):
      return horizontal
    elif (height < width):
      return vertical
    return horizontal if random.randint(0, 1) == 0 else vertical 

# Main function

def divide(grid, x, y, width, height, orientation):

  if (width <= 1 or height <= 1): # If the area is too small to divide
    return

  # Wall starting position
  wx = x + (0 if orientation == horizontal else random.randint(0, width - 2)) # Subtract 2 to ensure wall isn't drawn at edge
  wy = y + (0 if orientation == vertical else random.randint(0, height - 2))

  # Wall opening position
  px = (random.randint(0, width) if orientation == horizontal else 0)
  py = (random.randint(0, height) if orientation == vertical else 0)

  # Direction the wall is drawn
  dx = (1 if orientation == horizontal else 0)
  dy = (1 if orientation == vertical else 0)

  wall_length = (width if orientation == horizontal else height)

  # Which direction is perpendicular to the wall
  perpendicular = (south if orientation == horizontal else east)

  # Draw wall
  for i in range(wall_length):
      grid[wy][wx] = (True if wx != px and wy != py else False) # Don't block the cell if it is the position of the opening
      wx += dx
      wy += dy

  # Recurse
  nx, ny = x, y
  w, h = [width, wy - y + 1] if orientation == horizontal else [wx - x + 1, height]
  divide(grid, nx, ny, w, h, get_orientation(w, h))

  nx, ny = [x, wy + 1] if orientation == horizontal else [wx + 1, y]
  w, h = [width, y + height - wy - 1] if orientation == horizontal else [x + width - wx - 1, height]
  divide(grid, nx, ny, w, h, get_orientation(w, h))

maze = init_grid()
divide(maze, 0, 0, grid_size, grid_size, get_orientation(grid_size, grid_size))
print(maze)
  
