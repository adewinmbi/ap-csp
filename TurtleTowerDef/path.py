import math

def generate_path(field_size, complexity=5):
  print("Generating path...")
  path = []

  hori_path_len = math.floor(field_size / complexity)
  vert_path_len = math.floor(field_size / 2) - 2 # Padding on top and bottom of path
  mid_y = math.floor(field_size / 2)

  path_x = 0 # Current x relative to the horizontal path that is being worked on
  dir = 0 # 0 = down, 1 = up
  x_paths_created = 0
  curr_y = mid_y
  
  for x in range(field_size):
    path_x += 1

    if (path_x < hori_path_len):
      path.append((x, curr_y))
    elif (path_x == hori_path_len):
      if dir == 1: # If the path should go up
        temp_y = 0
        if (x_paths_created % 2 != 0):
          # Append in reverse so the turtle travels the path cells in order
          for y in reversed(range(vert_path_len)):
            path.append((x, mid_y + y))
            temp_y = mid_y + (vert_path_len - 1)
        else:
          for y in range(vert_path_len):
            path.append((x, mid_y + y))
            temp_y = mid_y + y
        curr_y = temp_y

      else: # If the path should go down
        temp_y = 0
        if (x_paths_created % 2 != 0):
          # Append in reverse
          for y in reversed(range(vert_path_len)):
            path.append((x, mid_y - y))
            temp_y = mid_y - (vert_path_len - 1)
        else:
          for y in range(vert_path_len):
            path.append((x, mid_y - y))
            temp_y = mid_y - y
        curr_y = temp_y
      path_x = 0
      x_paths_created += 1
      if (x_paths_created % 2 == 0):
        curr_y = mid_y
        dir = 1 - dir
      
  # Remove last vertical path
  for i in range(vert_path_len - 1):
    path.pop()

  return path
  