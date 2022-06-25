from colorama import Fore, Back, Style
from random import *
from time import * 

hp = 0
lvl = 0
coins = 0
damage = 0
defense = 0



def logo():
    print(Fore.WHITE + "                                                                           ");sleep(0.25);print("                          _/_/_/    _/_/_/      _/_/_/                     ")
    sleep(0.25)
    print("                         _/    _/  _/    _/  _/                            ");sleep(0.25);print("                        _/_/_/    _/_/_/    _/  _/_/                       ")
    sleep(0.25)
    print("                       _/    _/  _/        _/    _/                        ");sleep(0.25);print("                      _/    _/  _/          _/_/_/                         ")
    sleep(0.25)
    print("                                                                           ")
    sleep(0.25)
    print("                                             _ _  _  _ _  _  _ _|_         ");sleep(0.45);print("                                            | | |(_)| | |(/_| | |          ")

def starter_game_menu():
    print(Fore.WHITE + "┌──────────────────────┐ \n├ 1. " + Fore.LIGHTCYAN_EX + "Играть" + Fore.WHITE + "            │")
    print("├ 2. " + Fore.LIGHTCYAN_EX + "Настройки" + Fore.WHITE + "         │") 
    print("├ 3. " + Fore.LIGHTCYAN_EX + "FAQ" + Fore.WHITE + "               │")
    print("├ 4. " + Fore.LIGHTCYAN_EX + "Выход" + Fore.WHITE + "             │")
    print("└─────┐" + "────────────────┘")
    question = int(input("      │ Выбор: "))
    print("\n"*50)
    return question


def show_parameters():
    print(Fore.WHITE + "   ●  ├ У тебя         │\n      ├────────────────┤")
    sleep(0.5)
    print("   ○  ├ " + Fore.LIGHTRED_EX + "{0}".format(lvl) + Fore.BLACK + " уровень\n      " + Fore.WHITE + "│")
    sleep(0.5)
    print("   ●  ├ " + Fore.LIGHTRED_EX + "{0}".format(hp) + Fore.BLACK + " здоровья\n      " + Fore.WHITE + "│")
    sleep(0.5)
    print(Fore.WHITE + "   ○  ├ " + Fore.LIGHTRED_EX + "{0}".format(coins) + Fore.BLACK + " монеты\n      " + Fore.WHITE + "│")
    sleep(0.5)
    print(Fore.WHITE + "   ●  ├ " + Fore.LIGHTRED_EX + "{0}".format(damage) + Fore.BLACK + " урон\n      " + Fore.WHITE + "│")
    sleep(0.5)
    print(Fore.WHITE + "   ○  ├ " + Fore.LIGHTRED_EX + "{0}".format(defense) + Fore.BLACK + " защита")
    sleep(0.5)

def iGame(iHp, iLvl, iCoins, iDMG, iDEF):
    global hp; hp = iHp
    global lvl; lvl = iLvl
    global coins; coins = iCoins
    global damage; damage = iDMG
    global defense; defense = iDEF
    
    show_parameters()

logo()

sleep(1)

question = starter_game_menu()
if question == 1:
    iGame(randint(500,1000), 0, randint(0,250), randint(25,100), randint(0,150))
    question = input(Fore.WHITE + "──────┼───────────────────────────────────\n   ➱  │ ВВЕДИТЕ " + Fore.LIGHTRED_EX + Style.DIM + "СТАРТ" + Fore.WHITE + Style.NORMAL + " ДЛЯ НАЧАЛА: ")
    if question == "старт":   
        while True:
            for i in range(10):
                rand = randint(0,2)
                if rand == 0:
                    print("│       ●               |\n│ ●               ●     |")
                    print("│                       |\n│                     ● |")
                    print("│              ●        |\n│             ●         |")
                    print("│   ●                   |\n│                       |")
                    print("│            ●          |\n│                    ●  |")
                    print("│                       |\n│        ●              |")
                    sleep(0.25)
                elif rand == 1:
                    print("│                  ●    |\n│       ●             ● |")
                    print("│     ●                 |\n│             ●         |")
                    print("│                     ● |\n│                       |")
                    print("│               ●       |\n│●                      |")
                    print("│    ●                  |\n│                    ●  |")
                    print("│          ●            |\n│     ●                 |")
                    sleep(0.25)
                elif rand == 2:
                    print("│       ●               |\n│●               ●      |") 
                    print("│                       |\n│         ●             |")
                    print("│●                ●     |\n│  ●         ●          |")                                       
                    print("│          ●            |\n│                  ●    |")
                    print("│                  ●    |\n│                       |")
                    print("│       ●               |\n│ ●               ●     |")
                    sleep(0.25)
            break
sleep(3)

