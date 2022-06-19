import random
from replit import clear
from art import logo
from art import vs
from game_data import data

bool=True
print(logo)
while bool==True:
  
  def more_followers(person1,person2):
    if person1['follower_count']>person2['follower_count']:
      return 'A'
    else:
      return 'B'
  
  n1=random.randint(0,50)
  count=0
  a=data[n1]
  print(f"Compare A: {a['name']}, a {a['description']}, from       {a['country']}")
  print(vs)
  n2=random.randint(0,50)
  b=[]
  b=data[n2]
  print(f"Against B: {b['name']}, a {b['description']}, from       {b['country']}")
  user_choice=input("Who has more followers: Type A or B? ")
  d=more_followers(a,b)
  if user_choice==d:
    count+=1
    print(f"You are right! Current score: {count}")
  else:
    print(f"Sorry that's wrong.Final score: {count}")
    bool=False
  
    
  
  
  
  