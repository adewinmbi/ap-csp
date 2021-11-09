import turtle
import math_util as util
import asyncio
import stats as s

class enemy:
  def __init__(self, health=10, damage=5, speed=1, pos=(0, 0), money=25):
    self.alive = True
    self.health = health
    self.damage = damage
    self.speed = speed
    self.pos = pos
    self.money = money
    self.current_path_cell = 0

    # Initialize turtle
    trtl = turtle.Turtle()
    trtl.hideturtle()
    trtl.shape("turtle")
    trtl.speed(0)
    trtl.penup()
    self.trtl = trtl

  def distance_from_player(self, player):
    return util.euclidian_distance(self.pos, player.pos)
  
  async def move(self, path): # Move to next path cell in list
    for i in range(len(path)):
      if (self.alive):
        self.pos = path[self.current_path_cell]
        nx = self.pos[0] * 20 * 0.5 - 100 # Constants used to avoid having to import
        ny = self.pos[1] * 20 * 0.5 - 100
        self.trtl.goto(nx, ny)
        self.pos = (nx, ny)
        self.current_path_cell += 1
        await asyncio.sleep(1 / self.speed)

  def take_damage(self, tower):
    # Subtract damage from health and check if dead
    self.health -= tower.damage
    self.check_dead()
  
  def check_dead(self):
    # Check if health <= 0
    if (self.health <= 0):
      self.die()

  def die(self):
    # Hide the turtle, stop moving, and add money to the player
    self.alive = False
    self.trtl.hideturtle()
    s.money += self.money
    if (self in s.all_enemies):
      s.all_enemies.remove(self)