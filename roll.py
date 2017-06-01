#!/usr/bin/python3

# Callable function for a player's turn

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
    
