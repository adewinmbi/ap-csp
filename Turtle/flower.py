#   Modify this code in VS Code to alternate the colors of the 
#   floors every three floors
import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)
painter.pensize(5)

# starting location of the tower
x = -150
y = -150

# height of tower and a counter for each floor
num_floors = 63
floor = 0

# iterate
while floor < num_floors:
  # set placement and color of turtle
  painter.penup()
  painter.goto(x, y)
  
  if (floor % 6 > 2): # Use modulo to alternate colors
      painter.color("blue")
  else:
      painter.color("grey")

  y = y + 5 # location of next floor
  floor = floor + 1

  #draw the floor
  painter.pendown()
  painter.forward(50)

wn = trtl.Screen()
wn.mainloop()