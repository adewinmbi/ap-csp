import asyncio
import turtle
import random
import tracemalloc

import stats as s
import enemy
import tower
import text
import path as pathmaker

tracemalloc.start()

wn = turtle.Screen()

# organize constants later
enemies = 10
field_size = 20
field_offset = 100
cell_scale = 0.5
current_tower = "TowerA"
enemy_spawn_interval = (1, 2) # Min and max possible seconds between each enemy spawn
path = pathmaker.generate_path(field_size)

# path = [(0, 10), (1, 10), (2, 10), (3, 10), (4, 10), # List of coordinates where a path exists
        # (5, 10), (6, 10), (6, 11), (6, 12), (6, 13)]

start_button = turtle.Turtle()
start_button.color("green")
start_button.penup()
start_button.shapesize(4)
start_button.goto(0,-120)

colors = {
  "background" : "#9fe85f",
  "path" : "#ebbd52",
  "tower" : "#969696",
  "enemy" : "#eb4444",
  "fortress" : "#fff154",
  "text" : "#000000"
}

towers = {
  "cost" : {
    "TowerA" : 50    
  },
  "speed" : {
    "TowerA" : 10
  },
  "radius" : {
    "TowerA" : 50
  },
  "damage" : {
    "TowerA" : 1
  },
  "a_speed" : {
    "TowerA" : 0.5
  }
}

score = 0
enemies_killed = 0
health = 50 # Health of the player's fortress

# Write important stats onto the screen
writer = text.init_writer(field_size, cell_scale, field_offset, colors["text"])
text.update_text(writer, health, s.money, score)

async def main_loop():
  while (True):
    for tower in s.all_towers:
      tower.act()
    await asyncio.sleep(1)

async def spawn_enemies():
  print("Spawning enemies...")
  for i in range(enemies):
    e = enemy.enemy()
    e.trtl.shapesize(cell_scale * 2)
    e.trtl.color(colors["enemy"])
    e.pos = cell_to_world(path[0][0], path[0][1])
    s.all_enemies.append(e)
  
  for e in s.all_enemies:
    e.trtl.showturtle()
    await e.move(path) # Begin enemy movement along path
    check_fortress_collision()
    await asyncio.sleep(random.randint(enemy_spawn_interval[0], enemy_spawn_interval[1]))

async def main():
  main_loop_task = asyncio.create_task(main_loop())
  spawn_enemies_task = asyncio.create_task(spawn_enemies())
  text.update_text(writer, health, s.money, score)

  await asyncio.gather(main_loop_task, spawn_enemies_task)

def start(x, y):
  turtle.onscreenclick(None)
  start_button.onclick(None)
  asyncio.run(main())

def cell_to_world(x, y): # Convert cell coordinates to world coordinates
  nx = x * 20 * cell_scale - field_offset
  ny = y * 20 * cell_scale - field_offset
  return (nx, ny)

def spawn_tower(mouse_x, mouse_y):
  if (mouse_inside_field(mouse_x, mouse_y)):
    tower_name = current_tower
    cost = towers["cost"][tower_name]
    if s.money >= cost:
      s.money -= cost
      text.update_text(writer, health, s.money, score)
      new_tower = tower.tower(pos=(mouse_x, mouse_y), damage=towers["damage"][tower_name], attack_radius=towers["radius"][tower_name], proj_speed=towers["speed"][tower_name], attack_speed=towers["a_speed"][tower_name])
      s.all_towers.append(new_tower)

def draw_field():
  print("Drawing playing field...")
  drawer = turtle.Turtle()
  drawer.speed("fastest")
  drawer.shape("square")
  drawer.fillcolor(colors["background"])
  drawer.pencolor("white") # White borders around each cell
  drawer.shapesize(cell_scale)
  drawer.penup()
  
  for x in range(field_size):
    for y in range(field_size):
      drawer.goto(cell_to_world(x, y))

      if (x == field_size - 1):
        drawer.fillcolor(colors["fortress"])
        drawer.stamp()
      else:
        for p in path:
          if p == (x, y):
            drawer.fillcolor(colors["path"])
            drawer.stamp()
            break
          else:
            drawer.fillcolor(colors["background"])
            drawer.stamp()

  print("Click to place a tower on the field.\nClick the green start button when you're done.")
  turtle.onscreenclick(spawn_tower)
  start_button.onclick(start)

def check_fortress_collision():
  global health

  for e in s.all_enemies:
    if (e.pos[1] >= field_size * 20 * cell_scale - field_offset): # If the enemy has collided with the fortress
      health -= e.damage
      text.update_text(writer, health, s.money, score)
      e.health = 0
      s.all_enemies.remove(e)
      del e

      # Update the enemy list for every tower object
      for t in s.all_towers:
        t.enemy_list = s.all_enemies

      if (health <= 0):
        lose_game()
      elif (len(s.all_enemies) <= 0):
        win_game()

def mouse_inside_field(mouse_x, mouse_y):
  if (mouse_y < - field_offset):
    return False
  if (mouse_y > 20 * cell_scale * (field_size) - field_offset):
    return False
  if (mouse_x < - field_offset or mouse_x > 20 * cell_scale * (field_size) - field_offset):
    return False
  return True

# Improve win and lose messages later
def lose_game():
  print("You lost. Score:", score)

def win_game():
  print("You win. Score:", score)

draw_field()

# asyncio.run(main())
# asyncio.run(main_loop())
# asyncio.run(spawn_enemies())

# await asyncio.gather[]

wn.mainloop()