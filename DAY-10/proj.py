# Calculator
from art import logo
def add(n1,n2):
  return n1+n2
def subtract(n1,n2):
  return n1-n2
def multiply(n1,n2):
  return n1*n2
def divide(n1,n2):
  return n1/n2
choice={"+":add,"-":subtract,"*":multiply,"/":divide}
def calculator():
  print(logo)
  n1=float(input("First number: "))
  for thing in choice:
    print(thing)
  bool=True
  while bool==True:
    op_n=input("Choose an operation:  ")
    n3=float(input("Next number: "))
    cfunction=choice[op_n]
    ans=cfunction(n1,n3)
    print(f"{n1} {op_n} {n3} = {ans}")
    user_choice=input(f"Type 'y' to continue calculating with        {ans}, or type 'n' to start a new calculation: \n")
    if user_choice=='y':
      n1=ans
    elif user_choice=='n':
      bool=False
      calculator()

    
calculator()
    