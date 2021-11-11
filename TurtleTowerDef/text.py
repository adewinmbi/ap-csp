import turtle

font_setup = ("Courier", 10, "normal")

def init_writer(field_size, cell_scale, field_offset, color):
  writer = turtle.Turtle()
  writer.penup()
  writer.color(color)
  writer.ht()
  writer.goto((field_size + 2) * 20 * cell_scale - (field_offset), 0)
  writer.pendown()
  return writer

def update_text(trtl, health, money, score):
  trtl.clear()
  trtl.write("Health: " + str(health) + "\n" + "Money: " + str(money) + "\n" + "Score: " + str(score) + "\n", font=font_setup)

def game_ended(trtl, win_lose, score):
  trtl.clear()
  trtl.write("You " +  str(win_lose) + "!\nScore: " + str(score))
