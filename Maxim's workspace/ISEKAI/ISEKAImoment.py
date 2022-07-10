from colorama import *
from random import *
from time import *
from data_game import *
import sound_play
from game_events import *


hp = 0
lvl = 0
coins = 0
damage = 0
defense = 0
location = 0

# def logo_old():
    # print("\n"+" "*26+"_/_/_/    _/_/_/      _/_/_/")
    # sleep(0.25)
    # print(" "*25+"_/    _/  _/    _/  _/")
    # sleep(0.25)
    # print(" "*24+"_/_/_/    _/_/_/    _/  _/_/")
    # sleep(0.25)
    # print(" "*23+"_/    _/  _/        _/    _/")
    # sleep(0.25)
    # print(" "*22+"_/    _/  _/          _/_/_/\n")
    # sleep(0.25)
    # print(" "*23+"_ _  _  _ _  _  _ _|_")
    # sleep(0.25)
    # print(" "*22+f"| | |(_)| | |(/_| | |  ✉  {Fore.LIGHTRED_EX+version}")
    


def starter_game_menu():
    print(f"{Fore.WHITE}{DRAWline(1,27)}\n├ 1. {Fore.LIGHTCYAN_EX}Играть{Fore.WHITE}                 │")
    print(f"├ 2. {Fore.LIGHTCYAN_EX}Настройки{Fore.WHITE}              │")
    print(f"├ 3. {Fore.LIGHTCYAN_EX}FAQ{Fore.WHITE}                    │")
    print(f"├ 4. {Fore.LIGHTCYAN_EX}История{Fore.WHITE}                │")
    print(f"├ 5. {Fore.LIGHTCYAN_EX}Выход{Fore.WHITE}                  │")
    print("└─────┐─────────────────────┘")
    question = int(input("      │ Выбор: "))
    print("\n"*50)
    return question


def road_generator(num): # Генератор, Спасибо MixKage
    for i in range(num):
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
    rand = randint(0,20)
    
    if rand == 8:
        road_generator(2)
        print(f"│ {Fore.LIGHTBLACK_EX}⌓{Fore.WHITE}          {Fore.BLUE}/{Fore.WHITE}       {Fore.LIGHTBLACK_EX}⌓{Fore.WHITE}           │")
        print(f"│           {Fore.BLUE}/-{Fore.WHITE}                   │")
        print(f"│          {Fore.BLUE}/{Fore.WHITE}      {Fore.LIGHTBLACK_EX}⌓{Fore.WHITE}              │")
        road_generator(2)
        print(f"\n{DRAWline(1,27)}{Fore.WHITE}\n│ Вы нашли Палку! {Fore.LIGHTRED_EX}+20{Fore.WHITE} урона.   ")
        damage += 20
        sleep(0.25)
        print(f"│ Теперь у вас {Fore.LIGHTRED_EX}{damage}{Fore.WHITE} урона \n{DRAWline(2,27)}\n")
        sleep(3)
        true = 1
    elif rand == 3:
        sleep(0.5); road_generator(4)
        print(f"│     {Fore.LIGHTBLACK_EX}⌓{Fore.WHITE}         ⌒           {Fore.LIGHTBLACK_EX}⌓{Fore.WHITE}    │"); road_generator(2)
        print(f"\n{DRAWline(1,27)}{Fore.WHITE}\n│ Вы споткнулись об кочку и упали! {Fore.LIGHTRED_EX}-25{Fore.WHITE} здоровья   "); hp -= 25; sleep(0.25)
        print(f"│ Теперь у вас {Fore.LIGHTRED_EX}{hp}{Fore.WHITE} здоровья \n{DRAWline(2,27)}\n"); sleep(3)
    elif rand == 1:
        sleep(0.5); road_generator(2)
        print(f"│          {Fore.YELLOW}℗{Fore.WHITE}           {Fore.LIGHTBLACK_EX}⌓{Fore.WHITE}         │"); road_generator(2); sleep(0.5)
        print(f"\n{DRAWline(1,27)}{Fore.WHITE}\n│ Вы нашли Монету! {Fore.LIGHTRED_EX}+25{Fore.WHITE} монет   "); coins += 25; sleep(0.25)
        print(f"│ Теперь у вас {Fore.LIGHTRED_EX}{coins}{Fore.WHITE} монет \n{DRAWline(2,27)}\n"); sleep(3)
    elif rand == 12:
        battle()
    else:
        for i in range(3):
            road_generator(5)
            sleep(0.4)

