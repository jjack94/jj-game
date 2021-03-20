import time
import jjgame


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


def helpme():
    time.sleep(2)
    assist = ["You may use lower and uppercase inputs for this game, make your decisions carefully as this game is "
              "unforgiving"]
    time.sleep(1)
    for x in assist:
        print(x)
