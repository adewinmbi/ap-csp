#   a118_turtles_in_traffic.py
#   Move turtles horizontally and vertically across screen.
#   Stopping turtles when they collide.
import turtle as trtl

# create two empty lists of turtles, adding to them later
horiz_turtles = []
vert_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle"]
horiz_colors = ["red", "blue", "green", "orange", "purple", "gold"]
vert_colors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown"]

tloc = 50
for s in turtle_shapes:

    ht = trtl.Turtle(shape=s)
    horiz_turtles.append(ht)
    ht.penup()
    new_color = horiz_colors.pop()
    ht.fillcolor(new_color)
    ht.goto(-350, tloc)
    ht.setheading(0)

    vt = trtl.Turtle(shape=s)
    vert_turtles.append(vt)
    vt.penup()
    new_color = vert_colors.pop()
    vt.fillcolor(new_color)
    vt.goto( -tloc, 350)
    vt.setheading(270)
  
    tloc += 50

speed = 3
steps = 0
collisionShape = "classic"
collisionColor = "grey"

while steps < 50:
    if (speed >= 10): # Reset speed if it passes max
        speed = 3

    for ht in horiz_turtles: # Iterate through turtle lists
        for vt in vert_turtles:

            vt.forward(speed) # Move turtles forwards
            ht.forward(speed)
                
            if vt.ycor() <= 0:
                vt.fillcolor(collisionColor) # Disable turtle
                vt.shape(collisionShape)
                vert_turtles.remove(vt)

            if (abs(ht.xcor() - vt.xcor()) < 20): # Check for collisions
                if (abs(ht.ycor() - vt.ycor()) < 20):
                    oldVertColor = vt.fillcolor() # Store color and shape values
                    oldVertShape = vt.shape()
                    vt.fillcolor(collisionColor) # Disable turtle
                    vt.shape(collisionShape)
                    vt.forward(-30) # Reverse 30 units after collision
                    vt.shape(oldVertShape)
                    vt.fillcolor(oldVertColor)

                    oldHoriColor = ht.fillcolor() # Repeat for horizontal turtles
                    oldHoriShape = ht.shape()
                    ht.fillcolor(collisionColor)
                    ht.shape(collisionShape)
                    ht.forward(-30)
                    ht.shape(oldHoriShape)
                    ht.fillcolor(oldHoriColor)
                    
        ht.forward(speed)
        if ht.xcor() >= 150: # Prevent turtles from moving offscreen
            ht.fillcolor(collisionColor)
            ht.shape(collisionShape)
            horiz_turtles.remove(ht)
    speed += 1 # Increase speed
    steps += 1

wn = trtl.Screen()
wn.mainloop()
