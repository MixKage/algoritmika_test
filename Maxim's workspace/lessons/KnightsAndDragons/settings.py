
# $$\   $$\           $$\           $$\        $$\                      $$$$$$\                  $$\       $$$$$$$\                                                             
# $$ | $$  |          \__|          $$ |       $$ |                    $$  __$$\                 $$ |      $$  __$$\                                                            
# $$ |$$  / $$$$$$$\  $$\  $$$$$$\  $$$$$$$\ $$$$$$\    $$$$$$$\       $$ /  $$ |$$$$$$$\   $$$$$$$ |      $$ |  $$ | $$$$$$\  $$$$$$\   $$$$$$\   $$$$$$\  $$$$$$$\   $$$$$$$\ 
# $$$$$  /  $$  __$$\ $$ |$$  __$$\ $$  __$$\\_$$  _|  $$  _____|      $$$$$$$$ |$$  __$$\ $$  __$$ |      $$ |  $$ |$$  __$$\ \____$$\ $$  __$$\ $$  __$$\ $$  __$$\ $$  _____|
# $$  $$<   $$ |  $$ |$$ |$$ /  $$ |$$ |  $$ | $$ |    \$$$$$$\        $$  __$$ |$$ |  $$ |$$ /  $$ |      $$ |  $$ |$$ |  \__|$$$$$$$ |$$ /  $$ |$$ /  $$ |$$ |  $$ |\$$$$$$\  
# $$ |\$$\  $$ |  $$ |$$ |$$ |  $$ |$$ |  $$ | $$ |$$\  \____$$\       $$ |  $$ |$$ |  $$ |$$ |  $$ |      $$ |  $$ |$$ |     $$  __$$ |$$ |  $$ |$$ |  $$ |$$ |  $$ | \____$$\ 
# $$ | \$$\ $$ |  $$ |$$ |\$$$$$$$ |$$ |  $$ | \$$$$  |$$$$$$$  |      $$ |  $$ |$$ |  $$ |\$$$$$$$ |      $$$$$$$  |$$ |     \$$$$$$$ |\$$$$$$$ |\$$$$$$  |$$ |  $$ |$$$$$$$  |
# \__|  \__|\__|  \__|\__| \____$$ |\__|  \__|  \____/ \_______/       \__|  \__|\__|  \__| \_______|      \_______/ \__|      \_______| \____$$ | \______/ \__|  \__|\_______/ 
#                         $$\   $$ |                                                                                                    $$\   $$ |                              
#                         \$$$$$$  |                                                                                                    \$$$$$$  |                              
#                          \______/                                                                                                      \______/                               

  # ___ Imports ___
import random, time



  # ___ Variables ___
HeroName = ""
BossName = "Дракон"
names = [
    "Барак Обама", "Моргенштерн", "Майкл", "Уилл", "Феня", "Алёша", "Олег", "Арнольд", 
    "Огурчик", "Кумаля", "Савеста", "Путин", "Трамп", "Тарус", "Винтаж", "Санс", "МакВин", 
    "Ochakovskiy", "Фёдор"
]



# ___ Functions ___
def randomItemList(list):
    return random.choice(list)
def rand(num1,num2):
    return random.randint(num1,num2)

# ___ Classes ___
class Hero():
    
    def __init__(self, name, hp, defense, dmg, weapon):
        self.start = time.time()
        self.name = name
        self.health = hp
        self.defense = defense
        self.damage = dmg
        self.weapon = weapon
    
    def print_info(self, text):
        print(f"{text}\n--> {self.name}")
        print(f"Уровень здоровья: {self.health}")
        print(f"Класс брони: {self.defense}")
        print(f"Сила удара: {self.damage}")
        print(f"Оружие: {self.weapon}")
        time.sleep(2)

    def strike(self, enemy):
        print(f"\n--> УДАР! {self.name} атакует! {enemy.name} с силой {self.damage}, используя {self.weapon}\n")
        time.sleep(2)
        enemy.defense -= self.damage
        if enemy.defense <= 0:
            enemy.health += enemy.defense
            enemy.defense = 0
    
        print(f"{enemy.name} покачнулся.\nКласс его брони упал до {enemy.defense}, а уровень здоровья до {enemy.health}\n")
        time.sleep(2)
    
    def death(self, enemy):
        end = time.time()
        print(f"\n--> Вы умерли от {enemy.name}"); time.sleep(1)
        self.print_info("")
        print(f"\nВремя: {round(end - self.start, 3)}")
        time.sleep(2)
    
    def fight(self, enemy):
        while self.health and enemy.health > 0:
            self.strike(enemy)
            if enemy.health <= 0:
                print(f"{enemy.name}, пал в нелегком бою!\n")
                break
            time.sleep(3)

            enemy.strike(self)
            if self.health <= 0:
                self.death(enemy)
                
