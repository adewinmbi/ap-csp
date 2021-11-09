import turtle

def move(trtl, position, cell_scale, offset):
  """
  Moves the turtle to a position on the grid
  
  turtle -- turtle to be moved : Turtle
  position -- the position on the grid to move to : tuple
  cell_scale -- the scale of the cells : int
  offset -- the offset of the grid from the origin : int
  """
  trtl.goto((position[0] * int(cell_scale * 20)) - offset, (position[1] * int(cell_scale * 20)) - offset)
