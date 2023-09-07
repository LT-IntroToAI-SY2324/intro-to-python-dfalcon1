# We will write a rock paper scissors game in class - Complete it in this file
import random

Player_choice = "normal"
computer_choice = "paper"

#make a function that gets the choices
def get_choices():
    options = ["fire","water","grass"]

    Player_choice = input("choose between fire, water, or grass.")
    computer_choice = random.choice(options)
    choices = {"player": Player_choice, "computer":computer_choice}
    return choices

choices = get_choices()
print()
print(choices)
print()
def type_advantages():
    if choices == {"player": "fire", "computer":"water"}:
        print("You Lose")
    elif choices == {"player": "fire", "computer":"grass"}:
        print("You win")
    elif choices == {"player": "fire", "computer":"fire"}:
        
        print("You tied")
     if choices == {"player": "water", "computer":"water"}:
        print("You tied")
    elif choices == {"player": "water", "computer":"grass"}:
        print("You Lose")
    elif choices == {"player": "water", "computer":"fire"}:
        print("You win")
        