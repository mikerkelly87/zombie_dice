#!/usr/bin/python3

import sqlite3
import re

# Function to view the current score of a player
def get_player_score(p):
    with sqlite3.connect("dice.db") as connection:
        # Create DB cursor object
        c = connection.cursor()
        c.execute("SELECT score FROM players WHERE name == ?", (p,))
        score = c.fetchone()
        print(p, "Your current score is", score[0], "Brains")
        score_formatted = int(score[0])
        return score_formatted
        
get_player_score("blake")



##############
# Left to do #
##############

# Test as is with 2, 3, and 4 players.
# If everything works move the player_turn() function to it's own file
# Test as is with 2, 3, and 4 players.
# If everything still works cleanup variables that might not need to exist
# make the application not bomb if you enter something unexpected


# moved variables

# Variables
#global number_of_players
#global player1
#global player2
#global player3
#global player4
#number_of_players = 0
#player1 = ""
#player2 = ""
#player3 = ""
#player4 = ""