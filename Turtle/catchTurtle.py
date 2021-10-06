#-----import statements-----
import turtle as t
import random


#-----game configuration----
turtleColor = "red"
turtleSize = 5
turtleShape = "turtle"
screenX = 380 # Slightly smaller than actual screen size to prevent turtle from moving to edge
screenY = 280
score = 0
font_setup = ("Arial", 20, "normal")
timer = 30
counter_interval = 1000 # 1 second
timer_up = False
sizes = [0.5, 0.8, 1, 1.3, 1.7, 2, 2.3, 2.5]
colors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown", "red", "blue", "green", "orange", "purple", "gold"]
game_started = False

#-----initialize turtle-----
tri = t.Turtle()
tri.shape(turtleShape)
tri.shapesize(turtleSize)
tri.fillcolor(turtleColor)
tri.penup() # Prevent turtle from leaving a trail
tri.hideturtle()

score_writer = t.Turtle()

counter = t.Turtle()

start_button = t.Turtle()
start_button.shape("triangle")
start_button.fillcolor("green")
start_button.shapesize(5)

#-----game functions--------
def tri_clicked(x, y):
    global game_started
    if (game_started):
        global timer_up
        if (timer_up == False):
            update_score()
            change_position()
            resize_turtle()
            recolor_turtle()
        else:
            tri.hideturtle()


def change_position():
    tri.hideturtle() # Prevent turtle from visibly moving
    new_xpos = random.randint(-screenX, screenX)
    new_ypos = random.randint(-screenY, screenY)
    tri.goto(new_xpos, new_ypos)
    tri.showturtle()

def update_score():
    global score
    score += 1
    score_writer.clear()
    score_writer.write(score, font=font_setup)

def position_score_writer():
    score_writer.penup()
    score_writer.goto(350, 280)
    score_writer.pendown()

def position_countdown():
    counter.penup()
    counter.goto(-350, 280)
    counter.pendown()

def countdown():
    global timer, timer_up, game_started
    counter.clear()
    if (game_started):
        if timer <= 0:
            counter.write("Time's Up!", font=font_setup)
            timer_up = True
            tri.hideturtle()
        else:
            counter.write("Timer: " + str(timer), font=font_setup)
            timer -= 1
            counter.getscreen().ontimer(countdown, counter_interval)

def resize_turtle(): # Shrink the turtle on click
    tri.shapesize(random.choice(sizes))

def recolor_turtle():
    tri.fillcolor(random.choice(colors))
    tri.stamp()
    tri.fillcolor(turtleColor) # Return turtle to original color

def start_game(x, y):
    global game_started
    game_started = True
    start_button.hideturtle()
    tri.showturtle()


#-----events----------------
position_countdown()
position_score_writer()
start_button.onclick(start_game)
tri.onclick(tri_clicked)
wn = t.Screen()
wn.bgcolor("indigo")
wn.ontimer(countdown, counter_interval)
wn.mainloop()