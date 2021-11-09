import math
import maze_utilities as util

# Placeholder for infinity
max_length = 99999999

def manhattan_distance(point_1, point_2):
  """
  Return the manhattan distance between two points.

  Keyword Arguments:
  point_1 -- first point : tuple
  point_2 -- second point : tuple
  """
  x_dist = abs(int(point_2[0]) - int(point_1[0]))
  y_dist = abs(int(point_2[1]) - int(point_1[1]))

  return x_dist + y_dist

def euclidean_distance(point_1, point_2):
  """
  Return the euclidean distance between two points

  Keyword Arguments:
  point_1 -- first point : tuple
  point_2 -- second point : tuple
  """
  x_dist = abs(point_2[0] - point_1[0])
  y_dist = abs(point_2[1] - point_1[1])

  return math.sqrt(x_dist*x_dist + y_dist*y_dist)

def prepend(original_list, new_item):
  """
  Add an item to the start of a list

  Keyword Arguments:
  original_list -- original list : list
  new_item -- item to be added to the list : any type
  """
  new_list = [new_item]
  for i in original_list:
    new_list.append(i)
  return new_list

def reconstruct_all_paths(previous, max_path=10000):
  """
  Reconstruct the steps from every path from A*

  Keyword Arguments:
  previous -- dictionary matching a node to the node before it : tuple dictionary
  max_path -- length of the maximum path : int
  """
  total_paths = []
  # Reconstruct all possible paths
  for i in previous.keys():
    total_paths.append(reconstruct_path(previous, i, max_path))
  # Find the longest path
  total_paths.sort(key=len)
  return total_paths

def reconstruct_path(previous, current, max_path=10000):
  """
  Reconstruct the steps in an A* path

  Keyword Arguments:
  previous -- dictionary matching a node to the node before it : tuple dictionary
  current -- tuple with (x,y) : tuple
  max_path -- length of the maximum path : int
  """
  total_path = [current]
  i = 0
  # Retrace steps from the goal until the start is reached
  while current in previous.keys() and i <= max_path:
    current = previous[current]
    total_path = prepend(total_path, current)
    i += 1
  return [total_path]

def neighbors(current, grid):
  """
  Return the neighbors of a tuple

  Keyword Arguments:
  current -- current point (tuple with x,y) : tuple
  grid -- grid that the point lies on (2D list of tuples) : list
  """
  # Get neighboring points
  neighbors_list = [
    (current[0] - 1, current[1]),
    (current[0] + 1, current[1]),
    (current[0], current[1] - 1),
    (current[0], current[1] + 1)
  ]

  # Remove points out of bounds
  temp_list = list(neighbors_list)

  for i in temp_list:
    if (i[0] < 0 or i[0] >= len(grid) or i[1] < 0 or i[1] >= len(grid[0]) or grid[i[0]][i[1]]):
      neighbors_list.remove(i)
  
  return neighbors_list

def astar(start, goal, h_score, grid, max_iterations = 1000, trtl = None, cell_scale = 0.5, offset = 100):
  """
  Find a path from start to goal

  Keyword Arguments:
  start -- start point (tuple with x y coordinates) : tuple
  goal -- end point (tuple with x y coordinates) : tuple
  h -- heuristic function : function
  max_iterations -- max number of iterations the algorithm can go through : int
  turtle -- turtle for live tracing of the path : Turtle
  cell_scale -- scale of the turtle : int
  offset -- offset of the entire maze from the origin : int
  """
  print("Beginning pathfinding with A*...")

  # Initialize turtle
  if (trtl):
    trtl.shape("square")
    trtl.fillcolor("white")
    trtl.penup()

  # The set of discovered points that may need to be expanded to find the print
  open_set = [start]

  # previous[n] is the point before n on the cheapest known path to n from start.
  previous = {}

  # g_score[n] is the cost of the cheapest path from the start to n.
  g_score = {}
  
  # f_score[n] is g_score[n] + h_score(n)
  f_score = {}

  # Set default g_score to (basically) infinity
  for x in range(len(grid)):
    for y in range(len(grid[x])):
      g_score[(x,y)] = max_length
      f_score[(x,y)] = max_length
  
  # Set default g_score of start
  g_score[start] = 0
  f_score[start] = h_score(start, goal)
  
  # How many times the algorithm has iterated
  iterations = 0

  # Move the turtle to the start
  if (trtl):
    trtl.goto(-offset, -offset)
  
  # Loop until all paths are explored
  while iterations < max_iterations:
    # set current to the point with the lowest f_score
    current = open_set[0]
    for i in open_set:
      if (f_score[i] < f_score[current]):
        current = i
    
    # If at goal, return the path
    if (current == goal):
      print("Found a path!")
      return reconstruct_path(previous, current, 1000)
    
    # Remove the current tile from the open set, as it has already been searched
    if (current in open_set):
      open_set.remove(current)

    for neighbor in neighbors(current, grid):
      if (trtl):
        util.move(trtl, current, cell_scale, offset)
        if (current != start and current != goal):
          trtl.stamp()
      
      # A possible new g_score for the neighbor
      temporary_g_score = g_score[current] + 1
      # Test if this way has a better g_score than before
      if (temporary_g_score < g_score[neighbor]):
        previous[neighbor] = current
        g_score[neighbor] = temporary_g_score
        f_score[neighbor] = g_score[neighbor] + h_score(neighbor, goal)

        # Move turtle to position if being used
        if (trtl):
          util.move(trtl, neighbor, cell_scale, offset)
          if (neighbor != start and neighbor != goal):
            trtl.stamp()
        
        if (neighbor not in open_set):
          open_set.append(neighbor)
    
    iterations += 1
    
    # Terminate search if open set is empty
    if (open_set == []):
      break
  
  # Open set is empty, but the goal was not reached
  print("Could not find a path out of the maze.")
  return reconstruct_all_paths(previous, len(grid)^2)
