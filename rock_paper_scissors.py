# We will write a rock paper scissors game in class - Complete it in this file
import random

Player_choice = "normal"
computer_choice = "paper"

#make a function that gets the choices
def get_choices():
    options = ['fire', 'water', 'grass']

    Player_choice = input("choose between fire, water, or grass. ")
    computer_choice = random.choice(options)
    choices = {"player": Player_choice, "computer":computer_choice}

    return choices

choices = get_choices()
print()
print(choices)
print()
if "Player" == "fire":
    if "computer" == 'water':
        print("you lose")