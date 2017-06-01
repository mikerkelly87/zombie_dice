#!/usr/bin/python3

# Callable function for a player's turn

import sqlite3
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


def roll():
    reset_cup()
    # pull 3 dice at random to roll
    # remove those 3 dice from the cup
    print("Drawing three dice from the cup to roll with")
    draw(3)
    # Let the user know what color dice they picked
    print("You have the following colored dice in your hand")
    colors_in_hand()
    # User rolls
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
