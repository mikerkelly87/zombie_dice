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
        number_of_players = input("How many players will be playing?\n"
                                "Please enter a number 2-4 and press Enter: ")
        if number_of_players == "2":
            print("")
        elif number_of_players == "3":
            print("")
        elif number_of_players == "4":
            print("")
        else:
            print("Please Enter a number between 2 and 4")
            game_setup()
        print("")
        if int(number_of_players) == 2:
            player1 = input("Please enter the name of player 1 and press Enter: ")
            player2 = input("Please enter the name of player 2 and press Enter: ")
            create_players_table(int(2), player1.capitalize(), player2.capitalize(), None, None)
            player_turn(int(2), player1.capitalize(), player2.capitalize(), None, None)
            break
        elif int(number_of_players) == 3:
            player1 = input("Please enter the name of player 1 and press Enter: ")
            player2 = input("Please enter the name of player 2 and press Enter: ")
            player3 = input("Please enter the name of player 3 and press Enter: ")
            create_players_table(int(3), player1.capitalize(), player2.capitalize(), player3.capitalize(), None)
            player_turn(int(3), player1.capitalize(), player2.capitalize(), player3.capitalize(), None)
            break
        elif int(number_of_players) == 4:
            player1 = input("Please enter the name of player 1 and press Enter: ")
            player2 = input("Please enter the name of player 2 and press Enter: ")
            player3 = input("Please enter the name of player 3 and press Enter: ")
            player4 = input("Please enter the name of player 4 and press Enter: ")
            create_players_table(int(4), player1.capitalize(), player2.capitalize(), player3.capitalize(), player4.capitalize())
            player_turn(int(4), player1.capitalize(), player2.capitalize(), player3.capitalize(), player4.capitalize())
            break
        else:
            print("Please enter a number 2-4 and press Enter")
    print("")

game_setup()
