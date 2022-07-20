class Hero():
    def __init__(self, name, health, armor, power, weapon):
        self.name = name
        self.health = health
        self.armor = armor
        self.power = power
        self.weapon = weapon

    def print_stats(self):
        print('Поприветствуйте', self.name)
        print('Уровень здоровья:', self.health)
        print('Броня:', self.armor)
        print('Сила:', self.power)
        print('Оружие:', self.weapon)

    def attack(self, Enemy):
        print('Атака!', self.name, 'атакует', Enemy.name, 'с силой', self.power, 'используя', self.weapon)
        Enemy.armor -= Me.power
        if Enemy.armor <= 0:
            Enemy.health += Enemy.armor
            Enemy.armor = 0
        print('Враг хп:', Enemy.health)
        print('Враг броня:', Enemy.armor)





Me = Hero('Арнольд', 50, 200, 20, 'Лапки')
Enemy = Hero('Бандит из-под Мышкина', 20, 100, 20, 'Всё ещё Лапки')
Me.print_stats()


while Enemy.health != 0:
    Me.attack(Enemy)