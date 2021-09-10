import jjgame
import globalvaribles

# launch from here to begin game 
def main():
    globalvaribles.gVariables()
    while globalvaribles.playername != "Name":
        jjgame.ch_1()
    else:
        jjgame.greet()


if __name__ == "__main__":
    main()
