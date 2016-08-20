import random


class Creature:
    # level
    # name

    def __init__(self, name, level):
        self.name = name
        self.level = level

    def get_defensive_roll(self):
        return random.randint(1, 12) * self.level


class Wizard(Creature):
    # def __init__(self, name, level):
    #     super().__init__(name, level)

    def attack(self, creature):
        print("The wizard {} attacks {}!".format(
            self.name, creature.name
        ))

        my_roll = self.get_defensive_roll()
        creature_roll = self.get_defensive_roll()

        print("You roll {} ...".format(my_roll))
        print("The {} rolls {} ...".format(creature.name, creature_roll))

        if my_roll >= creature_roll:
            print("The wizard has handily TRIUMPHED over {}".format(creature.name))
            return True;
        else:
            print("The wizard has been DEFEATED :(")
            return False


class Dragon:
    pass
