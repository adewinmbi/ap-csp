# a123_apple_avalanche - Brianna Adewinmbi and Kyle Huang 
import turtle
import random
import string

#-----setup-----
apple_image = "res/apple.gif" # Store the file name of your shape

wn = turtle.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.bgpic("res/background.gif")

ground_height = -150

apple = turtle.Turtle()
active_apple = apple
apple.color("white")

alphabet = list(string.ascii_lowercase)
current_letter = alphabet.pop(random.randint(0, len(alphabet)))

#-----functions----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple():
  active_apple.shape(apple_image)
  wn.update()
  wn.tracer(False)
  active_apple.penup()
  active_apple.speed(0)
  active_apple.goto(active_apple.xcor() - 18, active_apple.ycor() - 40)
  print(current_letter)  
  active_apple.write(current_letter, font=("Helvetica", 50, "normal"))
  active_apple.goto(active_apple.xcor() + 18, active_apple.ycor() + 40)
  active_apple.speed(1)
  active_apple.clear()
  wn.tracer(True)

def drop_apple():
  active_apple.goto(active_apple.xcor(), ground_height)
  active_apple.hideturtle()

#-----function calls-----
draw_apple()

wn.onkeypress(drop_apple, current_letter)

wn.listen()

wn.mainloop()