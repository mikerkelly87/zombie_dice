#!/usr/bin/python3

# Callable function for a player's turn

import sqlite3
import random
from main import player1, player2, player3, player4, number_of_players, current_player
from sql import reset_cup, draw, colors_in_hand

# Variables for the Dice
starting_dice = ("Green", "Green", "Green", "Green", "Green", "Green",
                 "Yellow", "Yellow", "Yellow", "Yellow",
                 "Red", "Red", "Red")

# Sides
green = ("Brains", "Brains", "Brains", "Runner", "Runner", "Shotgun")
yellow = ("Brains", "Brains", "Runner", "Runner", "Shotgun", "Shotgun")
red = ("Brains", "Runner", "Runner", "Shotgun", "Shotgun", "Shotgun")

# Variables to keep track of how many Brains/Shotguns/Runners
# the player has on their current roll
brains = 0
runners = 0
shotguns = 0

def pick_outcome():
    hand = colors_in_hand()
    # For the 1st die in the user's hand, select
    # the outcome of the roll at random
    if hand[0] == "Green":
        print("The first die is Green")
        print("It rolled as a", random.choice(green))
        print("")
    elif hand[0] == "Yellow":
        print("The first die is Yellow")
        print("It rolled as a", random.choice(yellow))
        print("")
    elif hand[0] == "Red":
        print("The first die is Red")
        print("It rolled as a", random.choice(red))
        print("")
    # For the 2nd die in the user's hand, select
    # the outcome of the roll at random
    if hand[1] == "Green":
        print("The first die is Green")
        print("It rolled as a", random.choice(green))
        print("")
    elif hand[1] == "Yellow":
        print("The first die is Yellow")
        print("It rolled as a", random.choice(yellow))
        print("")
    elif hand[1] == "Red":
        print("The first die is Red")
        print("It rolled as a", random.choice(red))
        print("")
    # For the 3rd die in the user's hand, select
    # the outcome of the roll at random
    if hand[2] == "Green":
        print("The first die is Green")
        print("It rolled as a", random.choice(green))
        print("")
    elif hand[2] == "Yellow":
        print("The first die is Yellow")
        print("It rolled as a", random.choice(yellow))
        print("")
    elif hand[2] == "Red":
        print("The first die is Red")
        print("It rolled as a", random.choice(red))
        print("")


def roll():
    """
    For some reason reset_cup is printing colors, commenting out for now
    while developing but need to come back to it before the final test of
    roll()
    """
    #reset_cup()
    # pull 3 dice at random to roll
    # remove those 3 dice from the cup
    print("")
    print("Drawing three dice from the cup to roll with")
    draw(3)
    print("")
    print("......... 1")
    print("......... 2")
    print("......... 3")
    print("")
    # Let the user know what color dice they picked
    print("You have the following colored dice in your hand:")
    print("")
    hand = colors_in_hand()
    print(hand[0])
    print(hand[1])
    print(hand[2])
    print("")


    """
    This is where I am currently stuck.
    I need to figure out how to pass the (color1, color2, color3) variables
    from the colors_in_hand() function in the sql.py file to this file. At
    that point I can match the color of each die to the corresponding sides
    tuple to get an accurate random roll for each one
    """
# for every brain add 1 to brain count
# for every shotgun add to shotgun count
# for every runner add to runner count
# If shotgun count is 3 set all counts back to zero and end turn
# Elif ask user if they want to keep rolling
# If user wants to keep rolling
#  If runner count is 1 pull 2 dice at random and remove them from cup and let the user know what
#  color dice they picked
#  Elif runner count is 2 pull 1 dice at random and remove it from cup and let the user know what
#  color dice they picked
#  Else reroll the 3 dice already out of the cup
# Else add brain count to user score


roll()
pick_outcome()
