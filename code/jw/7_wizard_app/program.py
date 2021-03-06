import random

import time
from actors import Wizard, Creature, SmallAnimal, Dragon


def print_header():
    print('----------------------------------')
    print('-----      DARK FOREST       -----')
    print('----------------------------------')
    print('')


def game_loop():
    creatures = [
        SmallAnimal('Toad',1),
        SmallAnimal('Tiger', 10),
        SmallAnimal('Bat', 3),
        Dragon('Dragon', 250, 100, True),
        Wizard('Evil Wizard', 1000)
    ]

    hero = Wizard('Gandalf', 75)

    while True and len(creatures) > 0:
        print()
        active_creature = random.choice(creatures)
        print('A {} of level {} has appeared from a dark and foggy forest ...'
              . format(active_creature.name, active_creature.level))
        print()

        cmd = input('Do you [a]ttack. [r]un away or [l]ook around? ')
        cmd = cmd.lower().strip()

        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                time.sleep(5)
        elif cmd == 'r':
            print('The wizard has become unsure of his power and flees')
        elif cmd == 'l':
            print('The wizard takes in the beautiful surroundings and sees ...')
            for c in creatures:
                print(' * A {} of level {}' . format(c.name, c.level))
                time.sleep(1)
        else:
            break

        if not creatures:
            print('You have defeated all the creatures. Well Done!')

def main():
    print_header()
    game_loop()


if __name__ == '__main__':
    main()
