import turtle
import projectile
import asyncio
import stats as s

class tower:
  def __init__(self, pos=(-100, -100), damage=1, attack_radius=10, proj_speed=5, attack_speed = 0.5):
    self.pos = pos
    self.damage = damage
    self.attack_radius = attack_radius
    self.projectile_speed = proj_speed
    self.attack_speed = attack_speed
    self.active = True

    self.trtl = turtle.Turtle()
    self.trtl.penup()
    self.trtl.speed(0)
    self.trtl.goto(pos[0], pos[1])
  
  def find_closest_enemy(self, enemy_list):    
    # Return if there are no enemies
    if (enemy_list == None or len(enemy_list) == 0):
      return None
    closest_enemy = None
    closest_distance = 10000
    for enemy in enemy_list:
      # Set to closest enemy if its distance is closer
      enemy_distance = enemy.distance_from_player(self)
      if (enemy_distance <= self.attack_radius and enemy_distance <= closest_distance):
        closest_enemy = enemy
        closest_distance = enemy_distance
    
    return closest_enemy

  def act(self):
    if (self.active):
      self.pos = self.trtl.pos()
      self.attack(s.all_enemies)

  async def action_loop(self):
    # Loops while tower is active
    while (self.active):
      self.attack(s.all_enemies)
      await asyncio.sleep(self.attack_speed)

  def attack(self, enemy_list):
    # Attack target
    target = self.find_closest_enemy(enemy_list)
    if (target != None):
      new_projectile = projectile.proj(self, target, self.pos, speed=self.projectile_speed)
      new_projectile.attack()
  
  def enemies_in_range(self, enemy_list):
    if (enemy_list == None):
      return None
    
    in_range_enemies = []
    for enemy in enemy_list:
      if enemy.distance_from_player(self) <= self.attack_radius:
        in_range_enemies.append(enemy)
    
    return in_range_enemies