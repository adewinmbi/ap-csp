import turtle
import math_util as util
import math
import asyncio
import stats as s

class proj:
  def __init__(self, parent_tower, target_enemy, pos, shape="arrow", speed=5):
    self.parent_tower = parent_tower
    self.trtl = turtle.Turtle()
    self.trtl.shape(shape)
    self.trtl.shapesize(0.25)
    self.trtl.penup()
    self.trtl.speed(0)
    self.trtl.goto(pos)

    self.speed = speed
    self.target_enemy = target_enemy

    self.is_attacking = True

  def attack(self, writer):
    move_task = asyncio.create_task(self.move_towards_enemy(writer))

    asyncio.gather(move_task)

  async def move_towards_enemy(self, writer):
    while (self.is_attacking and (self.target_enemy in s.all_enemies)):
      current = self.trtl.pos()
      # Detect if the projectile will hit the enemy on the next movement
      if self.speed > util.euclidian_distance(current, self.target_enemy.pos):
        # Destroy projectile and make enemy take damage
        self.is_attacking = False
        self.trtl.hideturtle()
        self.target_enemy.take_damage(self.parent_tower, writer)
      else:
        angle = util.get_pos_angle(util.get_angle_degrees(current, self.target_enemy.pos))
        # Move towards enemy
        self.trtl.setheading(angle)
        self.trtl.forward(self.speed)
      # Wait 0.5 seconds before moving again
      await asyncio.sleep(0.5)
    self.trtl.hideturtle()



