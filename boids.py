# Implementation of the boids algorithm using the turtle library

import turtle as t
import random

class Boid: # Allows a turtle to store its velocity
    velocityX, velocityY = 0, 0
    turtle = t.Turtle()

painter = t.Turtle()

turtleShapes = ["arrow", "turtle", "circle", "square", "triangle", "arrow", "turtle", "circle", "square", "triangle"]
turtleColors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown", "red", "blue", "green", "orange", "purple", "gold"]
boids = []

# ============= CONSTANTS =============
screenBoundaries = 300 # Prevents movement off-screen
spawnRange = 100 # Defines the largest distance horizontally and vertically that a turtle can "spawn" from the origin
collisionRange = 12 # Collider radius around each boid
smoothness = 10 # Smooths movment
velChangeSmoothness = 8 # Smooths change between velocities
edgeBounceSmoothness = 5 # Smooths movement away from screen boundaries
maxVelocity = 30

for s in turtleShapes: # Create boids
    newBoid = Boid()
    boids.append(newBoid)

    newTurtle = t.Turtle(shape = s)
    newColor = random.choice(turtleColors) # Randomize colors
    newTurtle.fillcolor(newColor)
    newTurtle.pencolor(newColor)
    
    newTurtle.shapesize(random.uniform(0.3, 1.3)) # Randomize sizes
    newTurtle.pensize(3)

    newBoid.turtle = newTurtle


def InitPositions(): # Give each turtle a random starting position (within spawn range)
    for boid in boids:
        boid.turtle.penup()
        boid.turtle.goto(random.randint(-spawnRange, spawnRange), random.randint(-spawnRange, spawnRange))
        boid.turtle.pendown()

def MoveAllBoids():

    # Three two-component (x & y) velocity vectors with components defined seperately
    vx1, vy1, vx2, vy2, vx3, vy3, vx4, vy4 = 0, 0, 0, 0, 0, 0, 0, 0

    for boid in boids: # One velocity vector per rule
        vx1, vy1 = RuleFlyTowardsCenter(boid)
        vx2, vy2 = RuleKeepDistance(boid)
        vx3, vy3 = RuleMatchVelocity(boid)
        vx4, vy4 = RuleBoundPosition(boid)

        boid.velocityX = max(-maxVelocity, min(boid.velocityX + vx1 + vx2 + vx3 + vx4, maxVelocity)) # Combine newly calculated velocities; Clamp between max and min velocity
        boid.velocityY = max(-maxVelocity, min(boid.velocityY + vy1 + vy2 + vy3 + vy4, maxVelocity))
        boid.turtle.goto(boid.turtle.xcor() + boid.velocityX, boid.turtle.ycor() + boid.velocityY) # Move turtle based on velocity


def RuleFlyTowardsCenter(boid): # Fly towards center of all other boids
    totalCenterX, totalCenterY = 0, 0
    percievedCenterX, percievedCenterY = 0, 0 # Center (average position) of all other boids not including itself
    
    for b in boids:
        if (b != boid):
            totalCenterX += b.turtle.xcor()
            totalCenterY += b.turtle.ycor()

    percievedCenterX = totalCenterX / (len(boids) - 1) # Calculate average
    percievedCenterY = totalCenterY / (len(boids) - 1)

    return ((percievedCenterX - boid.turtle.xcor()) / smoothness, (percievedCenterY - boid.turtle.ycor()) / smoothness)


def RuleKeepDistance(boid): # Prevent collisions with other boids
    cx, cy = 0, 0 # Displacement

    for b in boids:
        if (b != boid):
            diffX = b.turtle.xcor() - boid.turtle.xcor()
            diffY = b.turtle.ycor() - boid.turtle.ycor()
            if (abs(diffX) < collisionRange): # If collision happens
                if (abs(diffY) < collisionRange):
                    cx = cx - (diffX) # Calculate necessary displacement
                    cy = cy - (diffY)

    return (cx, cy)


def RuleMatchVelocity(boid): # Approach a velocity similar to all other boids
    totalVelX, totalVelY = 0, 0
    percievedVelX, percievedVelY = 0, 0 # Center (average position) of all other boids not including itself
    
    for b in boids:
        if (b != boid):
            totalVelX += b.velocityX
            totalVelY += b.velocityY

    percievedVelX = totalVelX / (len(boids) - 1) # Calculate average
    percievedVelY = totalVelY / (len(boids) - 1)

    return ((percievedVelX - boid.velocityX) / smoothness, (percievedVelY - boid.velocityY) / smoothness)

def RuleBoundPosition(boid): # Prevents boids from leaving screen boundaries
    vx, vy = 0, 0

    if (boid.turtle.xcor() < -screenBoundaries): # Check if boid is beyond boundary
        vx = edgeBounceSmoothness # Adjust velocity to bring boid within boundary
    elif (boid.turtle.xcor() > screenBoundaries):
        vx = -edgeBounceSmoothness

    if (boid.turtle.ycor() < -screenBoundaries):
        vy = edgeBounceSmoothness
    if (boid.turtle.ycor() > screenBoundaries):
        vy = -edgeBounceSmoothness
    
    return vx, vy

# ============= MAIN LOOP =============
InitPositions()

while (True):
    MoveAllBoids()

wn = t.Screen()
wn.mainloop()