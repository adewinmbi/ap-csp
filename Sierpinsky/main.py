# Draw triangle
# Draw smaller upside down inner triangle
# Position to draw the next triangles
# - Need x starting pos = length / 4
# - Need y starting pos = sqrt(3/2)a

import turtle as t

# Initialization
trtl = t.Turtle()
trtl.speed(0)

# Constants
largeTriLength = 200
depth = 3

# Globals
currentLength = largeTriLength
triangles = 1

def DrawMainTriangle(length): # Begins drawing at bottom left corner
    for i in range(0, 3):
        trtl.forward(largeTriLength)
        trtl.left(120)

def DrawTriangle(length): # Begins at top left corner
    for i in range(0, 3):
        trtl.forward(length)
        trtl.right(120)

# Utilities
def Move(x, y): # Moves turtle without creating path
    trtl.penup()
    trtl.goto(x, y)
    trtl.pendown()

# def HeightFromLength(length): # Calculate height of equilateral triangle
#     height = math.sqrt(3/2) * length
#     return height
    
Move(-(largeTriLength / 2), -(largeTriLength / 2)) # Move to starting position to center large triangle
DrawMainTriangle(largeTriLength)
Move(-largeTriLength / 4, trtl.ycor() + largeTriLength / 2 - largeTriLength / 15)
DrawTriangle((largeTriLength / 2))

iteration = 1

while (depth > 0):
    currentLength /= 4
    tris = triangles
    while (tris > 0):
        Move(iteration + 1)

    triangles = math.pow(triangles, 3)
    depth -= 1
    


wn = t.Screen()
wn.mainloop()