# RPG style game
# choose one hero
# random attack from 1-25
# choose character == Archer, Mage, Warrior
#

from random import randint
import math
import time
import sys


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


age()
backstory()
player_one()
time.sleep(2)
choose_hero()
Start_over()

damage_taken = randint(1, 25)
