import jjgame
import globalvaribles

# begin game 
def main():
    globalvaribles.gVariables()
    while globalvaribles.playername != "Name":
        jjgame.ch_1()
    else:
        jjgame.greet()


if __name__ == "__main__":
    main()
