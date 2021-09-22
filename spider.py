import turtle as trtl

p = trtl.Turtle()
p.pensize(5)
p.speed(0)

# Draw body
p.pensize(150)
p.circle(60, 360)

# Draw head
p.penup()
p.goto(0, -100)
p.pendown()
p.pensize(50)
p.circle(20, 360)

# Draw legs
legs = 4
legX = -80
legY = -40
legIncrement = 60

p.pensize(10)
p.lt(90)

while legs > 0:
    print("asdasd")
    p.penup()
    p.goto(legX, legY)
    p.pendown()
    p.circle(100, 150)
    p.penup()
    p.rt(150) # Turn right 150 deg
    legY += legIncrement
    legs -= 1

legs = 4
legX = 230
legY = -40

while legs > 0:
    print("00000")
    p.penup()
    p.goto(legX, legY)
    p.pendown()
    p.circle(100, 150)
    p.penup()
    p.rt(150) # Turn right 150 deg
    legY += legIncrement
    legs -= 1

# Draw eyes
p.pencolor("orange")

eyes = 2
eyeX = -10
eyeY = -100

while eyes > 0:
    p.penup()
    p.goto(eyeX, eyeY)
    p.pendown()
    p.circle(5, 360)
    p.penup()
    eyeX += 30
    eyes -= 1

wn = trtl.Screen()
wn.mainloop()
