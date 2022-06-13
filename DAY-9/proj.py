from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
def find_highest_bidder(bidders):
  x=0
  h=0
  winner=""
  for people in bidders:
    x=bidders[people]
    if x>h:
      h=x
      winner=people
  print(f"Winner is {winner} with bidding amount ${h}")
bids={}
bool=True
while bool==True:
  name=input("What is your name?: ")
  bid=int(input("What's your bid?: $"))
  bids[name]=bid
  user_choice=input("Are there any other bidder's? Type 'yes' or   'no'.\n")
  if user_choice=='no':
    bool=False
    find_highest_bidder(bids)
  elif user_choice=='yes':
    clear()


    