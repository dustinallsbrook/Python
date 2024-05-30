import art
import game_data
from random import randint
import os
high_score = 0

def main():
  print(f"{art.logo}\n")
  game()
  
def game():
  celeb_list = []
  for i in range(2):
    celeb_list.append(randint(0,len(game_data.data)-1))
  win_scenario = True
  score = 0
  while win_scenario != False:
    global high_score
    celeb_a = game_data.data[celeb_list[0]]
    celeb_b = game_data.data[celeb_list[1]]
    print(f"Compare A: {celeb_a['name']}, {celeb_a['description']}, {celeb_a['country']}")
    print(f"{art.vs}\n")
    print(f"Against B: {celeb_b['name']}, {celeb_b['description']}, {celeb_b['country']}")
    # print(f"A: {celeb_a['follower_count']} B: {celeb_b['follower_count']}")
    guess = input("\nWho has more followers? 'A' or 'B'?: ").lower()
    print(guess)
    while guess != 'a' and guess != 'b':
      guess = input("Not 'A' or 'B'. Try again.").lower()
    if calcu(guess,celeb_list,celeb_a,celeb_b,win_scenario) == False:
      if score > high_score:
        high_score = score
      win_scenario = False
      os.system('clear')
      print(art.logo)
      print(f"Wrong. Your score is {score}. Current high score is high score is {high_score}.")
    else:
      score += 1
      os.system('clear')
      print(art.logo)
      print(f"You're right! Current score is {score}.")
  keep_playing = input("Do you want to keep playing? 'Y' or 'N': ").lower()
  while keep_playing != 'y' and keep_playing != 'n':
    keep_playing = input("Not 'Y' or 'N'. Try again.: ")
  if keep_playing == 'y':
    os.system('clear')
    main()
  else:
    os.system('clear')
    exit()

def calcu(guess,celeb_list,celeb_a,celeb_b,win_scenario):
  #print(guess)
  if int(celeb_a['follower_count']) > int(celeb_b['follower_count']):
    higher_celeb='a'
  else:
    higher_celeb='b'
  celeb_list[0] = celeb_list[1]
  celeb_list[1] = randint(0,len(game_data.data)-1)
  #print(f"The higher celeb is {higher_celeb}")
  if guess == higher_celeb:
    return celeb_list
  else:
    win_scenario = False
    return win_scenario

main()
