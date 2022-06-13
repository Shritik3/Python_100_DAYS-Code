programming_dictionary = {
  "Bug": "An error in a program that prevents the program from     running as expected.", 
  "Function": "A piece of code that you can easily call over and      over again."
}
print(programming_dictionary["Bug"])
# new entry
programming_dictionary["Loop"]="The action of doing something over and over again."
print(programming_dictionary)

# creating new empty dictionary
empty_dictionary={}
# edit item in dictionary
programming_dictionary["Bug"]="A moth in your computer"
print(programming_dictionary)

for thing in programming_dictionary:
  print(thing)
  print(programming_dictionary[thing])
# wiping out data from dictionary
programming_dictionary={}
print(programming_dictionary)






student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades={}

#TODO-2: Write your code below to add the grades to student_grades.👇
for thing in student_scores:
  if student_scores[thing]>=91 and student_scores[thing]<=100:
    student_grades[thing]="Outstanding"
  elif student_scores[thing]>=81 and student_scores[thing]<=90:
    student_grades[thing]="Exceeds Expectations"
  elif student_scores[thing]>=71 and student_scores[thing]<=80:
    student_grades[thing]="Acceptable"
  elif student_scores[thing]<=70:
    student_grades[thing]="Fail"



    

# 🚨 Don't change the code below 👇
print(student_grades)





#Nesting 
# one key will have only one value so we use lists
capitals = {
  "France": "Paris",
  "Germany": "Berlin",
}
# Nesting lists in lists
["a","b",["c","d"]]

#Nesting a List in a Dictionary

travel_log = {
  "France": ["Paris", "Lille", "Dijon"],
  "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

#Nesting Dictionary in a Dictionary

travel_log = {
  "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
  "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

#Nesting Dictionaries in Lists

travel_log = [
{
  "country": "France", 
  "cities_visited": ["Paris", "Lille", "Dijon"], 
  "total_visits": 12,
},
{
  "country": "Germany",
  "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
  "total_visits": 5,
},
]





travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(c,v,l):
  travel_log1={}
  travel_log1["country"]=c
  travel_log1["visits"]=v
  travel_log1["cities"]=l
  travel_log.append(travel_log1)




#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)



