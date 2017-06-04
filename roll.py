#!/usr/bin/python3

# Callable function for a player's turn

import sqlite3
import random
from main import player1, player2, player3, player4, number_of_players
from main import current_player
from sql import reset_cup, draw, colors_in_hand

# Variables for the Dice
starting_dice = ("Green", "Green", "Green", "Green", "Green", "Green",
                 "Yellow", "Yellow", "Yellow", "Yellow",
                 "Red", "Red", "Red")

# Sides
green = ("Brain", "Brain", "Brain", "Runner", "Runner", "Shotgun")
yellow = ("Brain", "Brain", "Runner", "Runner", "Shotgun", "Shotgun")
red = ("Brain", "Runner", "Runner", "Shotgun", "Shotgun", "Shotgun")


def roll():
    # Variables to keep track of how many Brains/Shotguns/Runners
    # the player has on their current roll
    global brains
    global runners
    global shotguns
    brains = 0
    runners = 0
    shotguns = 0
    hand = colors_in_hand()
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
    #hand = colors_in_hand()
    print("#######")
    print(hand[0])
    print(hand[1])
    print(hand[2])
    print("#######")
    print("")
    #print("On this turn so far you have", brains, "Brains, and", shotguns,
        #"Shotgun blasts")
    print("")
    # for every brain add 1 to brain count
    # for every shotgun add to shotgun count
    # for every runner add to runner count
    """
    Need to figure out why first/second/third is not printing in order
    """
    for i in colors_in_hand():
        if i == "Green":
            print("The first die is Green")
            outcome = random.choice(green)
            print("It rolled a", outcome)
            print("")
            if outcome == "Brain":
                brains = brains + 1
            elif outcome == "Runner":
                runners = runners + 1
            elif outcome == "Shotgun":
                shotguns = shotguns + 1
        elif i == "Yellow":
            print("The second die is Yellow")
            outcome = random.choice(yellow)
            print("It rolled a", outcome)
            print("")
            if outcome == "Brain":
                brains = brains + 1
            elif outcome == "Runner":
                runners = runners + 1
            elif outcome == "Shotgun":
                shotguns = shotguns + 1
        elif i == "Red":
            print("The third die is Red")
            outcome = random.choice(red)
            print("It rolled a", outcome)
            print("")
            if outcome == "Brain":
                brains = brains + 1
            elif outcome == "Runner":
                runners = runners + 1
            elif outcome == "Shotgun":
                shotguns = shotguns + 1
    print("On this turn so far you have", brains, "Brains, and", shotguns,
    "Shotgun blasts")
    # If shotgun count is 3 set all counts back to zero and end turn
    if shotguns > 2:
        print("That's 3 shotgun blats, your turn is over")
    else:
        print("You still don't have 3 shotguns blasts this turn, you can keep",
              "rolling if you would like")



# Elif ask user if they want to keep rolling
# If user wants to keep rolling
#  If runner count is 1 pull 2 dice at random and remove them from cup and let the user know what
#  color dice they picked
#  Elif runner count is 2 pull 1 dice at random and remove it from cup and let the user know what
#  color dice they picked
#  Else reroll the 3 dice already out of the cup
# Else add brain count to user score


roll()
#pick_outcome()
