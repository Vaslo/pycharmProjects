# import actors
from actors import Wizard, Creature

def main():
    print_header()
    game_loop()


def print_header():
    print("-------------------------------")
    print("      WIZARD GAME APP")
    print("-------------------------------")


def game_loop():
    creatures = [
        Creature(),
        Creature(),
        Creature(),
        Creature(),
        Creature()
    ]

    hero = Wizard()

    while True:
        cmd = input("Do you [a]ttack, [r]unaway, [l]ook around?")
        if cmd == "a":
            print("attack")
        elif cmd == "r":
            print("runaway")
        elif cmd == "l":
            print("look around")
        else:
            print("Ok, exiting game game - BYE!")
            break


if __name__ == '__main__':
    main()
