import turtle
import random

n, s, e, w = 1, 2, 4, 8
dx = { e : 1, w : -1, n : 0, s : 0 }
dy = { e : 0, w : 0, n : -1, s : 1 }
opposite = { e : w, w :  e, n :  s, s : n }


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
    directions = [n, s, e, w]
    random.shuffle(directions)

    for dir in directions:
        nx, ny = cx + dx[dir], cy + dy[dir]

        if ny in range(0, len(grid) - 1) and nx in range(0, len(grid[ny]) - 1) and grid[ny][nx] == 0:
            grid[cy][cx] |= dir
            grid[ny][nx] |= opposite[dir]
            carve_passage(nx, ny, grid)

def draw_maze_ascii(maze):
    
    # print(len(maze), len(maze[0])) prints 10, 10
    print(" " + "_" * (len(maze) * 2 - 1))
    for y in range(len(maze)):
        print("|", end='')
        for x in range(len(maze)):
            print(" " if maze[y][x] & s != 0 else "_", end='')
            if (maze[y][x] & e != 0):
                print(" " if (maze[y][x] | maze[y][x+1]) & s != 0 else "_", end='')
            else:
                print("|", end='')
        print("")

# True = blocked, False = open
def grid_to_maze(grid):
    # TODO: Draw top border
    maze = [[False] * (len(grid) + 1) for i in range(len(grid) * 2)]

    for y in range(len(maze)):
        maze[y][0] = True
        if y % 2 == 0:
            for x in range(len(grid)):
                if grid[int(y / 2)][x] & s != 0:
                    maze[y + 1][x + 1] = False # x + 1 to account for offset from border, y + 1 to move to line below current one
                else:
                    maze[y + 1][x + 1] = True # Block cell under

                if (grid[int(y / 2)][x] & e != 0):
                    if (grid[int(y / 2)][x] | grid[int(y / 2)][x + 1]) & s != 0:
                        maze[y + 1][x + 1] = False
                    else:
                        maze[y + 1][x + 1] = True # Block cell under
                else:
                    maze[y][x + 1] = True
                    maze[y + 1][x + 1] = True

    return maze

tur = turtle.Turtle()
cell_scale = 0.5
offset = 200

def move(trtl, position, cell_scale, offset):
  """
  Moves the turtle to a position on the grid
  
  turtle -- turtle to be moved : Turtle
  position -- the position on the grid to move to : tuple
  cell_scale -- the scale of the cells : int
  offset -- the offset of the grid from the origin : int
  """
  trtl.goto((position[0] * cell_scale * 20) - offset, (position[1] * cell_scale * 20) - offset)

def draw_maze(maze, trtl):
  """
  Draws the maze specified.

  Keyword Arguments:
  maze -- maze with True = blocked : 2D boolean list
  trtl -- turtle used to draw maze : Turtle
  """
  trtl.speed("fastest")
  trtl.shape("square")
  trtl.fillcolor("blue")
  trtl.shapesize(cell_scale)
  trtl.penup()
  for y in range(0, len(maze)):
    for x in range(0, len(maze[0])):
      move(trtl, (x, y), cell_scale, offset)
      if maze[y][x]:
        # Stamp the turtle to represent a blocked cell
        trtl.stamp()
  
  # Draw start and end squares
  trtl.fillcolor("red")
  trtl.goto(-offset, -offset)
  trtl.stamp()
  trtl.fillcolor("green")
  maze_end = ((len(maze)-1) * cell_scale) * 20 - offset
  trtl.goto(maze_end, maze_end)
  trtl.stamp()

mz = generate_maze(10)
draw_maze_ascii(mz)
draw_maze(grid_to_maze(mz), tur)

wn = turtle.Screen()
wn.mainloop()