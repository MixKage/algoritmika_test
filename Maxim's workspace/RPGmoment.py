from ast import While
from colorama import *
from random import *
from time import *
import data_game
import sound_play
import turtle

version = "1betafl"

hp = 0
lvl = 0
coins = 0
damage = 0
defense = 0
location = 0

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
    print(Fore.WHITE + "┌──────────────────────┐ \n├ 1. " + Fore.LIGHTCYAN_EX + "Играть" + Fore.WHITE + "            │")
    print("├ 2. " + Fore.LIGHTCYAN_EX + "Настройки" + Fore.WHITE + "         │")
    print("├ 3. " + Fore.LIGHTCYAN_EX + "FAQ" + Fore.WHITE + "               │")
    print("├ 4. " + Fore.LIGHTCYAN_EX + "Прочее" + Fore.WHITE + "            │")
    print("├ 5. " + Fore.LIGHTCYAN_EX + "Выход" + Fore.WHITE + "             │")
    print("└─────┐" + "────────────────┘")
    question = int(input("      │ Выбор: "))
    print("\n"*50)
    return question


def road_generator(): # Генератор, Спасибо MixKage
    road = Fore.WHITE + '│ '
    for i in range(30):
        rand = randint(0, 65)
        if rand == 14:
            road += Fore.LIGHTBLACK_EX + '⌓'
        else:
            road += Fore.WHITE + ' '
    road += Fore.WHITE + ' │'
    print(road)


def first_location(): # Первая локация, 5 монстров
    global location; location = 1
    global coins
    global damage
    global hp
    rand = randint(0,12)
    
    if rand == 8:
        road_generator()
        road_generator()
        print("│ " + Fore.LIGHTBLACK_EX + "⌓" + Fore.WHITE + "          " + Fore.BLUE + "/" + Fore.WHITE + "       " + Fore.LIGHTBLACK_EX + "⌓" + Fore.WHITE + "           │")
        print("│           " + Fore.BLUE + "/-" + Fore.WHITE + "                   │")
        print("│          " + Fore.BLUE + "/" + Fore.WHITE + "      " + Fore.LIGHTBLACK_EX + "⌓" + Fore.WHITE + "              │")
        road_generator()
        road_generator()
        print("\n┌───────────────────────────┐" + Fore.WHITE + "\n│ Вы нашли Палку! " + Fore.LIGHTRED_EX + "+20" + Fore.WHITE + " урона.   ")
        damage += 20
        sleep(0.25)
        print("│ Теперь у вас " + Fore.LIGHTRED_EX + f"{damage}" + Fore.WHITE + " урона \n└───────────────────────────┘\n")
        sleep(3)
        true = 1
    elif rand == 3:
        sleep(0.5)
        road_generator()
        road_generator()
        road_generator()
        road_generator()
        print("│     " + Fore.LIGHTBLACK_EX + "⌓" + Fore.WHITE + "         ⌒           " + Fore.LIGHTBLACK_EX + "⌓" + Fore.WHITE + "    │")
        road_generator()
        print("\n┌───────────────────────────┐" + Fore.WHITE + "\n│ Вы споткнулись об кочку и упали! " + Fore.LIGHTRED_EX + "-25" + Fore.WHITE+ " здоровья   "); hp -= 25
        sleep(0.25)
        print("│ Теперь у вас " + Fore.LIGHTRED_EX + f"{hp}" + Fore.WHITE + " здоровья \n└───────────────────────────┘\n")
        sleep(3)
    elif rand == 1:
        sleep(0.5)
        road_generator()
        road_generator()
        print("│          " + Fore.YELLOW + "℗" + Fore.WHITE + "           " + Fore.LIGHTBLACK_EX + "⌓" + Fore.WHITE + "         │")
        road_generator()
        road_generator()
        sleep(0.5)
        print("\n┌───────────────────────────┐" + Fore.WHITE + "\n│ Вы нашли Монету! " + Fore.LIGHTRED_EX + "+25" + Fore.WHITE+ " монет   "); coins += 25
        sleep(0.25)
        print("│ Теперь у вас " + Fore.LIGHTRED_EX + f"{coins}" + Fore.WHITE + " монет \n└───────────────────────────┘\n")
        sleep(3)
    elif rand == 12:
        battle()
    else:
        for i in range(5):
            road_generator()
            road_generator()
            road_generator()
            road_generator()
            road_generator()
            sleep(0.5)

def battle():
    if location == 1:
        rand = randint(0, 5)
        sleep(2)
        if rand >= 0 and rand <= 5: # Волк
            print("\n┌──────────────────────┐\n├ Вы встретили " + Fore.LIGHTRED_EX + f"{data_game.location1_monsters[0]}") 
            print(Fore.WHITE +f"├ ○ {Fore.LIGHTRED_EX+data_game.wolf[1]}"+Fore.WHITE+f"  ♥ {Fore.LIGHTRED_EX+data_game.wolf[0]}"+Fore.WHITE+f"  ➹ {Fore.LIGHTRED_EX+data_game.wolf[2]}\n")

def show_parameters():
    print(Fore.WHITE + "   ●  ├ У тебя         │\n      ├────────────────┤")
    sleep(0.5)
    print("   ○  ├ " + Fore.LIGHTRED_EX + "{0}".format(lvl) + Fore.BLACK + " уровень\n      " + Fore.WHITE + "│")
    sleep(0.5)
    print("   ♥  ├ " + Fore.LIGHTRED_EX + "{0}".format(hp) + Fore.BLACK + " здоровья\n      " + Fore.WHITE + "│")
    sleep(0.5)
    print(Fore.WHITE + "   ℗  ├ " + Fore.LIGHTRED_EX + "{0}".format(coins) + Fore.BLACK + " монеты\n      " + Fore.WHITE + "│")
    sleep(0.5)
    print(Fore.WHITE + "   ➹  ├ " + Fore.LIGHTRED_EX + "{0}".format(damage) + Fore.BLACK + " урон\n      " + Fore.WHITE + "│")
    sleep(0.5)
    print(Fore.WHITE + "   ☯  ├ " + Fore.LIGHTRED_EX + "{0}%".format(defense) + Fore.BLACK + " защита")
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
    # sound_play.first_music()
    logo()

    sleep(1)

    question = starter_game_menu()
    while question != 5:
        if question == 1:
            iGame(randint(700, 1000), 0, randint(0, 100), randint(25, 100), randint(0, 50))
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

                            print(Fore.WHITE + "\n┌────────────────────────┐\n├ На табличке написанно.")

                            print("│ ← Лес      ↑ Деревня \n├ Куда мы дальше отправимся?\n├────────────────────────┤\n│ 1." + Fore.LIGHTCYAN_EX + " Леc                 " + Fore.WHITE + "│")
                            print("│ 2." + Fore.LIGHTCYAN_EX + " Деревня             " + Fore.WHITE + "│")
                            print("├────────────────────────┘")
                            sleep(1)
                            question = int(input(Fore.WHITE + "│ " + Fore.BLACK + " ☦ " + Fore.WHITE + " От " + Fore.LIGHTRED_EX + " ВАС " + Fore.WHITE + " зависит " + Fore.LIGHTRED_EX + " ЕГО СУДЬБА: "))
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
