#!/usr/bin/python3

# This will create the sqlite database once the user decides
# how many players are playing

# Import sqlite module and variables from main.py
import sqlite3
from main import number_of_players, player1, player2, player3, player4


# Callable Function to create database with names of players
def create_players_table(num_of_players):
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


# Create a database table to keep track of which dice are
# in the cup throughout a player's turn
def create_cup_table():
    with sqlite3.connect("dice.db") as connection:
        # Create DB cursor object
        c = connection.cursor()
        # Drop table first to always start a new game
        c.execute("DROP TABLE IF EXISTS cup")
        # Create players table
        c.execute("CREATE TABLE cup(dice TEXT)")


# Reset the dice in the cup
def reset_cup():
    with sqlite3.connect("dice.db") as connection:
        # Create DB cursor object
        c = connection.cursor()
        # Put 6 Green dice into the cup
        i = 0
        while i < 6:
            c.execute("INSERT INTO cup VALUES('Green')")
            i = i + 1
        # Put 4 Yellow dice into the cup
        i = 0
        while i < 4:
            c.execute("INSERT INTO cup VALUES('Yellow')")
            i = i + 1
        # Put 3 Red dice into the cup
        i = 0
        while i < 3:
            c.execute("INSERT INTO cup VALUES('Red')")
            i = i + 1

# This was put in to test the DB creation
# create_players_table(4)
create_cup_table()
reset_cup()