def battle(): #битва
    if location == 1:
        rand = randint(0, 5) 
        sleep(2)
        if rand >= 0 and rand <= 5: # Волк
            print(f"\n{DRAWline(1,27)}\n├ Вы встретили {Fore.LIGHTRED_EX}{location1_monsters[0]}") 
            print(f"{Fore.WHITE}├ ○ {Fore.LIGHTRED_EX+wolf[1]}{Fore.WHITE}  ♥ {Fore.LIGHTRED_EX+wolf[0]}{Fore.WHITE}  ➹ {Fore.LIGHTRED_EX+wolf[2]}")
            print(f"{Fore.WHITE}└─────┐─────────────────────┘")
            question = input(f"      │ {Fore.CYAN} Попытка побега? {Fore.WHITE} (да/нет) ").lower()
            if question == "да":
                print(f"      │\n      │ {Fore.CYAN} Пробуем...")
                rand = randint(0,50)
                sleep(2)
                if rand >= 0 and rand <= 8:
                    print(f"{Fore.WHITE}      │\n      │ {Fore.CYAN}Получилось!") 
                    sound_play.success_sound(False); sleep(2); pass
                else:
                    print(f"{Fore.WHITE}      │\n      │ {Fore.CYAN} Неудача!")
                    sound_play.failure_sound(False); sleep(2)
                    battle("Волк")


def show_parameters(): # статы
    print(f"{Fore.WHITE}   ●  ├ У тебя         │\n      ├────────────────┤")
    sleep(0.5)
    print(f"   ○  ├ {Fore.LIGHTRED_EX}{lvl}{Fore.BLACK} уровень\n      {Fore.WHITE}│")
    sleep(0.5)
    print(f"   ♥  ├ {Fore.LIGHTRED_EX}{hp}{Fore.BLACK} здоровья\n      {Fore.WHITE}│")
    sleep(0.5)
    print(f"   ℗  ├ {Fore.LIGHTRED_EX}{coins}{Fore.BLACK} монеты\n      {Fore.WHITE}│")
    sleep(0.5)
    print(f"   ➹  ├ {Fore.LIGHTRED_EX}{damage}{Fore.BLACK} урон\n      {Fore.WHITE}│")
    sleep(0.5)
    print(f"   ☯  ├ {Fore.LIGHTRED_EX}{defense}%{Fore.BLACK} защита    {Fore.WHITE}")
    sleep(0.5)


def iGame(iHp, iLvl, iCoins, iDMG, iDEF): # инициальзация
    global hp; hp = iHp
    global lvl; lvl = iLvl
    global coins; coins = iCoins
    global damage; damage = iDMG
    global defense; defense = iDEF

    show_parameters()


def main():
    sound_play.first_music(False)
    logo()

    sleep(1)

    question = starter_game_menu()
    while question != 5:
        if question == 1:
            iGame(randint(700, 1000), 0, randint(0, 100), randint(25, 100), randint(0, 50))
            question = input("──────┼"+"─"*35+f"\n   ➱  │ ВВЕДИТЕ {Fore.LIGHTRED_EX}СТАРТ{Fore.WHITE} ДЛЯ НАЧАЛА: ").lower()
            if question == "старт":
                print("\n"*50)
                while True:
                    true = 0
                    for i in range(15):
                        first_location()
                        if i == 14:
                            print("\n"*50)
                            show_parameters()
                            print(f"{Fore.WHITE}\n{DRAWline(1,27)}\n├ На табличке написанно.")
                            print("│ ← Лес      ↑ Деревня \n├ Куда мы дальше отправимся?\n├"+"─"*24+f"\n│ 1.{Fore.LIGHTCYAN_EX} Леc {Fore.WHITE}")
                            print(f"│ 2.{Fore.LIGHTCYAN_EX} Деревня {Fore.WHITE}")
                            print("├───────────────────────────┘"); sleep(1)
                            question = int(input(f"{Fore.WHITE}│ {Fore.BLACK} ☦ {Fore.WHITE} От {Fore.LIGHTRED_EX} ВАС {Fore.WHITE} зависит {Fore.LIGHTRED_EX} ЕГО СУДЬБА: "))
                            break
        elif question == 2: print(f"{Fore.LIGHTCYAN_EX}{soon_text}\n\n"*10)
        elif question == 3: print(f"{Fore.LIGHTCYAN_EX}1. Игра на одном дыхании сохранений нет.\n пока всё"+"\n"*50)
        elif question == 4: print(f"{Fore.LIGHTCYAN_EX}{soon_text}\n\n"*10)
        sleep(3)
        question = starter_game_menu()


if __name__ == '__main__':
    main()
