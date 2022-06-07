from signal import pthread_sigmask


3+5
7-4
3*2
print(type(6/3))
# ** raise to the power
print(2**2)
# PEMDAS
# ()
# **
# * /
# + -


#BMI calculator
# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
a=float(height)
b=float(weight)
bmi=b/(a*a)
print(int(bmi))

# division gives floating point number as result

print(round(2.87983473748))
print(round(2.2847982374823,2))
# floor division
print(8//3)




# f-String no need of conversion for printing
score=0
height=1.8
isWinning=True
print(f"your score is {score},your height is {height}, you are winning {isWinning}")


# Life in weeks
# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
total_days=90*365
total_weeks=90*52
total_months=90*12
a=int(age)
days=a*365
weeks=a*52
months=a*12
days_left=total_days-days
weeks_left=total_weeks-weeks
months_left=total_months-months
print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")





# DAY-2 Final project
#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")
a=input("What was the total bill? $")
b=input("How much tip would you like to give? 10, 12, or 15? ")
c=input("How many people to split the bill? ")
x=float(a)
y=int(b)
z=int(c)
res=(x/z)*(1+(y/100))
print(f"Each person should pay: ${round(res,2)}")



