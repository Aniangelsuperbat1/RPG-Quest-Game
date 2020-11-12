import random
import time
import sys
import player_choice


class warrior(object):
    health = 200
    attack = 50
    magic = 5


class elf(object):
    health = 150
    attack = 75
    magic = 20


class wizard(object):
    health = 100
    attack = 20
    magic = 50

# enemy class


class zombie(object):
    name = "zombie"
    health = 100
    attack = 10
    defense = 40


class vampire(object):
    name = "vampire"
    health = 100
    attack = 20
    defense = 35


class werewolf(object):
    name = "werewolf"
    health = 100
    attack = 25
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
        # elif age >= str(100):
        #     print("You are way too old to be alive right now!")
        #     sys.exit
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


def battle(character):
    enemy = enemy_select(zombie, vampire, werewolf)
    print("you were attacked by a", enemy.name)
    print("What do you do?")
    while enemy.health > 0:
        choice = input("1. fight\n2. Use magic\n3. Run away")

        if choice == "1":
            print("you attack the", enemy.name)
            enemy.health = enemy.health - character.attack
            print("A direct hit, their remaining health is now",
                  enemy.health)
            if enemy.health > 0:
                character.health = character.health - enemy.attack
                print("you take some damage, your remaining health is now",
                      character.health)
            else:
                if enemy.name == "zombie":
                    enemy.health = 60
                elif enemy.name == "vampire":
                    enemy.health = 75
                elif enemy.health == "werewolf":
                    enemy.health = 100
                print("you have defeated the enemy!")
                break
        elif choice == "2":
            print("you use magic on the", enemy.name)
            enemy.health = enemy.health - character.magic
            print("A direct hit, their remaining health is now", enemy.health)
            if enemy.health > 0:
                character.health = character.health - enemy.attack
                print("you take some damage, your remaining health is now",
                      character.health)
            else:
                if enemy.name == "zombie":
                    enemy.health = 60
                elif enemy.name == "vampire":
                    enemy.health = 75
                elif enemy.health == "werewolf":
                    enemy.health = 100
                print("Yay! you have defeated the enemy!")
                break
        elif choice == "3":
            print("This is no time to be scared, the fate of the world is at stake!")
            battle(character)


def gameover(character):
    if character.health < 1:
        print("You have run out of health")
        print("The world will fall to the dark lord")
        print("You have failed in your mission")
        print("Thank you for playing")


# def Path_one():
#     decision = input("which path will you choose? 1\n 2\n 3")
#     if decision == "1":
#         print("")
#         First_path()
#     elif decision == "2":
#         print("")
#         Second_path()
#     elif decision == "3":
#         print("")
#         third_path()


# def First_path():
#     print("")
#     Path = input("which path will go down?: 1\n 2\n 3")
#     if Path == "1":
#         print("")
#         print("")
#         First_path_one()
#     elif Path == "2":
#         print("")
#         print("")
#         First_path_two()
#     elif Path == "3":
#         print("")
#         print("")
#         First_path_three()


# def First_path_one():
#     print("")
#     print("")
#     Path_two = input("which path will go down?: 1\n 2\n 3")
#     if Path_two == "1":
#         print("")
#         print("")
#         First_path_one_one()
#     elif Path_two == "2":
#         print("")
#         print("")
#         First_path_two_two()
#     elif Path_two == "3":
#         print("")
#         print("")
#         First_path_three_three()


# def First_path_two():
#     print("")
#     print("")
#     Path_three = input("which path will go down?: 1\n 2\n 3")
#     if Path_three == "1":
#         print("")
#         print("")
#         First_path_one_one()
#     elif Path_three == "2":
#         print("")
#         print("")
#         First_path_two_two()
#     elif Path_three == "3":
#         print("")
#         print("")
#         First_path_three_three()


# def First_path_three():
#     print("")
#     print("")
#     Path_four = input("which path will go down?: 1\n 2\n 3")
#     if Path_four == "1":
#         print("")
#         print("")
#         First_path_one_one()
#     elif Path_four == "2":
#         print("")
#         print("")
#         First_path_two_two()
#     elif Path_four == "3":
#         print("")
#         print("")
#         First_path_three_three()


