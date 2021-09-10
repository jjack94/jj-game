# james jack

import time
import globalvaribles
from game_over import game_over
from game_over_mid import game_over_mid

answer_a = ["a", "A"]
answer_b = ["b", "B"]
yes = ["yes", "y"]
no = ["no", "n"]
suit = 0


def greet():
    globalvaribles.playername = input("What is your name?: ")
    time.sleep(2)
    print("Would you like an explantation on inputs for this game:")
    option = input(">")
    if option in yes:
        globalvaribles.helpme()
    else:
        time.sleep(2)
        print("let us carry on.")
    time.sleep(2)
    print("Welcome to this text based game, ", globalvaribles.playername)
    ch_1()


def ch_1():
    print("The cryo-sleep pod opens, and the air is cold, but no one else on the crew’s pod opens. ")
    print(".")
    time.sleep(3)
    print("You wake up on your spacecraft, other crew are still in permanent sleep "
          "until the destination is reached. Waking up crew before destination could cause harm to them.")
    print(".")
    time.sleep(3)
    print("What will you do ?: ")
    time.sleep(1)
    print("""A: go inspect the sleep console to see why you woke up 
    B: Go to the main deck right away to see where the ship is""")
    option = input(">")

    if option in answer_a:
        print("the console display tells you that all crew were to be woke due to unidentified organic life found on "
              "the ship , it appears only your pod opened")
        print(".")
        time.sleep(3)
        print("you feel weak, you need to eat before you remotely think about dealing with a 'unidentified lifeform' "
              "on the ship ")
        time.sleep(3)
        ch_2()
    else:
        print("You rush to see where the ship has stopped moving, making your way to the main deck ")
        time.sleep(3)
        ch_3_4()


def ch_2():
    print("The mess hall was quiet and there was a flickering light in the far corner where the food dispenser is")
    print(".")
    time.sleep(3)
    print("you grabbed some nutritious food slop to eat, and sat at one of the many steel tables to eat")
    time.sleep(3)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print("while finishing up your meal, you hear a strange otherworldly hissing come from the vent above your table")
    print(".")
    time.sleep(3)
    print("what do you do now ?: ")
    time.sleep(1)
    print("A: get up and leave right away")
    print("B: ignore the hissing, it probably was just the wind")
    option = input(">")

    if option in answer_b:
        print("as you find out a little too late, that noise was not the wind")
        print(".")
        time.sleep(3)
        print("you hear a large thump from above you, and before you can even look up, everything goes black")
        print(".")
        game_over()
    else:
        ch_3_4()


