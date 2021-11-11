import turtle
import math_util as util
import asyncio
import stats as s
import text
import winlose as wl

class enemy:
  def __init__(self, health=10, damage=8, speed=2, pos=(0, 0), money=25):
    self.alive = True
    self.health = health
    self.damage = damage
    self.speed = speed
    self.pos = pos
    self.money = money
    self.current_path_cell = 0

    # Initialize turtle
    trtl = turtle.Turtle()
    trtl.shape("turtle")
    trtl.speed(0)
    trtl.penup()
    trtl.hideturtle()
    self.trtl = trtl

    self.direction = "e"

  def distance_from_player(self, player):
    return util.euclidian_distance(self.pos, player.pos)
  
  async def move(self, path, delay, collision_boundary, writer): # Move to next path cell in list
    await asyncio.sleep(delay)
    self.trtl.showturtle()
    for i in range(len(path)):
      if (self.alive):
        current_coords = self.pos
        self.pos = path[self.current_path_cell]
        nx = self.pos[0] * 20 * 0.5 - 100 # Constants used to avoid having to import
        ny = self.pos[1] * 20 * 0.5 - 100
        angle = util.cardinal_directions[util.get_cardinal_direction(current_coords, (nx, ny))]
        self.trtl.seth(angle)
        self.trtl.goto(nx, ny)
        self.pos = (nx, ny)
        self.current_path_cell += 1
        self.check_collision(collision_boundary, writer)
        await asyncio.sleep(1 / self.speed)

  def check_collision(self, boundary, writer):
    if (self.pos[0] >= boundary): # If the enemy has collided with the fortress
      s.health -= self.damage
      text.update_text(writer, s.health, s.money, s.score)
      self.health = 0
      s.all_enemies.remove(self)

      # Update the enemy list for every tower object
      for t in s.all_towers:
        t.enemy_list = s.all_enemies

      if (s.health <= 0):
        wl.lose_game(writer, s.score)
      elif (len(s.all_enemies) <= 0):
        wl.win_game(writer, s.score)
      
      del self

  def take_damage(self, tower, writer):
    # Subtract damage from health and check if dead
    self.health -= tower.damage
    self.check_dead(writer)
  
  def check_dead(self, writer):
    # Check if health <= 0
    if (self.health <= 0):
      self.die(writer)

  def die(self, writer):
    # Hide the turtle, stop moving, and add money to the player
    text.update_text(writer, s.health, s.money, s.score)
    s.score += 10
    self.alive = False
    self.trtl.hideturtle()
    s.money += self.money
    if (self in s.all_enemies):
      s.all_enemies.remove(self)
      
  def __del__(self):
    self.trtl.ht()
