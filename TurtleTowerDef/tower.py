import turtle
import projectile
import asyncio
import stats as s

class tower:
  def __init__(self, pos=(-100, -100), damage=1, attack_radius=10, proj_speed=5, attack_cooldown = 1, color="black"):
    self.pos = pos
    self.damage = damage
    self.attack_radius = attack_radius
    self.projectile_speed = proj_speed
    self.attack_cooldown = attack_cooldown
    self.active = True

    self.trtl = turtle.Turtle()
    self.trtl.penup()
    self.trtl.speed(0)
    self.trtl.color(color)
    self.trtl.goto(pos[0], pos[1])
    self.cooldown = 0
  
  def find_closest_enemy(self, enemy_list):    
    """
    Return the closest enemy to the tower in enemy_list.
    """
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

  def act(self, writer):
    """
    Update the tower every game loop.
    """
    if (self.active):
      self.pos = self.trtl.pos()
      self.attack(s.all_enemies, writer)
      self.cooldown += 0.25

  def attack(self, enemy_list, writer):
    """
    Attack the closest target in enemy_list if the cooldown is met.
    """
    # Attack target
    if (self.cooldown >= self.attack_cooldown):
      target = self.find_closest_enemy(enemy_list)
      if (target != None):
        new_projectile = projectile.proj(self, target, self.pos, speed=self.projectile_speed)
        new_projectile.attack(writer)

  def enemies_in_range(self, enemy_list):
    """
    Return all of the enemies in the tower's range in enemy_list.
    """
    if (enemy_list == None):
      return None
    
    in_range_enemies = []
    for enemy in enemy_list:
      if enemy.distance_from_player(self) <= self.attack_radius:
        in_range_enemies.append(enemy)
    
    return in_range_enemies