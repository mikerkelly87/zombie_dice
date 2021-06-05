## Zombie Dice

This is my attempt to recreate the dice game known 
as Zombie Dice in Python to get some more practice 
with Python

## Rules

The first player will pick 3 of the 13 dice from 
random out of the cup.  
The player will roll the dice, each die has 3 
outcomes, Brain, Shotgun Blast, or Runner.  
The player (or application in this case) will count 
up the number of each.  
Brains will count towards your overall score.  
A Runner doesn't count for or against you.  
If you get 3 shotgun blasts in a single turn you 
lose any Brains you would have gained that turn.  
After you count up your numbers you can choose to 
roll again or pass to the next player.  
If you rolled any Runners in your prior roll you 
have to keep those and only pull dice out of the 
cup to equal 3 dice to roll  
(ex1: if you had rolled 3 Runners you will roll 
those same 3 dice and not draw any new dice from the cup)  
(ex2: if you rolled 1 Runner you will roll that 
same die along with 2 new dice drawn from the cup)  
If you decide you don't want to risk rolling 
anymore Shotgun Blasts, you count up the total 
number of Brains you gathered and add that to 
your score.  
Player 2 follows this same process, then every 
other player takes their turn.  
This continues until a player reaches 13 Brains 
declaring them the winner.

## Caveats
If player 1 gains 13 Brains he can choose to keep 
rolling to add to that total. Player 1 may want to 
do this because the players following him will also 
get a chance to roll as well. No matter which 
player hits 13 Brains first the turn must finish. 
If player 2 gets 13 Brains first only the players 
who would roll after player 2 would get a last 
chance to roll.

If there is a tie, the leaders (only) play a single 
tie breaker round, this continues until there is a 
definite winner.

## Notable Mentions
There are 3 colors of dice, Green, Yellow, and Red.
There are 6 Green dice, 4 Yellow dice, and 3 Red 
dice.
A Green die has 3 Brains, 2 Runners, and 1 Shotgun 
Blast on it's six sides.
A Yellow die has 2 Brains, 2 Runners, and 2 Shotgun 
Blasts on it's six sides.
A Red die has 1 Brain, 2 Runners, and 3 Shotgun 
Blasts on it's six sides.
This is worth noting because if you have rolled 6 
Brains and 2 Shotgun Blast in your turn so far over 
6 Green dice and 2 Yellow Dice, you may want to end 
your turn as the remaining dice in the cup have a 
higher probability of giving you a 3rd Shotgun Blast.

If you run out of dice in the cup but want to keep 
rolling you (or the application in this case) will 
tally up the number of Brains and Shotgun blasts you 
have so far in the turn, then put all the dice back 
in the cup and continue picking dice to roll from 
the cup.
