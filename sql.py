#!/usr/bin/python3

# This will create the sqlite database once the user decides
# how many players are playing

# Import sqlite module and variables from main.py
import sqlite3
from main import number_of_players, player1, player2, player3, player4


# Callable Function to create database with names of players
def create_database(num_of_players):
    with sqlite3.connect("dice.db") as connection:
        # Create DB cursor object
        c = connection.cursor()
        # Drop table first to always start a new game
        c.execute("DROP TABLE IF EXISTS players")
        # Create players table
        c.execute("CREATE TABLE players(name TEXT, score INT)")
        # Add the player names
        if num_of_players == 2:
            c.execute("INSERT INTO players VALUES(?, ?)", (player1, 0))
            c.execute("INSERT INTO players VALUES(?, ?)", (player2, 0))
        elif number_of_players == 3:
            c.execute("INSERT INTO players VALUES(?, ?)", (player1, 0))
            c.execute("INSERT INTO players VALUES(?, ?)", (player2, 0))
            c.execute("INSERT INTO players VALUES(?, ?)", (player3, 0))
        elif number_of_players == 4:
            c.execute("INSERT INTO players VALUES(?, ?)", (player1, 0))
            c.execute("INSERT INTO players VALUES(?, ?)", (player2, 0))
            c.execute("INSERT INTO players VALUES(?, ?)", (player3, 0))
            c.execute("INSERT INTO players VALUES(?, ?)", (player4, 0))

# This was put in to test the DB creation
#create_database(4)

