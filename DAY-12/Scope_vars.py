################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")


# Local scope
def drink_potion():
  potion_strength=2
  print(potion_strength)

drink_potion()
# print(potion_strength)

# Global scope
player_health=10

def game():
  def drink_potion():
    potion_strength=2
    print(player_health)

  drink_potion()
game()
print(player_health)



game_level=3
def create_enemy():
  enemies=["a","b","c"]
  if game_level<5:
    new_enemy=enemies[0]

  print(new_enemy)
# print(new_enemy)

# Modify Global Scope
enemies = 1

def increase_enemies():
  global enemies
  enemies+=1
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")



enemy = 1

def increase_enemies():
  print(f"enemies inside function: {enemy}")
  return enemy + 1

ene=increase_enemies()
print(f"enemies outside function: {ene}")


# Global Constant declare it in upper case
PI=3.15194
URL="https://app.codingrooms.com/management/courses/6387/classes/8480/assignments"