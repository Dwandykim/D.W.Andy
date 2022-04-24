# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 11:39:44 2022

@author: dwandy
"""

""" Keep track of when user wins or computer wins """

import random

user_wins = 0
computer_wins = 0

options = ['rock', 'paper', 'scissors']

while True:
    user_input = input("Enter Rock/Paper/Scissors or Q to quit the game: ").lower()
    
    if user_input == 'q':
        break
    if user_input not in options:
        continue
    
    random_number = random.randint(0,2)
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")
    
    if user_input == 'rock' and computer_pick == 'scissors':
        user_wins += 1
        print("You won")
    elif user_input == 'paper' and computer_pick == 'rock':
        user_wins += 1
        print("You won")
    elif user_input == 'scissors' and computer_pick == 'paper':
        user_wins += 1
        print("You won")
    else:
        computer_wins += 1
        print("You lost")

print("You won", user_wins, "times.")
print("You lost", computer_wins, "times.")
