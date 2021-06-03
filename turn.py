#!/usr/binpython3

from sql_functions import *
from roll import *

# Function for managing each player's turn
def player_turn(n, p1, p2, p3, p4):
    while True:
        # If there are 2 players run turns for 2 players
        if n == 2:
            # If the any player's score is 13 or higher claim them the winner and quit
            score1 = get_player_score(p1)
            score2 = get_player_score(p2)
            if score1 >= 13:
                print(p1, "WINS THE GAME WITH A SCORE OF", score1, "BRAINS!!!")
                quit()
            if score2 >= 13:
                print(p2, "WINS THE GAME WITH A SCORE OF", score2, "BRAINS!!!")
                quit()
            # If the first player's score isn't 13 or higher continue with rolling the dice
            print("")
            print("It's Your Turn", p1)
            print("Here is the current score:")
            print("You:", score1)
            print(p2, score2)
            print("")
            roll(p1)
            # If the any player's score is 13 or higher claim them the winner and quit
            score1 = get_player_score(p1)
            score2 = get_player_score(p2)
            if score1 >= 13:
                print(p1, "WINS THE GAME WITH A SCORE OF", score1, "BRAINS!!!")
                quit()
            if score2 >= 13:
                print(p2, "WINS THE GAME WITH A SCORE OF", score2, "BRAINS!!!")
                quit()
            # If the second player's score isn't 13 or higher continue with rolling the dice
            print("")
            print("It's Your Turn", p2)
            print("Here is the current score:")
            print("You:", score2)
            print(p1, score1)
            print("")
            roll(p2)
            # If there are 3 players run turns for 3 players
        elif n == 3:
            # If the any player's score is 13 or higher claim them the winner and quit
            score1 = get_player_score(p1)
            score2 = get_player_score(p2)
            score3 = get_player_score(p3)
            if score1 >= 13:
                print(p1, "WINS THE GAME WITH A SCORE OF", score1, "BRAINS!!!")
                quit()
            if score2 >= 13:
                print(p2, "WINS THE GAME WITH A SCORE OF", score2, "BRAINS!!!")
                quit()
            if score3 >= 13:
                print(p3, "WINS THE GAME WITH A SCORE OF", score3, "BRAINS!!!")
                quit()
            # If nobody's score isn't 13 or higher continue with rolling the dice
            print("")
            print("It's Your Turn", p1)
            print("Here is the current score:")
            print("You:", score1)
            print(p2, score2)
            print(p3, score3)
            print("")
            roll(p1)
            # If any player's score is 13 or higher claim them the winner and quit
            score1 = get_player_score(p1)
            score2 = get_player_score(p2)
            score3 = get_player_score(p3)
            if score1 >= 13:
                print(p1, "WINS THE GAME WITH A SCORE OF", score1, "BRAINS!!!")
                quit()
            if score2 >= 13:
                print(p2, "WINS THE GAME WITH A SCORE OF", score2, "BRAINS!!!")
                quit()
            if score3 >= 13:
                print(p3, "WINS THE GAME WITH A SCORE OF", score3, "BRAINS!!!")
                quit()
            # If nobody's score isn't 13 or higher continue with rolling the dice
            print("")
            print("It's Your Turn", p2)
            print("Here is the current score:")
            print("You:", score2)
            print(p1, score1)
            print(p3, score3)
            print("")
            roll(p2)
            # If any player's score is 13 or higher claim them the winner and quit
            score1 = get_player_score(p1)
            score2 = get_player_score(p2)
            score3 = get_player_score(p3)
            if score1 >= 13:
                print(p1, "WINS THE GAME WITH A SCORE OF", score1, "BRAINS!!!")
                quit()
            if score2 >= 13:
                print(p2, "WINS THE GAME WITH A SCORE OF", score2, "BRAINS!!!")
                quit()
            if score3 >= 13:
                print(p3, "WINS THE GAME WITH A SCORE OF", score3, "BRAINS!!!")
                quit()
            # If the nobody's score isn't 13 or higher continue with rolling the dice
            print("")
            print("It's Your Turn", p3)
            print("Here is the current score:")
            print("You:", score3)
            print(p1, score1)
            print(p2, score2)
            print("")
            roll(p3)
        # If there are 3 players run turns for 3 players
        elif n == 4:
            # If the any player's score is 13 or higher claim them the winner and quit
            score1 = get_player_score(p1)
            score2 = get_player_score(p2)
            score3 = get_player_score(p3)
            score4 = get_player_score(p4)
            if score1 >= 13:
                print(p1, "WINS THE GAME WITH A SCORE OF", score1, "BRAINS!!!")
                quit()
            if score2 >= 13:
                print(p2, "WINS THE GAME WITH A SCORE OF", score2, "BRAINS!!!")
                quit()
            if score3 >= 13:
                print(p3, "WINS THE GAME WITH A SCORE OF", score3, "BRAINS!!!")
                quit()
            if score4 >= 13:
                print(p4, "WINS THE GAME WITH A SCORE OF", score4, "BRAINS!!!")
                quit()
            # If nobody's score isn't 13 or higher continue with rolling the dice
            print("")
            print("It's Your Turn", p1)
            print("Here is the current score:")
            print("You:", score1)
            print(p2, score2)
            print(p3, score3)
            print(p4, score4)
            print("")
            roll(p1)
            # If any player's score is 13 or higher claim them the winner and quit
            score1 = get_player_score(p1)
            score2 = get_player_score(p2)
            score3 = get_player_score(p3)
            score4 = get_player_score(p4)
            if score1 >= 13:
                print(p1, "WINS THE GAME WITH A SCORE OF", score1, "BRAINS!!!")
                quit()
            if score2 >= 13:
                print(p2, "WINS THE GAME WITH A SCORE OF", score2, "BRAINS!!!")
                quit()
            if score3 >= 13:
                print(p3, "WINS THE GAME WITH A SCORE OF", score3, "BRAINS!!!")
                quit()
            if score4 >= 13:
                print(p4, "WINS THE GAME WITH A SCORE OF", score4, "BRAINS!!!")
                quit()
            # If nobody's score isn't 13 or higher continue with rolling the dice
            print("")
            print("It's Your Turn", p2)
            print("Here is the current score:")
            print("You:", score2)
            print(p1, score1)
            print(p3, score3)
            print(p4, score4)
            print("")
            roll(p2)
            # If any player's score is 13 or higher claim them the winner and quit
            score1 = get_player_score(p1)
            score2 = get_player_score(p2)
            score3 = get_player_score(p3)
            score4 = get_player_score(p4)
            if score1 >= 13:
                print(p1, "WINS THE GAME WITH A SCORE OF", score1, "BRAINS!!!")
                quit()
            if score2 >= 13:
                print(p2, "WINS THE GAME WITH A SCORE OF", score2, "BRAINS!!!")
                quit()
            if score3 >= 13:
                print(p3, "WINS THE GAME WITH A SCORE OF", score3, "BRAINS!!!")
                quit()
            if score4 >= 13:
                print(p4, "WINS THE GAME WITH A SCORE OF", score4, "BRAINS!!!")
                quit()
            # If the nobody's score isn't 13 or higher continue with rolling the dice
            print("")
            print("It's Your Turn", p3)
            print("Here is the current score:")
            print("You:", score3)
            print(p1, score1)
            print(p2, score2)
            print(p4, score4)
            print("")
            roll(p3)
            # If any player's score is 13 or higher claim them the winner and quit
            score1 = get_player_score(p1)
            score2 = get_player_score(p2)
            score3 = get_player_score(p3)
            score4 = get_player_score(p4)
            if score1 >= 13:
                print(p1, "WINS THE GAME WITH A SCORE OF", score1, "BRAINS!!!")
                quit()
            if score2 >= 13:
                print(p2, "WINS THE GAME WITH A SCORE OF", score2, "BRAINS!!!")
                quit()
            if score3 >= 13:
                print(p3, "WINS THE GAME WITH A SCORE OF", score3, "BRAINS!!!")
                quit()
            if score4 >= 13:
                print(p4, "WINS THE GAME WITH A SCORE OF", score4, "BRAINS!!!")
                quit()
            # If the nobody's score isn't 13 or higher continue with rolling the dice
            print("")
            print("It's Your Turn", p4)
            print("Here is the current score:")
            print("You:", score4)
            print(p1, score1)
            print(p2, score2)
            print(p3, score3)
            print("")
            roll(p4)