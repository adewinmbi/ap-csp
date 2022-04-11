import math

cardinal_directions = {
  "e" : 0,
  "n" : 90,
  "w" : 180,
  "s" : 270
}

def manhattan_distance(pos1, pos2):
  return (pos2[0] - pos1[0]) + (pos2[1] - pos1[1])

def euclidian_distance(pos1, pos2):
  x = (pos2[0] - pos1[0])**2
  y = (pos2[1] - pos1[1])**2
  return math.sqrt(x + y)

def get_angle(origin, point):
  x = (point[0] - origin[0])
  y = (point[1] - origin[1])
  return math.atan2(y, x)

def get_angle_degrees(origin, point):
  return math.degrees(get_angle(origin, point))

def get_cardinal_direction(origin, point):
  return ((("e" if point[0] - origin[0] > 0 else "w") if point[0] != origin[0] else ("n" if point[1] - origin[1] > 0 else "s")))

def get_pos_angle(angle):
  return ( angle + 360 ) % 360