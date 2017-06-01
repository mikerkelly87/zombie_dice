#!/usr/bin/python3

# Callable function for a player's turn

import sqlite3
from main import player1, player2, player3, player4, number_of_players, current_player
from sql import reset_cup

# Variables for the Dice
starting_dice = ("Green", "Green", "Green", "Green", "Green", "Green",
                 "Yellow", "Yellow", "Yellow", "Yellow",
                 "Red", "Red", "Red")

# Sides
green = ("Brains", "Brains", "Brains", "Runner", "Runner", "Shotgun")
yellow = ("Brains", "Brains", "Runner", "Runner", "Shotgun", "Shotgun")
red = ("Brains", "Runner", "Runner", "Shotgun", "Shotgun", "Shotgun")


def roll(player):
    reset_cup()

# pull 3 at random to roll
# Let the user know what color dice they picked
# remove those 3 dice from the cup
# User rolls
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