def ch_3_4():
    print("The main deck had all of the security lights flashing and the message, "
          "“unknown biological lifeform detected” was flashing on the control screen. ")
    print(".")
    time.sleep(3)
    print("You see security measures were tripped and the ship is no longer moving. "
          "Manual override is required, or the unknown lifeform must be ejected from the ship to resume passage. ")
    print(".")
    time.sleep(3)
    print("You then notice there is a protective hazard suit sitting on the chair in front of you")
    print(".")
    time.sleep(3)
    print("This might be useful, do you want to take the time to put it on? ")
    option = input(">")

    if option in yes:
        suit = 1
        print("You put the suit on, it seems like it could protect you from whatever is out there")
    else:
        suit = 0
        print("You decide you cannot spare the time, turning your attention to the main screen")

    time.sleep(3)

    print("The computer tells you that the lifeform is in the bottom deck, "
          "the computer only is able to tell you it is"
          "located on the deck, and nothing more")
    print(".")
    time.sleep(3)
    print("What do you want to do now? ")
    print("A: Decide to go to the bottom floor and try to see if there is anything you can do. "
          "You do not have any weapons so you will have to chance it may be friendly, "
          "or that you can knock it into space via the airlock")
    print("B: You decide that re-routing the ship manually and going back to cryo-sleep is the most sound plan")

    option = input(">")
    if option in answer_b:
        print("You go back to sleep, and hope for the best")
        print(".")
        time.sleep(3)
        print("You never wake up. ")
        print(".")
        game_over()
    else:
        print("You reached the bottom deck")
    time.sleep(3)
    print(
        "You see a hall of rooms used for storage in front of you unlit, and the faint hissing bouncing off the walls")
    print("The sound is difficult to pinpoint, and you cant tell which room it is coming from")
    print(".")
    time.sleep(3)
    print("Naturally, you decide the first room on your right is the first one to check")
    print(".")
    time.sleep(3)
    print("Do you turn on the light before checking the room? ")
    option = input(">")

    if option in yes and suit < 1:
        print("You turn on the lights")
        print(".")
        time.sleep(3)
        print("A figure is coiled in the corner of the ceiling, and before your eyes adjust to the bright lights "
              "you just turned on, the figure leaps towards you and pass out")
        print(".")
        game_over_mid()
    elif option in yes and suit > 0:
        print("You turn on the lights ")
        print(".")
        time.sleep(3)
        print("Coiled in the corner of the 10 foot high ceiling, you see a something that "
              "vaguely looks human, but the arms"
              "and legs are much too long, and it appears to have transparent skin as well as a tail with a point ")
        print(".")
        time.sleep(3)
        print("The thing leaps out and you, and it's claws dig into the hazard suit")
        print(".")
        time.sleep(3)
        print("The suit was thick enough to where the claws did not reach through the suit, saving your life")
        print(".")
        time.sleep(3)
        print(".")
        print("The creature then lets out a loud shriek as if leaping into the light was harmful to it")
        print(".")
        time.sleep(3)
        print("The creature then leaps away from you into the dark corridor of the basement, hissing while it runs"
              "through a door to another room")
        print(".")
        ch_5()

    else:
        print("You slowly open the door, and the second it is open, you see a large figure leap towards you from the "
              "ceiling")
        print(".")
        time.sleep(3)
        print("Before you could even scream, the figure pulls you into the dark with them")
        print(".")
        game_over_mid()


def ch_5():
    print("As you are struggling to process what just happened, you realize that the room the thing ran into was"
          "the ONLY storage room with an airlock that can be opened within it")
    print(".")
    time.sleep(3)
    print("You could hear faint hissing coming from the room, which now sounds like it is turning into a growl")
    print(".")
    time.sleep(3)
    print("You decide that the best thing to do is open the airlock, how do you reach for the button ?: ")
    print(".")
    time.sleep(3)
    print("A: Reach slowly")
    print("B: Reach quickly")

    option = input(">")
    if option in answer_a:
        print("You slowly reach for the button that is arms reach in the doorway of the pitch black room")
        print(".")
        time.sleep(3)
        print("Your hand is on the button ready to push it down, and you can see the thing is slowly inching towards "
              "you across the room")
        print(".")
        time.sleep(3)
        print("You push the button down and grab on to the handle next to it as the room filled with scrap metal is "
              "sucked into the vacuum of space, including the creature")
        print(".")
        time.sleep(3)
        print("The creature lets out a shrill howl as it falls into space, and you are holding on for dear life as the "
              "airlock should soon close (standard airlock procedure is that they remain open for 5 seconds before "
              "closing")
        print(".")
        time.sleep(3)
        print("The airlock closes and you feel relieved to hear the intercom of the ship say 'unidentified lifeform no "
              "longer present, resuming flight path'")
        print(".")
        time.sleep(3)
        end()
    else:
        print("The creature reacts immediately to your fast movement, jumping towards you with it's mouth wide open")
        print(".")
        game_over_mid()


def end():
    print("You return to the main deck to make sure all is in order before returning to sleep")
    print(".")
    time.sleep(3)
    print("The journey to the destination is still 6 light years away, and you do not feel like staying awake for "
          "5 years, so you make your make back to the cyro sleep area ")
    print(".")
    time.sleep(3)
    print("You get into the pod, wondering how you will explain what happened to your crew mates, and if anyone will "
          "ever believe you")
    print(".")
    time.sleep(3)
    print("THE END")
    time.sleep(1)
    print("Would you like to play again? ")
    option = input(">")
    if option in yes:
        time.sleep(1)
        ch_1()
    else:
        print("Thank you for playing, ", globalvaribles.playername, "!!!!!")

