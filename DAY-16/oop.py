# import another_module
# print(another_module.another_variable)
# # from turtle import Turtle
# import turtle
#
# timmy=turtle.Turtle()
# my_screen=turtle.Screen()
# # print(timmy)
# print(my_screen.canvheight)
# timmy.shape("turtle")
# timmy.color("cyan")
# timmy.forward(100)
# my_screen.exitonclick()
# print("|Pokemon name|Type|")
from prettytable import PrettyTable
table = PrettyTable()

table.add_column("Name", ["Shritik", "Reyansh"])
table.add_column("LastName", ["Raj", "Gaumat"])
table.align="l"
print(table)



