class enemy:
    name = ""
    hp = 0
    lvl = 0
    dmg = 0
    loot = ""

    def __init__(self, name, hp, lvl, dmg, loot):
        self.name = name
        self.hp = hp
        self.lvl = lvl
        self.dmg = dmg
        self.loot = loot

monsters = {
     "Волк": {
    #     "Лут": ["Зуб Волка", 80],
    #     "Характеристики": {
    #         "hp": "500",
    #         "lvl": "2",
    #         "damage": "100",
    #         "defence%": 20
          enemy("Волк", 500, 2, 100, "Зуб Волка")
    #     }  
      },
    # "Заяц": {
    #     "Лут": ["Шубка Зайца", 10],
    #     "Характеристики": {
    #         "hp": "100",
    #         "lvl": "0",
    #         "damage": "25",
    #         "defence%": 50
    #     }
    # },
    # "Медведь": {
    #     "Лут": ["Когти Медведя", 200 ],
    #     "Характеристики": {
    #         "hp": "850",
    #         "lvl": "4",
    #         "damage": "200",
    #         "defence%": 5
    #     }
    # },
    # "Белка": {
    #     "Лут": ["Орех", 25],
    #     "Характеристики": {
    #         "hp": "150",
    #         "lvl": "1",
    #         "damage": "25",
    #         "defence%": 60
    #     }
    # },
    # "Сильван": {
    #     "Лут": [],
    #     "Характеристики": {
    #         "hp": "1200",
    #         "lvl": "8",
    #         "damage": "500",
    #         "defence%": 0
    #     }
    # },
}
