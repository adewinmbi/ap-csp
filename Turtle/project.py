import turtle as t

painter = t.Turtle()

# Get user input
size = int(input("Truck size: "))
color = input("Truck main color: ")
colorWheel = input("Truck wheel color: ")
posX = int(input("Truck x position: "))
posY = int(input("Truck y position: "))

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

def DrawTruck():
    # Calculate sizes based on user-inputted size
    wheelRad = size / 4.2
    bodyWidth = size
    bodyHeight = size / 1.8

    # Draw wheel 1
    Move(posX + wheelRad, posY)
    
    t.pencolor(colorWheel)
    t.circle(wheelRad, 360)

    # Draw wheel 2
    Move(posX + wheelRad + bodyWidth, posY)
    
    t.circle(wheelRad, 360)

    # Draw main body rectangle
    t.pencolor(color)
    DrawQuad(bodyWidth + (bodyWidth / 3), bodyHeight, posX + wheelRad - (bodyWidth / 3), posY + wheelRad)

    # Draw secondary rectangle
    DrawQuad(bodyWidth / 3, bodyHeight / 1.7, posX + wheelRad + bodyWidth, posY + wheelRad)

DrawTruck()

wn = t.Screen()
wn.mainloop()



