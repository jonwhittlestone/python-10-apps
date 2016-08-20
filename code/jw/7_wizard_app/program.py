import random

from actors import Wizard, Creature


def print_header():
    print('----------------------------------')
    print('-----       DARK ROOM        -----')
    print('----------------------------------')
    print('')


def game_loop():
    creatures = [
        Creature('Toad',1),
        Creature('Tiger', 10),
        Creature('Bat', 3),
        Creature('Dragon', 50),
        Creature('Evil Wizard', 1000)
    ]

    hero = Wizard('Gandalf', 75)

    while True:
        active_creature = random.choice(creatures)
        print('A {} of level {} has appeared from a dark and foggy forest ...'
              . format(active_creature.name, active_creature.level))
        print()

        cmd = input('Do you [a]ttack. [r]un away or [l]ook around? ')
        cmd = cmd.lower().strip()

        if cmd == 'a':
            hero.attack(active_creature)
        elif cmd == 'r':
            print('Run Away!')
        elif cmd == 'l':
            print('Look Around.')
        else:
            break


def main():
    print_header()
    game_loop()


if __name__ == '__main__':
    main()
