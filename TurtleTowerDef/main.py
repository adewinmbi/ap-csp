import turtle
import random
import asyncio
import path as pathmaker
import stats as s
import enemy
import tower
import text
import winlose as wl

wn = turtle.Screen()

# Constants
enemies = 10
field_size = 20
cell_scale = 0.5
field_offset = 100
enemy_spawn_interval = (2, 8) # Min and max possible seconds between each enemy spawn
path = pathmaker.generate_path(field_size)

# Initialize start button turtle
start_button = turtle.Turtle()
start_button.color("green")
start_button.penup()
start_button.shapesize(4)
start_button.goto((field_size + 5) * 20 * cell_scale - (field_offset), -50)

score = s.score
enemies_killed = 0
current_tower = "Standard Tower"

colors = {
  "background" : "#9fe85f",
  "path" : "#ebbd52",
  "enemy" : "#eb4444",
  "fortress" : "#fff154",
  "text" : "#000000"
}

selectable_towers = [
  "Standard Tower", "Sniper Tower"
]

towers = {
  "Cost" : {
    "Standard Tower" : 50,    
    "Sniper Tower" : 100,
  },
  "Projectile_Speed" : {
    "Standard Tower" : 10,
    "Sniper Tower" : 20
  },
  "Attack_Radius" : {
    "Standard Tower" : 50,
    "Sniper Tower" : 100
  },
  "Damage" : {
    "Standard Tower" : 1,
    "Sniper Tower" : 4
  },
  "Cooldown" : {
    "Standard Tower" : 0.5,
    "Sniper Tower" : 2
  },
  "Color" : {
    "Standard Tower" : "purple",
    "Sniper Tower" : "blue"
  }
}

# Write important stats onto the screen
writer = text.init_writer(field_size, cell_scale, field_offset, colors["text"])
text.update_text(writer, s.health, s.money, score)

async def main_loop():
  while (True):
    if (s.all_enemies is []):
      wl.win()
    for tower in s.all_towers:
      tower.act(writer)
    await asyncio.sleep(0.25)

async def spawn_enemies():
  print("Spawning enemies...")
  for i in range(enemies):
    e = enemy.enemy()
    e.trtl.shapesize(cell_scale * 2)
    e.trtl.color(colors["enemy"])
    e.pos = cell_to_world(path[0][0], path[0][1])
    s.all_enemies.append(e)
  
  move_tasks = []
  delay = 0
  boundary = (field_size - 1) * 20 * cell_scale - field_offset
  for e in s.all_enemies:
    move_task = asyncio.create_task(e.move(path, delay, boundary, writer))
    move_tasks.append(move_task)
    delay += random.randint(enemy_spawn_interval[0], enemy_spawn_interval[1])
    
  await asyncio.gather(move_tasks[0], move_tasks[1])

async def main():
  main_loop_task = asyncio.create_task(main_loop())
  spawn_enemies_task = asyncio.create_task(spawn_enemies())
  text.update_text(writer, s.health, s.money, score)

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
    Cost = towers["Cost"][tower_name]
    if s.money >= Cost:
      s.money -= Cost
      text.update_text(writer, s.health, s.money, score)
      new_tower = tower.tower(pos=(mouse_x, mouse_y), damage=towers["Damage"][tower_name], attack_radius=towers["Attack_Radius"][tower_name], proj_speed=towers["Projectile_Speed"][tower_name], attack_cooldown=towers["Cooldown"][tower_name])
      s.all_towers.append(new_tower)

def print_tower_stats():
  print("\nSelectable Towers:")
  for i in range(len(selectable_towers)):
    print(str(i + 1) + "-" + selectable_towers[i])

  print("\nTower stats:")
  for stat in towers.keys():
    print(stat + ": ", end="")
    for curr_tower in towers[stat].keys():
      end_symbol = ("\n" if curr_tower is list(towers[stat].keys())[len(towers[stat]) - 1] else ", ")
      print(curr_tower + "-" + str(towers[stat][curr_tower]), end=end_symbol)

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

  print("Press a number to select a tower, and click to place it on the field.\nClick the green start button when you're done.")
  turtle.onscreenclick(spawn_tower)
  start_button.onclick(start)
  print_tower_stats()

def mouse_inside_field(mouse_x, mouse_y):
  if (mouse_y < - field_offset):
    return False
  if (mouse_y > 20 * cell_scale * (field_size) - field_offset):
    return False
  if (mouse_x < - field_offset or mouse_x > 20 * cell_scale * (field_size) - field_offset):
    return False
  return True

draw_field()

wn.mainloop()
