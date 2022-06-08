rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
list=[rock,paper,scissors]
your_choice=input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n')
n1=int(your_choice)
a=list[n1]
print(a)

print('Computer chose')
n2=random.randint(0,2)
b=list[n2]
print(b)



if  n2>= 3 or n1 < 0: 
  print("You typed an invalid number, you lose!") 
elif n1 == 0 and n2 == 2:
  print("You win!")
elif n2 == 0 and n1 == 2:
  print("You lose")
elif n2 > n1:
  print("You lose")
elif n1 > n2:
  print("You win!")
elif n2 == n1:
  print("It's a draw")

