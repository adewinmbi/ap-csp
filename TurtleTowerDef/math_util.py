import math

def manhattan_distance(pos1, pos2):
  return (pos2[0] - pos1[0]) + (pos2[1] - pos1[1])

def euclidian_distance(pos1, pos2):
  x = (pos2[0] - pos1[0])**2
  y = (pos2[1] - pos1[1])**2
  return math.sqrt(x + y)

def get_angle(origin, point):
  x = (origin[0] - point[0])
  y = (origin[1] - point[1])
  return math.atan2(y, x)

def get_angle_degrees(origin, point):
  return math.degrees(get_angle(origin, point))

def get_pos_angle(angle):
  return ( angle + 360 ) % 360