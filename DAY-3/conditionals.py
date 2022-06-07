print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height>= 120:
  print("You can ride the rollercoaster")
else:
  print("You can not ride the rollercoaster")



print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height>= 120:
  print("You can ride the rollercoaster")
  age=int(input("What is your age in years? "))
  if age<12:
      print("You have to pay $5")
  elif age<=18:
      print("You have to pay $7")
  else:
      print("Pay $12")
else:
    print("Sorry your height is short")








# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if number%2==0:
  print("This is an even number")
else:
  print("This is an odd number.")





# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi=weight/(height**2)
nbmi=round(bmi)
if bmi<18.5:
  print(f"Your BMI is {nbmi}, you are underweight.")
elif bmi<25:
  print(f"Your BMI is {nbmi}, you have a normal weight.")
elif bmi<30:
  print(f"Your BMI is {nbmi}, you are slightly overweight.")
elif bmi<35:
  print(f"Your BMI is {nbmi}, you are obese.")
elif bmi>35:
  print(f"Your BMI is {nbmi}, you are clinically obese.")





# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if(year%4==0&(year%100==0|year%400==0)):
  print("Leap year.")
else:
  print("Not leap year.")




print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print("Child tickets are $5.")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7.")
  else:
    bill = 12
    print("Adult tickets are $12.")
  
  wants_photo = input("Do you want a photo taken? Y or N. ")
  if wants_photo == "Y":
    bill += 3
  
  print(f"Your final bill is ${bill}")

else:
  print("Sorry, you have to grow taller before you can ride.")




# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if size=="S":
  bill=15
  if add_pepperoni=="Y":
    bill +=2
elif size=="M":
  bill=20
  if add_pepperoni=="Y":
    bill +=3
elif size=="L":
  bill=25
  if add_pepperoni=="Y":
    bill +=3
    
if extra_cheese=="Y":
  bill+=1
  print(f"Your final bill is: ${bill}")
else:
  print(f"Your final bill is: ${bill}")

  


# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
n1=name1.lower()
t1=n1.count('t')
n2=name2.lower()
t2=n2.count('t')
t=t1+t2
n1=name1.lower()
r1=n1.count('r')
n2=name2.lower()
r2=n2.count('r')
r=r1+r2
n1=name1.lower()
u1=n1.count('u')
n2=name2.lower()
u2=n2.count('u')
u=u1+u2
n1=name1.lower()
e1=n1.count('e')
n2=name2.lower()
e2=n2.count('e')
e=e1+e2
total1=t+r+u+e
n1=name1.lower()
l1=n1.count('l')
n2=name2.lower()
l2=n2.count('l')
l=l1+l2
n1=name1.lower()
o1=n1.count('o')
n2=name2.lower()
o2=n2.count('o')
o=o1+o2
n1=name1.lower()
v1=n1.count('v')
n2=name2.lower()
v2=n2.count('v')
v=v1+v2
total2=l+o+v+e
score=int((f"{total1}"+f"{total2}"))
if(score<10 or score>90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif(score>=40 and score<=50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}")





