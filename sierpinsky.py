# Use of a recursive algorithm to draw the self-similar Sierpinski Triangle

import turtle as t

# Initialization
trtl = t.Turtle()
trtl.speed(0)

# Constants
colors = ["violet", "white", "green", "red", "blue"]
main_tri_vertices = [[-200, -100], [0, 200], [200, -100]]
depth = 4 # Number of recursions / number of different triangle sizes

# Utilities
def mid_point(point1, point2): # Return a tuple containing the x and y coordinates for the midpoint of two points
    return ((point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2)

def move_to(pos_x, pos_y): # Move to given position without drawing a path
    t.penup()
    t.goto(pos_x, pos_y)
    t.pendown()

# Functions
def draw_triangle(vertices, color): # Draw triangle with vertices at the points provided in a 2D array, in the color provided
    t.fillcolor(color)
    move_to(vertices[0][0], vertices[0][1])
    t.begin_fill()
    t.goto(vertices[1][0],vertices[1][1]) # Go to each vertex of the triangle
    t.goto(vertices[2][0],vertices[2][1])
    t.goto(vertices[0][0],vertices[0][1])
    t.end_fill()

def draw_structure(vertices, depth): # Recursively draw triangles with given vertex positions and incrementing colors
    draw_triangle(vertices, colors[depth])
    if depth > 0:
        draw_structure([vertices[0], mid_point(vertices[0], vertices[1]), mid_point(vertices[0], vertices[2])], depth - 1)
        draw_structure([vertices[1], mid_point(vertices[0], vertices[1]), mid_point(vertices[1], vertices[2])], depth - 1)
        draw_structure([vertices[2], mid_point(vertices[2], vertices[1]), mid_point(vertices[0], vertices[2])], depth - 1)

# Main function call
draw_structure(main_tri_vertices, depth)

wn = t.Screen()
wn.mainloop()