import math

def generate_path(field_size):
  path = []

  vert_path_len = field_size - 6 # Padding of 3 on top and bottom
  hori_path_len = math.floor(field_size / 5)
  extra = field_size % 5
  mid_y = math.floor(field_size / 2)

  path_x = 0 # Current x relative to the horizontal path that is being worked on
  dir = 0 # 0 = down, 1 = up
  for x in range(field_size):
    path_x += 1

    if (path_x < hori_path_len):
      path.append((x, mid_y))
    elif (path_x == hori_path_len):
      if dir == 1: # If the path should go up
        for y in range(vert_path_len - x):
          path.append((x, y + mid_y))
      else: # If the path should go down
        for y in range(vert_path_len - x):
          path.append((x, mid_y - y))
      path_x = 0

  return path