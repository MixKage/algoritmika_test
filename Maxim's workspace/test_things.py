import queue


weapons = ["govno", "fignya", "andrey", "sraka", "huy", 'chlen']

question = input("какой аружие? ").lower()

if question in weapons[0:3]:
    print("sosi chlen")
elif question in weapons[3:6]:
    print("poshel nahuy")