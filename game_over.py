import time
import jjgame
import globalvaribles
import main

#game over screen upon death of player character
def game_over():
    yes = ["yes", "y"]
    time.sleep(3)
    print("YOU DIED")
    time.sleep(3)
    print("would you like to try again? ")
    option = input(">")

    if option in yes:
        print("get ready to restart,", globalvaribles.playername)
        time.sleep(1)
        jjgame.ch_1()
    else:
        print("thanks for playing :) ")
