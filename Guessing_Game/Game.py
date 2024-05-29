#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import art
import random
rando_num = randint(1,100)
  
def main():
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
    guess = input("Make a guess: ")
  if guess < rando_num:
    print("Too Low.\nGuess again.")
  elif guess > rando_num:
    print("Too High.\n")
main()
