class hero:
    def __init__(self, name, health, attack, speed, magic_points):
        self.name = name
        self.health = health
        self.attack = attack
        self.speed = speed
        self.magic_points = magic_points
        print(name, health, attack, speed, magic_points)


def print_hero_discription(name, health, attack, speed, magic_points):
    print(name, health, attack, speed, magic_points)


def print_heroes():
    print_hero_discription("Warrior", "Health = 100", "Attack = 50",
                           "Speed = 20", "Magic points = 25")
    print_hero_discription("Archer", "Health = 100", "Attack = 35",
                           "Speed = 50", "Magic points = 75")
    print_hero_discription("Mage", "Health = 100", "Attack = 25",
                           "Speed = 35", "Magic points = 100")

# class monster:
#     def __init__(self, )


# Character_1 = hero("Warrior", "Health = 100", "Attack = 50",
#                    "Speed = 20", "Magic points = 25")
# Character_2 = hero("Archer", "Health = 100", "Attack = 35",
#                    "Speed = 50", "Magic points = 75")
# Character_3 = hero("Mage", "Health = 100", "Attack = 25",
#                    "Speed = 35", "Magic points = 100")
