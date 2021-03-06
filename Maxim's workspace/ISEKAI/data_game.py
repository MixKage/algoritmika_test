from time import *
from colorama import Fore

logo_text = """
████████████████████████████████████████████
█      █    █     █  ███   █       █      ██
███  ███  ███  ████  █   ███  ███  ███  ████
███  ███    █     █    █████       ███  ████
███  █████  █  ████  █   ███  ███  ███  ████
█      █    █     █  ███   █  ███  █      ██
████████████████████████████████████████████

        ██    ██ ███████ ██    ██ █████ ██    ██ ████████
        ███  ███ ██   ██ ███  ███ ██    ████  ██    ██
        ██ ██ ██ ██   ██ ██ ██ ██ █████ ██  ████    ██
        ██    ██ ██   ██ ██    ██ ██    ██    ██    ██
        ██    ██ ███████ ██    ██ █████ ██    ██    ██"""

soon_text = """
██████ ███████ ███████ ██    ██
███    ██   ██ ██   ██ ████  ██
██████ ██   ██ ██   ██ ██  ████
   ███ ██   ██ ██   ██ ██    ██
██████ ███████ ███████ ██    ██
"""

version = "2betafb"

def DRAWline(mark, sym):
    if mark == 1:
        line="┌"
        for i in range(sym):
            line += "─"
        line += "┐"
    elif mark == 2:
        line="└"
        for i in range(sym):
            line += "─"
        line += "┘"
    return line

def logo():
    print(f"\n{logo_text}\n\n ✉  {Fore.LIGHTRED_EX+version}"); sleep(0.25)

# GAME GAME GAME GAME GAME GAME GAME GAME GAME GAME GAME GAME 
weapons = ["sword", "bow", "longsword", "battle axe"]

location1_monsters = ["Волк", "Заяц", "Медведь", "Белка", "Леший"]

# stats = hp, lvl, damage, defense%  |   loot = coins, item
# first location  
wolf = ["500", "2", "100", 20]; wolf_loot = [80, "Зуб Волка"] 
rabbit = ["100", "0", "25", 50]; rabbit_loot = [10, "Шубка Зайца"]
bear = ["850", "4", "200", 5]; bear_loot = [200, "Когти Медведя"]
squirrel = ["150", "1", "25", 60]; squirrel_loot = [25, "Орех"] 
silvan = ["1200", "8", "500", 0]