fruit=['apple','peach','pear']
for item in fruit:
    print(item)
    print(item+'Pie')
    print(fruit)
print(fruit)



# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
s=0
for i in student_heights:
    s+=i
avg_height=s/len(student_heights)
res=round(avg_height)
print(res)



# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
m=student_scores[0]
for s in student_scores:
    if m<s:
        m=s
print(f"The highest score in the class is: {m}")

# from a to less than b but not equal
a=int(input("Starting index"))
b=int(input("End index"))
c=int(input("Difference between two no"))
for number in range(a,b,c):
  print(number)



total=0
for number in range(1,101):
  total+=number
print(total)




#Write your code below this row 👇
for i in range(1,101):
    if (i%3==0 and i%5==0):
        print("FizzBuzz")
    elif i%5==0:
        print("Buzz")
    elif i%3==0:
        print("Fizz")
    else:
        print(f"{i}")

