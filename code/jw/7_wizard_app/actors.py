import random


class Wizard:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def attack(self, creature):
        print("The wizard {} attacks {}!".format(
            self.name, creature.name
        ))

        my_roll = random.randint(1, 12 ) * self.level
        creature_roll

class Creature:
    # level
    # name

    def __init__(self, name, level):
        self.name = name
        self.level = level
