#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic", "arrow", "turtle", "circle", "square", "triangle", "classic", "arrow", "turtle", "circle", "square", "triangle", "classic", "arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold", "red", "blue", "green", "orange", "purple", "gold", "red", "blue", "green", "orange", "purple", "gold", "red", "blue", "green", "orange", "purple", "gold"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  new_color = turtle_colors.pop()
  t.pencolor(new_color)
  t.fillcolor(new_color)
  t.pensize(5)
  t.speed(0)
  t.penup()
  my_turtles.append(t)

#  
startx = 0
starty = 0
direction = 0
segmentLength = 50

#
for t in my_turtles:
  t.setheading(direction)
  t.goto(startx, starty)
  t.pendown()
  t.right(45)
  t.forward(segmentLength)
  segmentLength += 10 # Increase the segment length every iteration
  direction = t.heading() # Save the past direction/heading to be used in the next iteration
  startx = t.xcor()
  starty = t.ycor()

  # startx = startx + 50
  # starty = starty + 50

wn = trtl.Screen()
wn.mainloop()