# 2D array, True = blocked, false = open
# Every spot will be initialized as closed
# Turtle starts at origin

import turtle
import random
# import astar

maze_stamp = turtle.Turtle()
maze_stamp.shape("square")
maze_stamp.color("blue")
maze_stamp.shapesize(10)
maze_stamp.penup()

grid_size = 500
num_visited = 0
grid = []

def neighbors(current, grid):
  # Get neighboring points
  neighbors_list = [
    (current[0] - 1, current[1]),
    (current[0] + 1, current[1]),
    (current[0], current[1] - 1),
    (current[0], current[1] + 1)
  ]

  # Remove points out of bounds
  for i in neighbors_list:
    if i[0] < 0 or i[0] > grid_size - 1 or grid[i[0]][i[1]]:
      neighbors_list.remove(current)
  
  return neighbors_list

def generate_grid():
  temp = []

  for x in range(0, grid_size):
    for y in range(0, grid_size):
      temp.append([True, False]) # Tuple follows this format: (is cell blocked, has cell been visited)
    grid.append(temp)
    temp = []

def generate_maze(): # Aldous-Broder
  x, y = 0, 0
  grid[x][y][1] = True

  while (num_visited < grid_size - 1):
    random_neighbor = random.choice(neighbors((x, y), grid))
    nx, ny = random_neighbor
    if (grid[nx][ny][1] == False): # If cell has not been visited
      grid[nx][ny][1] = True
      grid[x][y][1] = True
      x = nx
      y = ny
      print("path made at: " + nx, ny)

def draw_maze(): # Multiply each coord by 5 so each cell is 10 units wide
  for x in range(0, grid_size - 1):
    for y in range(0, grid_size - 1):
      maze_stamp.goto(x * 5, y * 5)
      if (grid[x][y][0] == True): # If current cell is blocked
        maze_stamp.stamp()

generate_grid()
generate_maze()
draw_maze()

wn = turtle.Screen()
wn.mainloop()