# def First_path_one_one():
#     print("")
#     Path_five = input("which path will go down?: 1\n 2\n 3")
#     if Path_five == "1":
#         print("")
#         print("")
#         First_path_one_one_one()
#     elif Path_five == "2":
#         print("")
#         print("")
#         First_path_two_two_two()
#     elif Path_five == "3":
#         print("")
#         print("")
#         First_path_three_three_three()


# def First_path_two_two():
#     print("")
#     Path_six = input("which path will go down?: 1\n 2\n 3")
#     if Path_six == "1":
#         print("")
#         print("")
#         First_path_one_one_one()
#     elif Path_six == "2":
#         print("")
#         print("")
#         First_path_two_two_two()
#     elif Path_six == "3":
#         print("")
#         print("")
#         First_path_three_three_three()


# def First_path_three_three():
#     print("")
#     Path_Seven = input("which path will go down?: 1\n 2\n 3")
#     if Path_Seven == "1":
#         print("")
#         print("")
#         First_path_one_one_one()
#     elif Path_Seven == "2":
#         print("")
#         print("")
#         First_path_two_two_two()
#     elif Path_Seven == "3":
#         print("")
#         print("")
#         First_path_three_three_three()


# def First_path_one_one_one():
#     print("")
#     print("")
#     Dark_Lord()


# def First_path_two_two_two():
#     print("")
#     print("")
#     Dark_Lord()


# def First_path_three_three_three():
#     print("")
#     print("")
#     Dark_Lord()


# def Second_path():
#     print("")
#     print("")
#     Path_eight = input("which path will go down?: 1\n 2\n 3")
#     if Path_eight == "1":
#         print("")
#         print("")
#         second_path_one()
#     elif Path_eight == "2":
#         print("")
#         print("")
#         second_path_two()
#     elif Path_eight == "3":
#         print("")
#         print("")
#         second_path_three()


# def second_path_one():
#     print("")
#     print("")
#     Path_nine = input("which path will go down?: 1\n 2\n 3")
#     if Path_nine == "1":
#         print("")
#         print("")
#         second_path_one_one()
#     elif Path_nine == "2":
#         print("")
#         print("")
#         second_path_two_two()
#     elif Path_nine == "3":
#         print("")
#         print("")
#         second_path_three_three()

# def second_path_two():
#     print("")
#     print("")
#     Path_ten = input("which path will go down?: 1\n 2\n 3")
#     if Path_ten == "1":
#         print("")
#         print("")
#         second_path_one_one()
#     elif Path_ten == "2":
#         print("")
#         print("")
#         second_path_two_two()
#     elif Path_ten == "3":
#         print("")
#         print("")
#         second_path_three_three()

# def second_path_three():
#     print("")
#     print("")
#     Path_eleven = input("which path will go down?: 1\n 2\n 3")
#     if Path_eleven == "1":
#         print("")
#         print("")
#         second_path_one_one()
#     elif Path_eleven == "2":
#         print("")
#         print("")
#         second_path_two_two()
#     elif Path_eleven == "3":
#         print("")
#         print("")
#         second_path_three_three()

# def second_path_one_one():
#     print("")
#     print("")
#     Path_twelve = input("which path will go down?: 1\n 2\n 3")
#     if Path_twelve == "1":
#         print("")
#         print("")
#         second_path_one_one_one()
#     elif Path_twelve == "2":
#         print("")
#         print("")
#         second_path_two_two_two()
#     elif Path_twelve == "3":
#         print("")
#         print("")
#         second_path_three_three_three()

# def second_path_two_two():
#     print("")
#     print("")
#     Path_13 = input("which path will go down?: 1\n 2\n 3")
#     if Path_13 == "1":
#         print("")
#         print("")
#         second_path_one_one_one()
#     elif Path_13 == "2":
#         print("")
#         print("")
#         second_path_two_two_two()
#     elif Path_13 == "3":
#         print("")
#         print("")
#         second_path_three_three_three()

# def second_path_three_three():
#     print("")
#     print("")
#     Path_14 = input("which path will go down?: 1\n 2\n 3")
#     if Path_14 == "1":
#         print("")
#         print("")
#         second_path_one_one_one()
#     elif Path_14 == "2":
#         print("")
#         print("")
#         second_path_two_two_two()
#     elif Path_14 == "3":
#         print("")
#         print("")
#         second_path_three_three_three()

