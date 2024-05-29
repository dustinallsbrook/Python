import art
import random
RANDO_NUM = 0
  
def main():
  global RANDO_NUM
  RANDO_NUM = random.randint(1,100)
  print(RANDO_NUM)
  print(art.logo)
  print("I'm thinking of a number between 1 and 100")
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
  return game_time(difficulty)

def game_time(diffculty):
  attempts = 0
  if diffculty == 'hard':
    attempts = 5
  else:
    attempts = 10
  return play_time(attempts)

def play_time(attempts):
  guess = 0
  while attempts > 0:
    guess = int(input("Make a guess: "))
    if guess < RANDO_NUM:
      print("Too Low.\nGuess again.")
    elif guess > RANDO_NUM:
      print("Too High.\nGuess again.")
    else:
      print(art.win_art)
      new_game()
    attempts -= 1
    print(f"You have {attempts} remaining to guess the number.")
  print(art.lose_art)
  new_game()

def new_game():
  if input("Play again? 'y' or 'n': ") == 'y':
    main()
  else:
    exit()
main()
