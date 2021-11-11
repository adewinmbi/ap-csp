import text

def lose_game(writer, score):
  text.game_ended(writer, "lose", score)
  print("You lost! Score:", score)

def win_game(writer, score):
  text.game_ended(writer, "win", score)
  print("You win! Score:", score)