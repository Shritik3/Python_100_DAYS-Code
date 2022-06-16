#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
from art import logo
print(logo)
print("Welcome to the number guessing game")
print("I'm thinking of a number between 1 to 100")
no=random.randint(1,101)
user_dif=input("Choose a difficulty.Type 'easy' or 'hard': ")
def compare_no(a):
  if a<no:
    return "Too low."
  elif a>no:
    return "Too High"
  elif a==no:
    return f"You got it,the answer was {a}"
if user_dif=="easy":
  c=10
  bool=True
  while c!=0:
    while bool==True:
      print(f"You have {c} attempts remaining to guess the             number")
      a=int(input("Make a guess: "))
      b=compare_no(a)
      if b==f"You got it,the answer was {a}":
        bool=False
        print(b)
      else:
        c-=1
        print(b)
        print("Guess again.")
elif user_dif=="hard":
  c=5
  bool=True
  while c!=0:
    while bool==True:
      print(f"You have {c} attempts remaining to guess the             number")
      a=int(input("Make a guess: "))
      b=compare_no(a)
      if b==f"You got it,the answer was {a}":
        bool=False
        print(b)
      else:
        c-=1
        print(b)
        print("Guess again.")
        
      

