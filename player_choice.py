from random import randint


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


class Werewolf(object):
    name = "werewolf"
    health = 100
    attack = 55
    defense = 35
