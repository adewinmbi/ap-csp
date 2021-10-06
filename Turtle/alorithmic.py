import turtle as t

painter = t.Turtle()

# Move to x and t coordinates given without drawing a line
def Move(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

# Draw a quad with the specified width, height, and starting position
def DrawQuad(sizeX, sizeY, x, y):
    Move(x, y)
    t.begin_fill
    t.goto(x + sizeX, y)
    t.goto(x + sizeX, y + sizeY)
    t.goto(x, y + sizeY)
    t.goto(x, y)
    t.end_fill

size = 100

def DrawTruck():
    # Calculate sizes based on user-inputted size
    wheelRad = size / 4.2
    bodyWidth = size
    bodyHeight = size / 1.8

    # Draw wheel 1
    Move(-100 + wheelRad, -100)
    
    t.pencolor("black")
    t.circle(wheelRad, 360)

    # Draw wheel 2
    Move(-100 + wheelRad + bodyWidth, -100)
    
    t.circle(wheelRad, 360)

    # Draw main body rectangle
    t.pencolor("red")
    DrawQuad(bodyWidth + (bodyWidth / 3), bodyHeight, -100 + wheelRad - (bodyWidth / 3), -100 + wheelRad)

    # Draw secondary rectangle
    DrawQuad(bodyWidth / 3, bodyHeight / 1.7, -100 + wheelRad + bodyWidth, -100 + wheelRad)

DrawTruck()

wn = t.Screen()
wn.mainloop()



