#   a115_robot_maze.py
import turtle as trtl

#----- maze and turtle config variables
screen_h = 400
screen_w = 420
startx = -100
starty = -100
turtle_scale = 1.5

#------ robot commands
def move():
  robot.dot(10)
  robot.fd(50)

def turn_left():
  robot.speed(0)
  robot.lt(90)
  robot.speed(2)

def turn_right():
  robot.speed(0)
  robot.lt(-90)
  robot.speed(2)

#----- init screen
wn = trtl.Screen()
wn.setup(width=screen_w, height=screen_h)
robot_image = "res/robot.gif"
wn.addshape(robot_image)

#----- init robot
robot = trtl.Turtle(shape=robot_image)
robot.hideturtle()
robot.color("darkorchid")
robot.pencolor("darkorchid")
robot.penup()
robot.setheading(90)
robot.turtlesize(turtle_scale, turtle_scale)
robot.goto(startx, starty)
robot.speed(2)
robot.showturtle()

#---- TODO: change maze here
wn.bgpic("res/maze4.png") # other file names should be maze2.png, maze3.png

#---- While loops
steps = 4
i = 2

while (i > 0):
  while (steps > 0): # Move vertically
    move()
    steps -= 1
  
  if (i < 2): # Turn right on the second iteration
    turn_left()
  else:
    turn_right()
  steps = 2

  while (steps > 0): # Move horizontally
    move()
    steps -= 1
  turn_right()
  steps = 4

  i -= 1 # Decrement

for n in range(0, 2): # Rotate 180 degrees
  turn_left()

steps = 4
while (steps > 0):
  move()
  steps -= 1

#---- end robot movement 

wn.mainloop()