# def second_path_one_one_one():
#     print("")
#     print("")
#     Dark_Lord()

# def second_path_two_two_two():
#     print("")
#     print("")
#     Dark_Lord()

# def second_path_three_three_three():
#     print("")
#     print("")
#     Dark_Lord()

# def third_path():
#     print("")
#     print("")
#     Path_15 = input("which path will go down?: 1\n 2\n 3")
#     if Path_15 == "1":
#         print("")
#         print("")
#         third_path_one()
#     elif Path_15 == "2":
#         print("")
#         print("")
#         third_path_two()
#     elif Path_15 == "3":
#         print("")
#         print("")
#         third_path_three()

# def third_path_one():
#     print("")
#     print("")
#     Path_16 = input("which path will go down?: 1\n 2\n 3")
#     if Path_16 == "1":
#         print("")
#         print("")
#         third_path_one_one()
#     elif Path_16 == "2":
#         print("")
#         print("")
#         third_path_two_two()
#     elif Path_16 == "3":
#         print("")
#         print("")
#         third_path_three_three()

# def third_path_two():
#     print("")
#     print("")
#     Path_17 = input("which path will go down?: 1\n 2\n 3")
#     if Path_17 == "1":
#         print("")
#         print("")
#         third_path_one_one()
#     elif Path_17 == "2":
#         print("")
#         print("")
#         third_path_two_two()
#     elif Path_17 == "3":
#         print("")
#         print("")
#         third_path_three_three()

# def third_path_three():
#     print("")
#     print("")
#     Path_18 = input("which path will go down?: 1\n 2\n 3")
#     if Path_18 == "1":
#         print("")
#         print("")
#         third_path_one_one()
#     elif Path_18 == "2":
#         print("")
#         print("")
#         third_path_two_two()
#     elif Path_18 == "3":
#         print("")
#         print("")
#         third_path_three_three()

# def third_path_one_one():
#     print("")
#     print("")
#     Path_19 = input("which path will go down?: 1\n 2\n 3")
#     if Path_19 == "1":
#         print("")
#         print("")
#         third_path_one_one_one()
#     elif Path_19 == "2":
#         print("")
#         print("")
#         third_path_two_two_two()
#     elif Path_19 == "3":
#         print("")
#         print("")
#         third_path_three_three_three()

# def third_path_two_two():
#     print("")
#     print("")
#     Path_20 = input("which path will go down?: 1\n 2\n 3")
#     if Path_20 == "1":
#         print("")
#         print("")
#         third_path_one_one_one()
#     elif Path_20 == "2":
#         print("")
#         print("")
#         third_path_two_two_two()
#     elif Path_20 == "3":
#         print("")
#         print("")
#         third_path_three_three_three()

# def third_path_three_three():
#     print("")
#     print("")
#     Path_21 = input("which path will go down?: 1\n 2\n 3")
#     if Path_21 == "1":
#         print("")
#         print("")
#         third_path_one_one_one()
#     elif Path_21 == "2":
#         print("")
#         print("")
#         third_path_two_two_two()
#     elif Path_21 == "3":
#         print("")
#         print("")
#         third_path_three_three_three()

# def third_path_one_one_one():
#     print("")
#     print("")
#     Dark_Lord()

# def third_path_two_two_two():
#     print("")
#     print("")
#     Dark_Lord()

# def third_path_three_three_three():
#     print("")
#     print("")
#     Dark_Lord()

def Start_over(character):
    Play_Again = input("would you like to play again? [Y/N]:")
    if Play_Again.casefold() == "y":
        player_one()
        backstory()
        time.sleep(2)
        heroselect()
        enemy_select(zombie, vampire, werewolf)
        battle(character)
        Start_over(character)
    else:
        Play_Again.casefold() == "n"
        print("Thank you for playing")


def MainScreenOptions():
    MainScreen()
    Choice = input("what do you want to do:")
    if Choice == ("play"):
        character = heroselect()
        age()
        backstory()
        player_one()
        time.sleep(2)

        enemy_select(zombie, vampire, werewolf)
        battle(character)
        Start_over(character)
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
