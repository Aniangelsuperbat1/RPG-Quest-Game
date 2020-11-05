from random import randint
import time
import sys


def MainScreen():
    print("Play")
    print("Quit")
    print("Help")


def age():
    age = ""
    while age <= str(17):
        age = input("what is your age?")
        if age <= str(17):
            print("you are too young to play this game!, go home!")
            sys.exit()
        else:
            print("Yay! You are old enough to play this game")


def backstory():
    time.sleep(2)
    print("The world is on the brink of extintion")
    time.sleep(2)
    print("The dark overlord is on the verge of victory")
    time.sleep(2)
    print("You are the the world's last hope")
    time.sleep(2)


def player_one():
    name = input("Weary traveler, what is your name?")
    print("welcome " + name)


def choose_hero():
    import characters
    characters.print_heroes()
    hero = ""
    while hero != "Warrior" and hero != "Archer" and hero != "Mage":
        hero = input("which hero would you like to be? (Warrior Archer Mage):")
        if hero == "Warrior":
            print("great choice!")
        elif hero == "Archer":
            print("Amazing Choice")
        elif hero == "Mage":
            print("Super Duper Choice")
        else:
            print("invalid choice. Please try again")


def Start_over():
    Play_Again = input("would you like to play again? [Y/N]:")
    if Play_Again.casefold() == "y":
        backstory()
        player_one()
        time.sleep(2)
        choose_hero()
        Start_over()
    else:
        Play_Again.casefold() == "n"
        print("Thank you for playing")


def MainScreenOptions():
    MainScreen()
    Choice = input("what do you want to do:")
    if Choice == ("play"):
        age()
        backstory()
        player_one()
        time.sleep(2)
        choose_hero()
        Start_over()
    elif Choice == ("help"):
        print("Play: Plays the game")
        print("Quit: Quits the game")
        MainScreenOptions()
    elif Choice == ("quit"):
        sys.exit

    while Choice not in ("play, quit, help"):

        print("invalid choice, please try again")
        MainScreenOptions()


print()
print()
print()
print("           *********************")
print("           *  Welcome to game  *")
print("           *********************")


MainScreenOptions()
