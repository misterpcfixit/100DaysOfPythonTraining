############DEBUGGING#####################

# Describe Problem - problem is that range highest is set to 20 so the condition of i equals 20 never happens. range will count from 0 to 19.
# def my_function():
#   for i in range(1, 21):
#     if i == 20:
#       print("You got it")
# my_function()

# # Reproduce the Bug - list index out of range is the error. randint set to 1-6 which the list only has 6 items. this randint range is off by 1 should be randint(0, 5) to account for list starting at 0.
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0 , 5)
# print(dice_imgs[dice_num])

# # Play Computer - there is no 1994 and no outside of range. added elif year >= 1994. and else statement for any others. 
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year >= 1994:
#   print("You are a Gen Z.")
# else:
#   print("Wow you're old.")

# # Fix the Errors -IndentationError needed print to be tabbed. TypeError needs input to be an int. finally print is formatted for fstring but missing f. Also missing else nothing will print if not old enough to drive.
# age = int(input("How old are you?"))
# if age > 18:
#     print(f"You can drive at age {age}.")
# else:
#     print("You need to be 18 to drive.")

# #Print is Your Friend. change print to pages then words per page you see that word per page stays at 0 because of a conditional ==. change to = and it fixes it .
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# #Use a Debugger - in VS code you need to put in a break point if you are debugging with no errors. the issue is the blist append needs to be indented in the loop.
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#     b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])
