# We will write a rock paper scissors game in class - Complete it in this file
import random

#make a function that gets the choices
def get_choices():
    options = ["normal","fire","water","grass","electric","poison","bug","rock","fighting","flying","ground","Ice","Psychic","Ghost","Dragon","steel","Dark","Fairy"]

    Player_choice = input("choose between fire, water, or grass.")
    computer_choice = random.choice(options)
    choices = {"player": Player_choice, "computer":computer_choice}
    return choices
choices = get_choices()
print()
print(choices)
print()
def type_advantages():
    if choices == {"player": "fire", "computer":"normal"}:
        print("You tied")
    elif choices == {"player": "fire", "computer":"water"}:  
        print("You lose")
    elif choices == {"player": "fire", "computer":"grass"}:
        print("You win")
    elif choices == {"player": "fire", "computer":"fire"}:  
        print("You tied")
    elif choices == {"player": "fire", "computer":"electric"}:  
        print("You tied")
    elif choices == {"player": "fire", "computer":"poison"}:  
        print("You tied")
    elif choices == {"player": "fire", "computer":"bug"}:  
        print("You win")
    elif choices == {"player": "fire", "computer":"rock"}:  
        print("You lose")
    elif choices == {"player": "fire", "computer":"fighting"}:  
        print("You tied")
    elif choices == {"player": "fire", "computer":"flying"}:  
        print("You tied")
    elif choices == {"player": "fire", "computer":"ground"}:  
        print("You lose")
    elif choices == {"player": "fire", "computer":"Ice"}:  
        print("You Win")
    elif choices == {"player": "fire", "computer":"Psychic"}:  
        print("You tied")
    elif choices == {"player": "fire", "computer":"Ghost"}:  
        print("You tied")
    elif choices == {"player": "fire", "computer":"Dragon"}:  
        print("You lose")
    elif choices == {"player": "fire", "computer":"Dark"}:  
        print("You tied")
    elif choices == {"player": "fire", "computer":"Steel"}:  
        print("You win")
    elif choices == {"player": "fire", "computer":"Fairy"}:  
        print("You win")

    elif choices == {"player": "water", "computer":"normal"}:
        print("You tied")
    elif choices == {"player": "water", "computer":"water"}:  
        print("You tied")
    elif choices == {"player": "water", "computer":"grass"}:
        print("You lose")
    elif choices == {"player": "water", "computer":"fire"}:  
        print("You win")
    elif choices == {"player": "water", "computer":"electric"}:  
        print("You lose")
    elif choices == {"player": "water", "computer":"poison"}:  
        print("You tied")
    elif choices == {"player": "water", "computer":"bug"}:  
        print("You tied")
    elif choices == {"player": "water", "computer":"rock"}:  
        print("You win")
    elif choices == {"player": "water", "computer":"fighting"}:  
        print("You tied")
    elif choices == {"player": "water", "computer":"flying"}:  
        print("You tied")
    elif choices == {"player": "water", "computer":"ground"}:  
        print("You win")
    elif choices == {"player": "water", "computer":"Ice"}:  
        print("You Win")
    elif choices == {"player": "water", "computer":"Psychic"}:  
        print("You tied")
    elif choices == {"player": "water", "computer":"Ghost"}:  
        print("You tied")
    elif choices == {"player": "water", "computer":"Dragon"}:  
        print("You lose")
    elif choices == {"player": "water", "computer":"Dark"}:  
        print("You tied")
    elif choices == {"player": "water", "computer":"Steel"}:  
        print("You win")
    elif choices == {"player": "water", "computer":"Fairy"}:  
        print("You tied")

    elif choices == {"player": "grass", "computer":"normal"}:
        print("You tied")
    elif choices == {"player": "grass", "computer":"water"}:  
        print("You win")
    elif choices == {"player": "grass", "computer":"grass"}:
        print("You tied")
    elif choices == {"player": "grass", "computer":"fire"}:  
        print("You lose")
    elif choices == {"player": "grass", "computer":"electric"}:  
        print("You win")
    elif choices == {"player": "grass", "computer":"poison"}:  
        print("You lose")
    elif choices == {"player": "grass", "computer":"bug"}:  
        print("You lose")
    elif choices == {"player": "grass", "computer":"rock"}:  
        print("You win")
    elif choices == {"player": "grass", "computer":"fighting"}:  
        print("You tied")
    elif choices == {"player": "grass", "computer":"flying"}:  
        print("You lose")
    elif choices == {"player": "grass", "computer":"ground"}:  
        print("You win")
    elif choices == {"player": "grass", "computer":"Ice"}:  
        print("You lose")
    elif choices == {"player": "grass", "computer":"Psychic"}:  
        print("You tied")
    elif choices == {"player": "grass", "computer":"Ghost"}:  
        print("You tied")
    elif choices == {"player": "grass", "computer":"Dragon"}:  
        print("You lose")
    elif choices == {"player": "grass", "computer":"Dark"}:  
        print("You tied")
    elif choices == {"player": "grass", "computer":"Steel"}:  
        print("You lose")
    elif choices == {"player": "grass", "computer":"Fairy"}:  
        print("You tied")

type_advantages()