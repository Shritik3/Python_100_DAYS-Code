#String
print("HEllo"[4])
print("123"+"783")

#Integer
print(123+345)
#comma replaced by _ it is removed by python only for human understanding of large numbers
1_234_567_890

two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

a=two_digit_number[0]
b=two_digit_number[1]
sum=int(a)+int(b)
print(sum)


#Float
3.141598

#Boolean
True
False

#we can not concatenate strings with integers
num_char=len(input("what is your  name?"))
# print("your name has"+num_char+"character.")
print(type(num_char))
new_num_char=str(num_char)
# now all have same data type as string in the print 
print("your name has"+new_num_char+"character.")

print(70+float("100.5"))
# 170.5
print(str(70)+str(100))
# 70100

 
