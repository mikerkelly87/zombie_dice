#!/usr/bin/python3

# This will create the sqlite database once the user decides
# how many players are playing

# Import sqlite module and variables from main.py
import sqlite3
import time
#from main import number_of_players, player1, player2, player3, player4


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
        # Create cup table
        c.execute("CREATE TABLE cup(dice TEXT)")


# Create a database table to keep track of the colors of dice
# that are currently in the active player's hand
def create_hand_table():
    with sqlite3.connect("dice.db") as connection:
        # Create DB cursor object
        c = connection.cursor()
        # Drop table first to always start a new game
        c.execute("DROP TABLE IF EXISTS hand")
        # Create player's hand table
        c.execute("CREATE TABLE hand(dice TEXT)")


# Create a database table to keep track of the colors of dice
# that are put to the side from the player's hand
def create_side_table():
    with sqlite3.connect("dice.db") as connection:
        # Create DB cursor object
        c = connection.cursor()
        # Drop table first to always start a new game
        c.execute("DROP TABLE IF EXISTS side")
        # Create side table
        c.execute("CREATE TABLE side(dice TEXT)")


# Reset the dice in the cup
def reset_cup():
    with sqlite3.connect("dice.db") as connection:
        # Create DB cursor object
        c = connection.cursor()
        # Create the cup table
        create_cup_table()
        # Replace all the dice in the cup with the original values
        #
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


# Put all dice on the side back into the cup if the cup is empty
def refill_cup():
    with sqlite3.connect("dice.db") as connection:
        # Create DB cursor object
        c = connection.cursor()
        print("Cup is empty, moving dice from the side back",
          "into the cup")
        # Move the dice from the side back into the cup while
        # The global variables in roll() will keep track of what has been rolled
        c.execute("INSERT INTO cup SELECT * FROM side")
        c.execute("DELETE FROM side")
        # Need to 'VACUUM' to reindex the row IDs
        c.execute('VACUUM')


# Draw x amount of dice from the cup and put them into the active player's hand
def draw(x):
    # Let the player know how many dice are being drawn from the cup
    if x ==3:
        print("Drawing three dice from the cup to roll with")
        print("")
        print("......... 1")
        time.sleep(1)
        print("......... 2")
        time.sleep(1)
        print("......... 3")
        print("")
    elif x == 2:
        print("Drawing two dice from the cup to roll with")
        print("")
        print("......... 1")
        time.sleep(1)
        print("......... 2")
        print("")
    elif x == 1:
        print("Drawing one die from the cup to roll with")
        print("")
        print("......... 1")
        print("")
    # The loop that will move the dice from the cup to the player's hand
    for i in range(0, x):
        with sqlite3.connect("dice.db") as connection:
            # Create DB cursor object
            c = connection.cursor()
            # Check to make sure there is enough dice to draw from the cup
            c.execute("SELECT Count(*) FROM cup")
            count = c.fetchone()
            count_formatted = count[0]
            # If there isn't enough dice in the cup, refill the cup from the
            # dice on the side
            if count_formatted < x:
                refill_cup()
            c.execute("SELECT rowid,dice FROM cup ORDER BY RANDOM() LIMIT 1;")
            while True:
                row = c.fetchone()
                if row is None:
                    break
                row_id = row[0]
                color = row[1]
                # Put the drawn die from the cup into the active player's hand
                c.execute('INSERT INTO hand (dice) VALUES("{0}")'.format(color))
                # Remove the die from the cup
                c.execute('DELETE FROM cup WHERE rowid = {0}'.format(row_id))



# Let the active player know what color dice they have in their hand
def colors_in_hand():
    with sqlite3.connect("dice.db") as connection:
        # Create the DB cursor object
        c = connection.cursor()
        # First Color
        c.execute("SELECT * FROM hand WHERE rowid = 1")
        c1 = c.fetchone()
        color1 = c1[0]
        # Second Color
        c.execute("SELECT * FROM hand WHERE rowid = 2")
        c2 = c.fetchone()
        color2 = c2[0]
        # Third COlor
        c.execute("SELECT * FROM hand WHERE rowid = 3")
        c3 = c.fetchone()
        color3 = c3[0]
        # Put the colors into a tuple
        hand = [color1, color2, color3]
        # Pass the colors so roll() can see them
        return hand


# Add the brains from the current turn to the player's total score
def add_score(x, player):
    with sqlite3.connect("dice.db") as connection:
        # Create the DB cursor object
        c = connection.cursor()
        # Add the number of brains to the player's score
        c.execute("""UPDATE players SET score = score + ? WHERE name LIKE ?""", (x,player))


# Move a Green Die from the player's hand to the side
# Any Die that wasn't rolled as a runner needs to be put to the side
def move_green():
    with sqlite3.connect("dice.db") as connection:
        # Create the DB cursor object
        c = connection.cursor()
        c.execute("SELECT rowid,dice FROM hand WHERE dice = 'Green' LIMIT 1;")
        row = c.fetchone()
        row_id = row[0]
        color = row[1]
        # Put the green die from the hand to the side
        c.execute('INSERT INTO side (dice) VALUES("{0}")'.format(color))
        # Remove the die from the hand
        c.execute('DELETE FROM hand WHERE rowid = {0}'.format(row_id))
        # Need to 'VACUUM' to reindex the row IDs
        c.execute('VACUUM')


# Move a Yellow Die from the player's hand to the side
# Any Die that wasn't rolled as a runner needs to be put to the side
def move_yellow():
    with sqlite3.connect("dice.db") as connection:
        # Create the DB cursor object
        c = connection.cursor()
        c.execute("SELECT rowid,dice FROM hand WHERE dice = 'Yellow' LIMIT 1;")
        row = c.fetchone()
        row_id = row[0]
        color = row[1]
        # Put the green die from the hand to the side
        c.execute('INSERT INTO side (dice) VALUES("{0}")'.format(color))
        # Remove the die from the hand
        c.execute('DELETE FROM hand WHERE rowid = {0}'.format(row_id))
        # Need to 'VACUUM' to reindex the row IDs
        c.execute('VACUUM')


# Move a Red Die from the player's hand to the side
# Any Die that wasn't rolled as a runner needs to be put to the side
def move_red():
    with sqlite3.connect("dice.db") as connection:
        # Create the DB cursor object
        c = connection.cursor()
        c.execute("SELECT rowid,dice FROM hand WHERE dice = 'Red' LIMIT 1;")
        row = c.fetchone()
        row_id = row[0]
        color = row[1]
        # Put the green die from the hand to the side
        c.execute('INSERT INTO side (dice) VALUES("{0}")'.format(color))
        # Remove the die from the hand
        c.execute('DELETE FROM hand WHERE rowid = {0}'.format(row_id))
        # Need to 'VACUUM' to reindex the row IDs
        c.execute('VACUUM')


# This was put in to test the DB operations
# create_players_table(4)
# create_cup_table()
# reset_cup()
# create_hand_table()
# draw(3)
# colors_in_hand()
# add_score(20, "mike")
# create_side_table()
# refill_cup()
