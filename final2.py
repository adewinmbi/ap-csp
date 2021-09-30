import turtle as t
painter = t.Turtle()

turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle"]
turtles = []

totalTurtles = 20
startIncrement = 5 # Space between the beginning position of each turtle

while (totalTurtles > 0):
    totalTurtles -= 1

wn = t.Screen()
wn.mainloop()