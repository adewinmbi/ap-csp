# Implementation based on the boids algorithm

import turtle as t
import random
painter = t.Turtle()

turtleShapes = ["arrow", "turtle", "circle", "square", "triangle"]
turtleColors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown", "red", "blue", "green", "orange", "purple", "gold"]
turtles = []

totalTurtles = turtleShapes.count()

spawnRange = 100 # Negative spawnRange defines the lower and leftmost boundaries, while positive spawnRange defines the upper and rightmost boundaries

for s in turtleShapes:
    newTurtle = t.Turtle(shape = s)
    turtles.append(newTurtle)
    turtles.penup()
    newColor = random.choice(turtleColors)
    newTurtle.fillcolor(newColor)
    newTurtle.goto(-spawnRange, spawnRange)

wn = t.Screen()
wn.mainloop()