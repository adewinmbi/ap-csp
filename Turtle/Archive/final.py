# Turtle bounces off boundaries
# Stamp at angle changes

import turtle as t
import random

painter = t.Turtle()

turtleShapes = ["arrow", "turtle", "circle", "square", "triangle"]
turtleColors = ["red", "blue", "green", "orange", "purple", "gold", "darkred", "darkblue", "lime", "salmon", "indigo", "brown"]

speed = 10 # Space between each step
boundaryX = 100
boundaryY = 100
currentAngle = 0

# Set turtle initial position and rotation
t.setheading(20)
currentAngle = 20

def RandomizeVisual(): # Randomize the shape, color, and line thickness,
    t.shape(random.choice(turtleShapes))
    t.pencolor(random.choice(turtleColors))
    t.fillcolor(random.choice(turtleColors))
    t.pensize(random.randint(5, 10))
    t.stamp()

def CalculateNewAngleUp(wallAngle, curAng): # Wall angle should be the normal of the wall that is collided with
    newAngle = wallAngle - curAng
    t.setheading(newAngle)
    return newAngle

def CalculateNewAngleDown(wallAngle, curAng):
    newAngle = wallAngle + curAng
    t.setheading(newAngle)
    return newAngle

def CalculateNewAngle(wallAngle, curAng):
    if (curAng >= 180 or curAng <= 0): # If turtle is moving downward when collision occurs
        currentAngle = CalculateNewAngleDown(-wallAngle, curAng)
    else:
        currentAngle = CalculateNewAngleUp(wallAngle, curAng)

turnAngle = 10
angleIncrement = 5

while True: # Main loop
    t.forward(speed)

    if (t.xcor() >= boundaryX): # Collision with right wall
        t.left(turnAngle)
        t.forward(speed)
        turnAngle += angleIncrement
        RandomizeVisual()

    elif (t.xcor() <= -boundaryX): # Collision with left wall
        t.left(turnAngle)
        t.forward(speed)
        turnAngle += angleIncrement
        RandomizeVisual()

    elif (t.ycor() <= -boundaryY): # Collision with bottom wall
        t.left(turnAngle)
        t.forward(speed)
        turnAngle += angleIncrement
        RandomizeVisual()

    elif (t.ycor() >= boundaryY): # Collision with top wall
        t.left(turnAngle)
        t.forward(speed)
        turnAngle += angleIncrement
        RandomizeVisual()

    # if (currentAngle >= 360):
    #     currentAngle = 360 - currentAngle

    # if (currentAngle <= 0):
    #     currentAngle = 360 + currentAngle

    # if (t.xcor() >= boundaryX): # Collision with right wall
    #     if (currentAngle >= 180 or currentAngle <= 0): # If turtle is moving downward when collision occurs
    #         currentAngle = CalculateNewAngleDown(-180, currentAngle)
    #     else:
    #         currentAngle = CalculateNewAngleUp(180, currentAngle)

    # elif (t.xcor() <= -boundaryX): # Collision with left wall
    #     if (currentAngle >= 180 or currentAngle <= 0): # If turtle is moving downward when collision occurs
    #         currentAngle = CalculateNewAngleDown(0, currentAngle)
    #     else:
    #         currentAngle = CalculateNewAngleUp(0, currentAngle)

    # elif (t.ycor() <= -boundaryY): # Collision with bottom wall
    #     if (currentAngle >= 180 or currentAngle <= 0): # If turtle is moving downward when collision occurs
    #         currentAngle = CalculateNewAngleDown(-270, currentAngle)
    #     else:
    #         currentAngle = CalculateNewAngleUp(270, currentAngle)

    # elif (t.ycor() >= boundaryY): # Collision with top wall
    #     if (currentAngle >= 180 or currentAngle <= 0): # If turtle is moving downward when collision occurs
    #         currentAngle = CalculateNewAngleDown(-90, currentAngle)
    #     else:
    #         currentAngle = CalculateNewAngleUp(90, currentAngle)

wn = t.Screen()
wn.mainloop()