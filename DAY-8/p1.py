name=input("Enter your name ?\n")
def greet(n):
    print("Hello {n}")
    print("How do you do? {n}")
    print("Isn't the weather nice today?")

greet(name)


# function with more than one keywords
name=input("Enter your name:")
add=input("Enter your address")
def greet_with(n,l):
    print(f"Your name is{n}")
    print(f"Your address is {l}")


greet_with(name,add)
greet_with("Shritik","Agra")

# Keyword Arguments
def greet_with(n,l):
    print(f"Your name is{n}")
    print(f"Your address is {l}")

greet_with(l="Agra",n="Shritik")




#Write your code below this line 👇
import math
def paint_calc(width,cover,height):
  number_of_cans=(height*width)/5
  nc=(int(math.ceil(number_of_cans)))
  print(f"You'll need {nc} cans of paint")






#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)




#Write your code below this line 👇
def prime_checker(number):
  c=0
  for i in range(1,number+1):
    if number%i==0:
      c=c+1
    else:
      c=c
  if c==2:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")





#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



