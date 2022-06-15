from art import logo
from replit import clear
import random

def deal_cards():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  a=random.choice(cards)
  return a
def compare(user_score,comp_score):
  if user_score==comp_score:
    return "PUSH, its a draw"
  elif comp_score==0:
    return "Lose,opponent has a blackjack"
  elif user_score==0:
    return "WIN with a blackjack"
  elif user_score>21:
    return "You went over, you lose"
  elif comp_score>21:
    return "Computer busts,you win"
  elif user_score>comp_score:
    return "You win"
  else:
    return "You lose"
def play_game():  
  print(logo)
  user=[]
  computer=[]
  game_over=False
  for _ in range(2):
    user.append(deal_cards())
    computer.append(deal_cards())
    
  def cal_score(list):
    if sum(list)==21 and len(list)==2:
      return 0
    if 11 in list and sum(list)>21:
      list.remove(11)
      list.append(1)
    return sum(list)
  
  while not game_over:
    user_score=cal_score(user)
    comp_score=cal_score(computer)
    print(f"Your cards {user} with a score of {user_score}")
    print(f"Computer's first card is {computer[0]}")
    if user_score==0 or comp_score==0 or user_score>21:
      game_over=True
    else:
      user_choice=input("Type 'y' to get new card or type 'n' to       pass: ")
      if user_choice=='y':
        user.append(deal_cards())
      else:
        game_over=True
  while comp_score!=0 and comp_score<17:
    computer.append(deal_cards())
    comp_score=cal_score(computer)
  print(f"Your final deck {user}, and final score is {user_score}")
  print(f"Compute final deck {computer}, and its final score is {comp_score}")
  print(compare(user_score,comp_score))
while input("Type 'y' to play a game of blackjack, 'n' to quit")=='y':
  clear()
  play_game()
  