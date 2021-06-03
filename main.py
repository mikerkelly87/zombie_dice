#!/usr/bin/python3

# Main flow of the application

# Import functions
from sql_functions import *
from roll import roll
from turn import *

# Game setup function
def game_setup():
    # Ask the user how many players are playing
    while True:
        print("")
        number_of_players = int(input("How many players will be playing?\n"
                                "Please enter a number 2-4 and press Enter: "))
        print("")
        if number_of_players == 2:
            player1 = input("Please enter the name of player 1 and press Enter: ")
            player2 = input("Please enter the name of player 2 and press Enter: ")
            create_players_table(int(2), player1, player2, None, None)
            player_turn(int(2), player1, player2, None, None)
            break
        elif number_of_players == 3:
            player1 = input("Please enter the name of player 1 and press Enter: ")
            player2 = input("Please enter the name of player 2 and press Enter: ")
            player3 = input("Please enter the name of player 3 and press Enter: ")
            create_players_table(int(3), player1, player2, player3, None)
            player_turn(int(3), player1, player2, player3, None)
            break
        elif number_of_players == 4:
            player1 = input("Please enter the name of player 1 and press Enter: ")
            player2 = input("Please enter the name of player 2 and press Enter: ")
            player3 = input("Please enter the name of player 3 and press Enter: ")
            player4 = input("Please enter the name of player 4 and press Enter: ")
            create_players_table(int(4), player1, player2, player3, player4)
            player_turn(int(4), player1, player2, player3, player4)
            break
        else:
            print("Please enter a number 2-4 and press Enter")
    print("")

game_setup()
