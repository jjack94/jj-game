import time
import jjgame


def game_over_mid():
    time.sleep(3)
    print("YOU DIED")
    time.sleep(3)
    print("would you like to try from the start of the previous scene again? ")
    option = input(">")

    if option in yes:
        print("get ready to restart from start of previous scene,", globalvaribles.playername)
        time.sleep(1)
        jjgame.ch_3_4()
    else:
        print("thanks for playing :) ")