from colorama import Fore, Style
from random import *
from time import *
import data_game
import turtle

version = "1betafl"

hp = 0
lvl = 0
coins = 0
damage = 0
defense = 0


def logo():
    print(Fore.WHITE + "                                                                           ")
    sleep(0.25)
    print("                          _/_/_/    _/_/_/      _/_/_/                     ")
    sleep(0.25)
    print("                         _/    _/  _/    _/  _/                            ")
    sleep(0.25)
    print("                        _/_/_/    _/_/_/    _/  _/_/                       ")
    sleep(0.25)
    print("                       _/    _/  _/        _/    _/                        ")
    sleep(0.25)
    print("                      _/    _/  _/          _/_/_/                         \n")
    sleep(0.25)
    print("                                             _ _  _  _ _  _  _ _|_         ")
    sleep(0.25)
    print(
        "                                            | | |(_)| | |(/_| | |          ")
    sleep(0.5)
    print(f"\n ✉  version - {version}" + Fore.GREEN +
          "\n   EVERYTHING IS SUBJECT TO CHANGE")


def starter_game_menu():
    print(Fore.WHITE + "┌──────────────────────┐ \n├ 1. " +
          Fore.LIGHTCYAN_EX + "Играть" + Fore.WHITE + "            │")
    print("├ 2. " + Fore.LIGHTCYAN_EX + "Настройки" + Fore.WHITE + "         │")
    print("├ 3. " + Fore.LIGHTCYAN_EX + "FAQ" + Fore.WHITE + "               │")
    print("├ 4. " + Fore.LIGHTCYAN_EX + "Прочее" + Fore.WHITE + "            │")
    print("├ 5. " + Fore.LIGHTCYAN_EX + "Выход" + Fore.WHITE + "             │")
    print("└─────┐" + "────────────────┘")
    question = int(input("      │ Выбор: "))
    print("\n"*50)
    return question


def road_generator():
    road = '│ '
    for i in range(30):
        rand = randint(0, 50)
        if rand == 14:
            road += '⌓'
        else:
            road += ' '
    road += ' │'
    print(road)


def first_location():

    global true
    global coins
    global damage
    global hp
    rand = 8
    for i in range(5):
        road_generator()
        road_generator()
        road_generator()
        road_generator()
        road_generator()
        sleep(0.5)
    if rand == 8 and true != 1:
        print("│ ⌓          " + Fore.BLUE + "/" +
              Fore.WHITE + "       ⌓           │")
        print("│           " + Fore.BLUE + "/-" +
              Fore.WHITE + "                   │")
        print("│          " + Fore.BLUE + "/" +
              Fore.WHITE + "      ⌓              │")
        road_generator()
        print("\n┌───────────────────────────┐" + Fore.WHITE +
              "\n│ Вы нашли Палку! " + Fore.LIGHTRED_EX + "+20" + Fore.WHITE + " урона.   ")
        damage += 20
        sleep(0.25)
        print("│ Теперь у вас " + Fore.LIGHTRED_EX +
              f"{damage}" + Fore.WHITE + " урона \n└───────────────────────────┘\n")
        sleep(3)
        true = 1
    # if rand >= 5 and rand <= 6:
    #     sleep(0.5)
    #     if var == 0:
    #         print("│●                ●     │\n│  ●         ●          │")
    #         print("│                       │\n│         ●             │")
    #         print("│                       │")
    #         print("│ ●       " + Fore.BLUE + "/" + Fore.WHITE + "       ●     │")
    #         print("│        " + Fore.BLUE + "/-" + Fore.WHITE + "             │")
    #         print("│       " + Fore.BLUE + "/" + Fore.WHITE + "      ●        │")
    #         print("│                  ●    │\n│                       │")
    #         print("│       ●               │\n│●               ●      │")
    #         sleep(0.5)
    #         print("\n┌───────────────────────────┐" + Fore.WHITE + "\n│ Вы нашли Палку! " + Fore.LIGHTRED_EX + "+20" + Fore.WHITE+ " урона.   "); damage += 20
    #         sleep(0.25)
    #         print("│ Теперь у вас " + Fore.LIGHTRED_EX + f"{damage}" + Fore.WHITE + " урона \n└───────────────────────────┘\n")
    #         sleep(3)
    #         var = 1
    #     elif var != 0:
    #         sleep(0.5)
    #         print("│                  ●    │\n│       ●             ● │")
    #         print("│     ●                 │\n│             ●         │")
    #         print("│                     ● │\n│                       │")
    #         print("│               ●       │\n│●                      │")
    #         print("│    ●                  │\n│                    ●  │")
    #         print("│          ●            │\n│     ●                 │")
    #         sleep(0.5)
    # elif rand == 7:
    #     sleep(0.5)
    #     print("│                  ●    │\n│       ●             ● │")
    #     print("│     ●                 │\n│             ●         │")
    #     print("│                     ● │\n│                       │")
    #     print("│               ●       │\n│●                      │")
    #     print("│    ●                  │\n│                    ●  │")
    #     print("│          ●            │\n│     ●                 │")
    #     print("\n┌───────────────────────────┐" + Fore.WHITE + "\n│ Вы упали! " + Fore.LIGHTRED_EX + "-35" + Fore.WHITE+ " здоровья   "); hp -= 35
    #     sleep(0.25)
    #     print("│ Теперь у вас " + Fore.LIGHTRED_EX + f"{hp}" + Fore.WHITE + " здоровья \n└───────────────────────────┘\n")
    #     sleep(3)
    # elif rand == 8:
    #     sleep(0.5)
    #     print("│●                ●     │\n│  ●         ●          │")
    #     print("│                       │\n│         ●             │")
    #     print("│          " + Fore.YELLOW + "○" + Fore.WHITE + "            │")
    #     print("│ ●              ●      │")
    #     print("│                       │")
    #     print("│                       │")
    #     print("│                  ●    │\n│                       │")
    #     print("│       ●               │\n│●               ●      │")
    #     sleep(0.5)
    #     print("\n┌───────────────────────────┐" + Fore.WHITE + "\n│ Вы нашли Монету! " + Fore.LIGHTRED_EX + "+25" + Fore.WHITE+ " монет   "); coins += 25
    #     sleep(0.25)
    #     print("│ Теперь у вас " + Fore.LIGHTRED_EX + f"{coins}" + Fore.WHITE + " монет \n└───────────────────────────┘\n")
    #     sleep(3)


