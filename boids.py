# Implementation of the boids algorithm

import turtle as t
import random

class Boid: # Allows a turtle to store its velocity
    velocityX, velocityY = 0
    turtle = t.Turtle()

painter = t.Turtle()

turtleShapes = ["arrow", "turtle", "circle", "square", "triangle"]
turtleColors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown", "red", "blue", "green", "orange", "purple", "gold"]
boids = []

spawnRange = 100 # Defines the largest distance horizontally and vertically that a turtle can "spawn" from the origin
smoothingFactor = 100 # Smooths movement when boid moves toward center
collisionRange = 5 # Collider radius around each boid

for s in turtleShapes:
    newBoid = Boid()
    boids.append(newBoid)

    newTurtle = t.Turtle(shape = s)
    newColor = random.choice(turtleColors)
    newTurtle.fillcolor(newColor)

    newBoid.turtle = newTurtle


def InitPositions(): # Give each turtle a random starting position (within spawn range)
    for boid in boids:
        boid.turtle.penup()
        boid.turtle.goto(random.randint(-spawnRange, spawnRange))
        boid.turtle.pendown()

def MoveAllBoids():

    # 'v' means velocity
    # 'x' or 'y' represents the x or y component in a velocity vector
    # '1', '2', or '3' defines which vector each component is part of
    vx1, vy1, vx2, vy2, vx3, vy3 = 0

    for boid in boids: # One velocity vector per rule
        vx1, vy1 = RuleFlyTowardsCenter(boid)
        vx2, vy2 = RuleKeepDistance(boid)
        vx3, vy3 = RuleMatchVelocity(boid)

        boid.velocityX = boids.velocityX + vx1 + vx2 + vx3 # Combine newly calculated velocities
        boid.velocityY = boids.velocityY + vy1 + vy2 + vy3
        boid.turtle.goto(boid.turtle.xcor() + boid.velocityX, boid.turtle.ycor() + boid.velocityY) # Move turtle based on velocity

# All rules should return tuplet containing x and y component of velocity
def RuleFlyTowardsCenter(boid):
    totalCenterX, totalCenterY = 0
    percievedCenterX, percievedCenterY = 0 # Center (average position) of all other boids not including itself
    
    for b in boids:
        if (b != boid):
            totalCenterX += b.turtle.xcor()
            totalCenterY += b.turtle.ycor()

    percievedCenterX = totalCenterX / (boids.count() - 1) # Calculate average
    percievedCenterY = totalCenterY / (boids.count() - 1)

    return ((percievedCenterX - boid.turtle.xcor()) / smoothingFactor, (percievedCenterY - boid.turtle.ycor()) / smoothingFactor)

def RuleKeepDistance(boid):
    cx, cy = 0 # Displacement

    for b in boids:
        if (b != boid):
            if (abs(b.turtle.xcor() - boid.turtle.xcor()) < collisionRange):
                print()

def RuleMatchVelocity(boid):
    print()

wn = t.Screen()
wn.mainloop()