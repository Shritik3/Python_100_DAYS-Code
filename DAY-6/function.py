print('Hello')
num_char=len('Hello')
print(num_char)

def my_function():
  print('Hello')
  print('Bye')

my_function()


# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json
# def turn_around():
#     turn_left()
#     turn_left()
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
# move()
# move()
# move()
# turn_around()
# turn_around()
# move()
# move()
# turn_right()



# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

# def cycle():
#     move()
#     turn_left()
#     move()
#     turn_left()
#     turn_left()
#     turn_left()
#     move()
#     turn_left()
#     turn_left()
#     turn_left()
#     move()
#     turn_left()
# for i in range(0,6):
#     cycle()

# no_of_hurdles=6
# while no_of_hurdles>0:
#     cycle()
#     no_of_hurdles-=1
#     print(no_of_hurdles)



# def cycle():
#     move()
#     turn_left()
#     move()
#     turn_left()
#     turn_left()
#     turn_left()
#     move()
#     turn_left()
#     turn_left()
#     turn_left()
#     move()
#     turn_left()
# while not at_goal():
#         cycle()

# The conditions front_is_clear() or wall_in_front(), at_goal(), and their negation.
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json
# def cycle():
#     turn_left()
#     move()
#     turn_left()
#     turn_left()
#     turn_left()
#     move()
#     turn_left()
#     turn_left()
#     turn_left()
#     move()
    
# while not at_goal():
#     if not front_is_clear():
#         cycle()
#         turn_left()
#     elif not wall_in_front():
#         move()

# http://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json
# def cycle():
#     if not right_is_clear:
#         move()
#         turn_left()
#     else:
#         turn_left()
#         turn_left()
#         turn_left()
#         move()
    
    
# while not at_goal():
#     if not wall_on_right():
#         cycle()
#     elif not wall_in_front():
#         move()
#     elif not front_is_clear():
#         turn_left()
    


# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

# while not at_goal():
#     if not wall_in_front():
#         move()
#     elif not wall_on_right():
#         turn_left()
#         turn_left()
#         turn_left()
#     elif not wall_on_right and not wall_in_front():
#         turn_left()
#         turn_left()
#         turn_left()
#         move()
#     else:
#         turn_left()




