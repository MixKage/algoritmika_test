from colorama import Fore, Back, Style
from random import *
from time import * 

# Оh, colorama? - Andrey, Your opponent

version = "1betafl"

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
    print("                       _/    _/  _/        _/    _/                        ");sleep(0.25);print("                      _/    _/  _/          _/_/_/                         \n")
    sleep(0.25)
    print("                                             _ _  _  _ _  _  _ _|_         ");sleep(0.25);print("                                            | | |(_)| | |(/_| | |          ")
    sleep(0.5)
    print(f" ✉  version - {version}              ")

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

def first_location():
    global var
    global coins
    global damage
    global hp
    rand = randint(0,15)
    if rand == 0:
        sleep(0.5)
        print("│       ●               |\n│ ●               ●     |")
        print("│                       |\n│                     ● |")
        print("│              ●        |\n│             ●         |")
        print("│   ●                   |\n│                       |")
        print("│            ●          |\n│                    ●  |")
        print("│                       |\n│        ●              |")
        sleep(0.5)
    elif rand == 1:
        sleep(0.5)
        print("│                  ●    |\n│       ●             ● |")
        print("│     ●                 |\n│             ●         |")
        print("│                     ● |\n│                       |")
        print("│               ●       |\n│●                      |")
        print("│    ●                  |\n│                    ●  |")
        print("│          ●            |\n│     ●                 |")   
        sleep(0.5)
    elif rand == 2:
        sleep(0.5)
        print("│       ●               |\n│●               ●      |") 
        print("│                       |\n│         ●             |")
        print("│●                ●     |\n│  ●         ●          |")                                       
        print("│          ●            |\n│                  ●    |")
        print("│                  ●    |\n│                       |")
        print("│       ●               |\n│ ●               ●     |")
        sleep(0.5)
    elif rand >= 3 and rand <= 5:
        sleep(0.5)
        if var == 0:
            print("│●                ●     |\n│  ●         ●          |")   
            print("│                       |\n│         ●             |") 
            print("│          " + Fore.BLUE + "○" + Fore.WHITE + "            |") 
            print("│ ●       " + Fore.BLUE + "/" + Fore.WHITE + "       ●     |")                                  
            print("│        " + Fore.BLUE + "/" + Fore.WHITE + "              |") 
            print("│       " + Fore.BLUE + "/" + Fore.WHITE + "      ●        |")
            print("│                  ●    |\n│                       |")
            print("│       ●               |\n│●               ●      |")
            sleep(0.5)
            print("\n┌───────────────────────────┐" + Fore.WHITE + "\n│ Вы нашли Палку! " + Fore.LIGHTRED_EX + "+20" + Fore.WHITE+ " урона.   "); damage += 20
            sleep(0.25)
            print("│ Теперь у вас " + Fore.LIGHTRED_EX + f"{damage}" + Fore.WHITE + " урона \n└───────────────────────────┘\n")
            sleep(3)
        elif var != 0:
            sleep(0.5)
        print("│                  ●    |\n│       ●             ● |")
        print("│     ●                 |\n│             ●         |")
        print("│                     ● |\n│                       |")
        print("│               ●       |\n│●                      |")
        print("│    ●                  |\n│                    ●  |")
        print("│          ●            |\n│     ●                 |")   
        sleep(0.5)
        var = 1
    elif rand >= 6 and rand <= 7:
        sleep(0.5)
        print("│                  ●    |\n│       ●             ● |")
        print("│     ●                 |\n│             ●         |")
        print("│                     ● |\n│                       |")
        print("│               ●       |\n│●                      |")
        print("│    ●                  |\n│                    ●  |")
        print("│          ●            |\n│     ●                 |") 
        print("\n┌───────────────────────────┐" + Fore.WHITE + "\n│ Вы упали! " + Fore.LIGHTRED_EX + "-35" + Fore.WHITE+ " здоровья.   "); hp -= 35
        sleep(0.25)
        print("│ Теперь у вас " + Fore.LIGHTRED_EX + f"{hp}" + Fore.WHITE + " здоровья \n└───────────────────────────┘\n")
        sleep(3)
    elif rand >= 8 and rand <= 10:
        sleep(0.5)
        print("│●                ●     |\n│  ●         ●          |")   
        print("│                       |\n│         ●             |") 
        print("│          " + Fore.YELLOW + "○" + Fore.WHITE + "            |") 
        print("│ ●              ●      |")                                  
        print("│                       |") 
        print("│                       |")
        print("│                  ●    |\n│                       |")
        print("│       ●               |\n│●               ●      |")
        sleep(0.5)
        print("\n┌───────────────────────────┐" + Fore.WHITE + "\n│ Вы нашли Монету! " + Fore.LIGHTRED_EX + "+25" + Fore.WHITE+ " монет.   "); coins += 25
        sleep(0.25)
        print("│ Теперь у вас " + Fore.LIGHTRED_EX + f"{coins}" + Fore.WHITE + " монет. \n└───────────────────────────┘\n")
        sleep(3)

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
while question != 5:
    if question == 1:
        iGame(randint(500,1000), 0, randint(0,250), randint(25,100), randint(0,150))
        question = input(Fore.WHITE + "──────┼───────────────────────────────────\n   ➱  │ ВВЕДИТЕ " + Fore.LIGHTRED_EX + Style.DIM + "СТАРТ" + Fore.WHITE + Style.NORMAL + " ДЛЯ НАЧАЛА: ")
        if question == "старт":
            print("\n"*50)   
            while True:
                print("")
                var = 0
                for i in range(15):
                    first_location()
                    if i == 14:
                        print("\n\nМы дошли до поворота. \n")
                        sleep(0.5)
                        print("Куда мы дальше отправимся?\n┌────────────────────────┐\n| 1." + Fore.LIGHTCYAN_EX + " Леc                 " + Fore.WHITE + "|")
                        print("| 2." + Fore.LIGHTCYAN_EX + " Деревня             " + Fore.WHITE + "|")
                        print("├────────────────────────┘")
                        question = int(input("| Выбор: "))
                        break
    elif question == 2:
        print(Fore.LIGHTCYAN_EX + "Их пока нет.\n"*50)  
    elif question == 3:
        print(Fore.LIGHTCYAN_EX + "1. Игра на одном дыхании сохранений нет.\n пока всё\n\n")             
    sleep(3)     
    question = starter_game_menu()            

# hey, I dont think my game can compare to THIS - Andrey, Your opponent?
# by the way, your game is pretty cool! - Just Andrey