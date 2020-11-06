import random
import time
import sys
import player_choice


class warrior(object):
    health = 200
    attack = 50
    magic = 0

class elf(object):
    health = 150
    attack = 45
    magic = 25


class wizard(object):
    health = 100
    attack = 35
    magic = 75

# enemy class


class zombie(object):
    name = "zombie"
    health = 60
    attack = 25
    defense = 40


class vampire(object):
    name = "vampire"
    health = 75
    attack = 40
    defense = 35


class werewolf(object):
    name = "werewolf"
    health = 100
    attack = 55
    defense = 35


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


def heroselect():
    print("What Hero will you be?!")
    select_character = input("1. Warrior \n2. Elf \n3. wizard \n")
    if select_character == "1":
        character = warrior
        print("Excellent, you have chosen the Warrior. Strong and courageous")
        print("health -", character.health)
        print("attack -", character.attack)
        print("magic - ", character.magic)
        return character
    elif select_character == "2":
        character = elf
        print("Splendid, you have chosen the elf. Wise, Nimble and loyl to the cause!")
        print("health -", character.health)
        print("attack -", character.attack)
        print("magic - ", character.magic)
        return character
    elif select_character == "3":
        character = wizard
        print("Wonderful, you have chosen the wizard. Mystical andvery powerful")
        print("health -", character.health)
        print("attack -", character.attack)
        print("magic - ", character.magic)
        return character
    else:
        print("Only choose the charactes given")
        heroselect()


def enemy_select(zombie, vampire, werewolf):
    enemies_list = [zombie, vampire, werewolf]
    random_chance = random.randint(0, 2)
    enemy = enemies_list[random_chance]
    return enemy


def battle():
    enemy = enemy_select(zombie, vampire, werewolf)
    print("you were attacked by", enemy.name)
    print("What do you do?")
    while enemy.health > 0:
        choice = input("1. fight\n2. Use magic\n3. Run away")

        if choice == "1":
            print("you attack the", enemy.name)
            enemy.health = enemy.health - character.attack
            print("A direct hit, their remaining health is now", enemy.health)
            if enemy.health > 0:
                character.health = character.health - enemy.attack
                print("you take some damage, your remaining health is now",
                      character.health)
            else:
                if enemy.name == "zombie":
                    enemy.health = 0
                elif enemy.name == "vampire":
                    enemy.health = 0
                elif enemy.health == "werewolf":
                    enemy.health = 0
                print("you have defeated the enemy!")
        elif choice == "2":
            print("you use magic on the", enemy.name)
            enemy.health = enemy.health - character.attack
            print("A direct hit, their remaining health is now", enemy.health)
            if enemy.health > 0:
                character.health = character.health - enemy.attack
                print("you take some damage, your remaining health is now",
                      character.health)
            else:
                if enemy.name == "zombie":
                    enemy.health = 0
                elif enemy.name == "vampire":
                    enemy.health = 0
                elif enemy.health == "werewolf":
                    enemy.health = 0
                print("Yay! you have defeated the enemy!")
        elif choice == "3":
            print("You got away safetly")
            break


# def choose_hero():
#     import characters
#     characters.print_heroes()
#     hero = ""
#     while hero != "Warrior" and hero != "Archer" and hero != "Mage":
#         hero = input("which hero would you like to be? (Warrior Archer Mage):")
#         if hero == "Warrior":
#             print("great choice!")
#         elif hero == "Archer":
#             print("Amazing Choice")
#         elif hero == "Mage":
#             print("Super Duper Choice")
#         else:
#             print("invalid choice. Please try again")


def Start_over():
    Play_Again = input("would you like to play again? [Y/N]:")
    if Play_Again.casefold() == "y":
        backstory()
        player_one()
        time.sleep(2)
        heroselect()
        # choose_hero()
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
        heroselect()
        enemy_select(zombie, vampire, werewolf)
        battle()
        # choose_hero()
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

character = heroselect
MainScreenOptions()