def show_parameters():
    print(Fore.WHITE + "   ●  ├ У тебя         │\n      ├────────────────┤")
    sleep(0.5)
    print("   ○  ├ " + Fore.LIGHTRED_EX +
          "{0}".format(lvl) + Fore.BLACK + " уровень\n      " + Fore.WHITE + "│")
    sleep(0.5)
    print("   ●  ├ " + Fore.LIGHTRED_EX +
          "{0}".format(hp) + Fore.BLACK + " здоровья\n      " + Fore.WHITE + "│")
    sleep(0.5)
    print(Fore.WHITE + "   ○  ├ " + Fore.LIGHTRED_EX +
          "{0}".format(coins) + Fore.BLACK + " монеты\n      " + Fore.WHITE + "│")
    sleep(0.5)
    print(Fore.WHITE + "   ●  ├ " + Fore.LIGHTRED_EX +
          "{0}".format(damage) + Fore.BLACK + " урон\n      " + Fore.WHITE + "│")
    sleep(0.5)
    print(Fore.WHITE + "   ○  ├ " + Fore.LIGHTRED_EX +
          "{0}".format(defense) + Fore.BLACK + " защита")
    sleep(0.5)


def iGame(iHp, iLvl, iCoins, iDMG, iDEF):
    global hp
    hp = iHp
    global lvl
    lvl = iLvl
    global coins
    coins = iCoins
    global damage
    damage = iDMG
    global defense
    defense = iDEF

    show_parameters()


def main():
    logo()

    sleep(1)

    question = starter_game_menu()
    while question != 5:
        if question == 1:
            iGame(randint(700, 1000), 0, randint(0, 100), randint(25, 100), 0)
            question = input(Fore.WHITE + "──────┼───────────────────────────────────\n   ➱  │ ВВЕДИТЕ " +
                             Fore.LIGHTRED_EX + Style.DIM + "СТАРТ" + Fore.WHITE + Style.NORMAL + " ДЛЯ НАЧАЛА: ").lower()
            if question == "старт":
                print("\n"*50)
                while True:
                    true = 0
                    for i in range(15):
                        first_location()
                        if i == 14:
                            print("\n"*50)
                            show_parameters()

                            print(
                                Fore.WHITE + "\n┌────────────────────────┐\n├ Мы дошли до поворота.")

                            print("│\n├ Куда мы дальше отправимся?\n├────────────────────────┤\n│ 1." +
                                  Fore.LIGHTCYAN_EX + " Леc                 " + Fore.WHITE + "│")
                            print("│ 2." + Fore.LIGHTCYAN_EX +
                                  " Деревня             " + Fore.WHITE + "│")
                            print("├────────────────────────┘")
                            sleep(1)
                            question = int(input(Fore.WHITE + "│ " + Fore.BLACK + " ☦ " + Fore.WHITE + " От " +
                                                 Fore.LIGHTRED_EX + " ВАС " + Fore.WHITE + " зависит " + Fore.LIGHTRED_EX + " ЕГО СУДЬБА: "))
                            break
        elif question == 2:
            print(Fore.LIGHTCYAN_EX + "Их пока нет.\n"*50)
        elif question == 3:
            print(Fore.LIGHTCYAN_EX +
                  "1. Игра на одном дыхании сохранений нет.\n пока всё\n\n")
        sleep(3)
        question = starter_game_menu()


if __name__ == '__main__':
    main()
