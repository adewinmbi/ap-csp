import maze
import astar
import turtle
import maze_utilities as util

# Constants
cell_scale = 0.75
offset = 200
maze_size = 30

# Init turtle
maze_drawer = turtle.Turtle()

# Function declarations
def empty_maze(maze_size):
  """
  Creates an empty maze.
  
  Keyword Arguments:
  maze_size - size length of maze : int > 0
  """
  maze = []
  for i in range(0, maze_size):
    column = []
    for j in range(0, maze_size):
      column.append(False)
    maze.append(column)
  
  return maze

def draw_maze(maze, trtl):
  """
  Draws the maze specified.

  Keyword Arguments:
  maze -- maze with True = blocked : 2D boolean list
  trtl -- turtle used to draw maze : Turtle
  """
  print("Rendering the maze...")
  trtl.speed(0)
  trtl.shape("square")
  trtl.fillcolor("blue")
  trtl.shapesize(cell_scale)
  trtl.penup()
  for x in range(0, maze_size):
    for y in range(0, maze_size):
      util.move(trtl, (x, y), cell_scale, offset)
      if maze[x][y]:
        # Stamp the turtle to represent a blocked cell
        trtl.stamp()
  
  # Draw start and end squares
  trtl.fillcolor("red")
  trtl.goto(-offset -1, -offset -2)
  trtl.stamp()
  trtl.fillcolor("green")
  maze_end = ((maze_size-1) * cell_scale) * 20 - offset
  trtl.goto(maze_end, maze_end)
  trtl.stamp()

def draw_border(x_len, y_len, trtl):
  """
  Draws a border around the maze.

  Keyword Arguments:
  border_size -- side length of the border : int
  trtl -- turtle used to draw the border : Turtle
  """
  trtl.speed(0)
  trtl.shape("square")
  trtl.fillcolor("black")
  trtl.begin_fill()
  trtl.shapesize(cell_scale)
  trtl.penup()
  util.move(trtl, (-1, -1), cell_scale, offset)
  trtl.setheading(0)
  for i in range(2):
    for j in range(x_len):
      trtl.stamp()
      trtl.forward(cell_scale * 20)
    trtl.left(90)
    for j in range(y_len):
      trtl.stamp()
      trtl.forward(cell_scale * 20)
    trtl.left(90)
  trtl.fillcolor("orange")
  trtl.end_fill()

# Move the turtle through the maze
def traverse_maze(maze, trtl, live_trace, start, end):
  """
  Moves the turtle through the maze.

  Keyword Arguments:
  maze -- maze with True=blocked : 2D boolean list
  trtl -- turtle used to traverse the maze : Turtle
  live_trace -- whether or not the a* algorithm will be visualized : bool
  """
  trtl.speed(2)
  trtl.goto(0 - offset, 0 - offset)

  trtl.shape("square")
  trtl.fillcolor("white")
  trtl.shapesize(cell_scale)
  trtl.pendown()

  # Generate path with a*
  if (live_trace):
    path = astar.astar(start, end, astar.manhattan_distance, maze, trtl=trtl, offset=offset, cell_scale=cell_scale)
  else:
    path = astar.astar(start, end, astar.manhattan_distance, maze, offset=offset, cell_scale=cell_scale)

  # If the goal was reached
  if (len(path) == 1):
    trtl.penup()
    trtl.color("green")
    trtl.pensize(5)
    trtl.goto(-offset, -offset)
    trtl.pendown()
    for position in path[0]:
      util.move(trtl, position, cell_scale, offset)
  else: # Draw all paths if the goal was not reached
    trtl.penup()
    trtl.fillcolor("gray")
    trtl.shapesize(cell_scale*3/4)
    trtl.pencolor("red")
    trtl.pensize(5)
    trtl.goto(-offset, -offset)
    trtl.pendown()
    print(path)
    for position in path[0][0]:
      util.move(trtl, position, cell_scale, offset)

# Main body
print("Welcome to Turtle Escape!\nThis program generates a maze and tries to find a path through it using the A* algorithm.")

print("Initializing the maze...")
raw_maze = maze.generate_maze(int(maze_size/2))
draw_border(maze_size-2, maze_size-1, maze_drawer)

print("Converting the maze to ascii...")
ascii_maze = maze.draw_maze_ascii(raw_maze)
for i in ascii_maze:
  print(i)

print("Converting the maze to blocks...")
current_maze = maze.string_to_maze(ascii_maze)
maze.draw_maze(current_maze, maze_drawer, cell_scale, offset)

traverse_maze(current_maze, maze_drawer, True, (0,0), (maze_size-4, maze_size-3))


#maze.draw_maze_ascii(current_maze)
#draw_border(maze_size + 1, maze_drawer)
#draw_maze(current_maze, maze_drawer)
#traverse_maze(current_maze, maze_drawer, True)

# Make screen persist
wn = turtle.Screen()
wn.mainloop()
