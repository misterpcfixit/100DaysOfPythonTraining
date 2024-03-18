# importing module random, ascii art from file and data structure from file. data structure is list with dictionary's
# inside. Dictionary keys are name, follower_count, description, and country
import random
import os
from art import hl, vs
from hl_data import data


# Choices 1 and 2 from list at random
def choice_a():
    choice = data[random.randint(0, 49)]
    return choice


def choice_b():
    choice = data[random.randint(0, 49)]
    while choice == choice1:
        choice = data[random.randint(0, 49)]
    return choice


def game():
    print(f"Compare A: {choice1['name']}, a {choice1['description']}, from {choice1['country']}")
    print(vs)
    print(f"Against B: {choice2['name']}, a {choice2['description']}, from {choice2['country']}")
    ask = input("Who has more followers? Type 'A' or 'B': ")
    return ask


def compare():
    if choice1['follower_count'] > choice2['follower_count']:
        c_answer = "a"
    else:
        c_answer = "b"
    return c_answer


# Picking choice 1 and 2
choice1 = choice_a()
choice2 = choice_b()

# variables to track score, question, and correct answer. 
points = 0

# Running the game
print(hl)
ques = game()
answer = compare()

# Check conditions for game
while ques.lower() == answer:
    points += 1
    os.system('cls||clear')
    choice1 = choice2
    choice2 = choice_b()
    print(hl)
    print(f"Correct, you have {points} points.")
    ques = game()
    answer = compare()
else:
    print(f"Game over. Final score was {points}")
