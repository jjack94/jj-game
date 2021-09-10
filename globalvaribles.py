import time
import jjgame

# values for answers and name for game files 
def gVariables():
    global playername
    global answer_a
    global answer_b
    global yes
    global no
    global suit


playername = "Name"  # Default player name
answer_a = ["a", "A"]
answer_b = ["b", "B"]
yes = ["yes", "y"]
no = ["no", "n"]
suit = 0

# help message for player
def helpme():
    time.sleep(2)
    assist = ["You may use lower and uppercase inputs for this game, make your decisions carefully as this game is "
              "unforgiving, and if you do not choose A or B the game will decide for you"]
    time.sleep(1)
    for x in assist:
        print(x)
