#!/usr/bin/python3

# Callable function for a player's turn

import sqlite3
import random
import time
#from main import player1, player2, player3, player4, number_of_players
#from main import current_player
from sql import reset_cup, draw, colors_in_hand, add_score, create_hand_table
from sql import create_side_table, move_green, move_yellow, move_red

# Variables for the Dice
starting_dice = ("Green", "Green", "Green", "Green", "Green", "Green",
                 "Yellow", "Yellow", "Yellow", "Yellow",
                 "Red", "Red", "Red")

# Sides of each color die
green = ("Brain", "Brain", "Brain", "Runner", "Runner", "Shotgun")
yellow = ("Brain", "Brain", "Runner", "Runner", "Shotgun", "Shotgun")
red = ("Brain", "Runner", "Runner", "Shotgun", "Shotgun", "Shotgun")


# Roll function for a player's turn
def roll(player_name):
    # Variables to keep track of how many Brains/Shotguns/Runners
    # the player has on their current roll
    global brains
    global runners
    global shotguns
    brains = 0
    runners = 0
    shotguns = 0
    # Put all the dice back in the cup
    reset_cup()
    # Create the hand table
    create_hand_table()
    # Create the side table
    create_side_table()
    print("")
    # Roll main loop
    while True:
        # Ask the user if they would like to roll
        choice = input("Would you like to roll?\n"
                       "(Type 'yes', or 'no')")
        print("")
        if choice == 'yes':
            # If the player didn't roll any runners draw 3 new dice
            if runners == 0:
                draw(3)
                hand = colors_in_hand()
                print("You have the following colored dice in your hand:")
                print("")
                print("##############")
                print(hand[0])
                print(hand[1])
                print(hand[2])
                print("##############")
                print("")
            # If the player rolled 1 runner draw 2 new dice
            elif runners == 1:
                draw(2)
                hand = colors_in_hand()
                print("You have the following colored dice in your hand:")
                print("")
                print("##############")
                print(hand[0])
                print(hand[1])
                print(hand[2])
                print("##############")
                print("")
                runners = 0
            # If the player rolled 2 runners draw 1 new die
            elif runners == 2:
                draw(1)
                hand = colors_in_hand()
                print("You have the following colored dice in your hand:")
                print("")
                print("##############")
                print(hand[0])
                print(hand[1])
                print(hand[2])
                print("##############")
                print("")
                runners = 0
            else:
                runners = 0
            # Check what was rolled
            # for every brain add 1 to brain count
            # for every shotgun add to shotgun count
            # for every runner add to runner count
            for i in colors_in_hand():
                if i == "Green":
                    print("One die is Green")
                    outcome = random.choice(green)
                    print("It rolled a", outcome)
                    print("")
                    if outcome == "Brain":
                        brains = brains + 1
                        # Move a Green die from hand to side
                        move_green()
                    elif outcome == "Runner":
                        runners = runners + 1
                    elif outcome == "Shotgun":
                        shotguns = shotguns + 1
                        # Move a Green die from hand to side
                        move_green()
                elif i == "Yellow":
                    print("One die is Yellow")
                    outcome = random.choice(yellow)
                    print("It rolled a", outcome)
                    print("")
                    if outcome == "Brain":
                        brains = brains + 1
                        # Move a Yellow die from hand to side
                        move_yellow()
                    elif outcome == "Runner":
                        runners = runners + 1
                    elif outcome == "Shotgun":
                        shotguns = shotguns + 1
                        # Move a Yellow die from hand to side
                        move_yellow()
                elif i == "Red":
                    print("One die is Red")
                    outcome = random.choice(red)
                    print("It rolled a", outcome)
                    print("")
                    if outcome == "Brain":
                        brains = brains + 1
                        # Move a Red die from hand to side
                        move_red()
                    elif outcome == "Runner":
                        runners = runners + 1
                    elif outcome == "Shotgun":
                        shotguns = shotguns + 1
                        # Move a Red die from hand to side
                        move_red()
            print("")
            print("On this turn so far you have", brains, "Brains, and", shotguns,
            "Shotgun blasts")
            print("")
            # If shotgun count is 3 set all counts back to zero and end turn
            if shotguns > 2:
                print("That's 3 shotgun blasts, your turn is over")
                # End the turn
                break
            # If the player doesn't have 3 shotgun blasts ask user if they
            # want to keep rolling
            else:
                # If the player says 'yes' the roll loop continues
                print("You still don't have 3 shotguns blasts this turn, you can keep",
                    "rolling if you would like")
                print("")
        # If the player says 'no' and wants to stop rolling for the turn
        elif choice == "no":
            print("Adding", brains,  "Brains to your count and ending your turn")
            print("")
            # Add the number of brains to the players main count
            add_score(brains, player_name)
            #  End the player's turn
            break

# This was put in to test a single turn
roll("john")
