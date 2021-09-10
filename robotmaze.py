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
robot_image = "robot.gif"
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
wn.bgpic("maze1.png") # other file names should be maze2.png, maze3.png

#---- While loops

# First route
steps = 3
i = 0
while (i < 2): # Outer while loop
  while (steps > 0): # Inner while loop
    move()
    steps -= 1
  turn_right()
  steps = 3
  i += 1

robot.goto(startx, starty) # Reset position

i = 0
steps = 3
while (i < 2): # Outer while loop
  turn_left()
  while (steps > 0): # Inner while loop
    move()
    steps -= 1
  steps = 3
  i += 1
turn_left()
move()

#---- end robot movement 

wn.mainloop()
