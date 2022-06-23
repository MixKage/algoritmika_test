from operator import contains
import time # библеотека задержки кода
from random import random, randrange, randint # библеотека рандома

def sleep(second): #функция с заморозкой кода, в скобках время в секундах
    time.sleep(second)
# randint(от, до) - случайное число можно присвоить переменной

def hello_def(): #пользователь написал "привет":
    name_not_exist = "Хммм, я думаю вы обманываете меня! Такого имени не существует!"
    sleep(1)
    if rand == 0:
        print("Приветствую. Как ваше имя?")
        name = input()
        if len(name) < 4:
            sleep(1)
            print(name_not_exist)
        else:
            print(f"Отличное имя! {name}")
    elif rand == 1:
        print("Здарова! Как тебя зовут?")
        name = input()
        if len(name) < 4:
            sleep(1)
            print(name_not_exist)
        else:
            print(f"Прекрасное имя! {name}, А как настроение?")
            mood = input().lower()       
            sleep(1)
        if mood in bad_mood_types: # настроение плохое:
            print(f"Не расстраивайся {name}!")
            sleep(0.35)
            print("")
        elif mood in good_mood_types:
            print(f"Надеюсь всё будет ещё лучше, {name}!")
    elif rand == 2:
        print("Привет!")
        sleep(0.3)
        name = input("Как тебя зовут?")
        if len(name) < 4:
            sleep(1)
            print(name_not_exist)
        else:
            print(f"Шикарное имя, {name}!")

# ----ИГРЫ---- 
def guess_number():
    index = 3
    var1 = ["1. От 0 до 10", "2. от 0 до 50", "3. От 0 до 100"]
    print("Так, тогда начинаем!")
    sleep(0.5)
    print("Вот варианты игры:")
    sleep(0.5)
    print('\n'.join(map(str, var1)))
    choose = input("Выбирай:").lower()
    sleep(1)
    if choose == "1":
        print("Отлично кто будет загадывать?")
        choose = input("Я или Ты?").lower()
        sleep(1)
        if contains(choose, "ты"):
            num = randint(0, 10)
            print("Хорошо! Я загадал!")
            sleep(0.5)
            for i in range(3):
                index -= 1
                choose = int(input("У тебя 3 попытки (число от 0 до 10)"))
                sleep(0.5)
                if choose == num:
                    if index == 2:
                        print("Поздравляю! Вы угадали с первого раза!")
                    else:
                        print("Повезло вам! Поздравляю!")
                    break
                else:
                    num2 = randint(0,2)
                    if num2 == 0 and i != 2:
                        print(f"Эх, неудача... у вас осталось - {index} попытки.")
                    elif num2 == 1 and i != 2:
                        print(f"Какая жалость... у вас осталось - {index} попытки.")
                    elif num2 == 2 and i != 2:
                        print(f"Невезуха, В любом случае у вас осталось - {index} попытки!")
                    else:
                        print("Не повезло вам в этот раз.")
        elif contains(choose, "я"):
            choose = int(input("Твой выбор (от 0 до 10):"))
            sleep(0.5)
            print("Загадали? Отлично! У меня есть 3 попытки.")
            sleep(1)
            print("Так... Я готов!")
            for i in range(3):
                index -=1
                num = randint(0, 10)
                for i2 in range(3):
                    print(f"{i2+1}...")
                    sleep(1)
                print(f"{num}!")
                sleep(0.5)
                answer = input("Я угадал?").lower()
                sleep(0.5)
                if contains(answer, "да") and choose == num:
                    print("Ура!!! Я выйграл!")
                    break
                elif contains(answer, "да") and choose != num:
                    print("Ты меня обманываешь! Зануда.")
                    break
                elif contains(answer, "нет") and choose == num:
                    print("Ты такой обманщик, я всё вижу! Жулик!")
                    break
                elif contains(answer, "нет") and choose != num:
                    if i == 2:
                        print("Я проиграл...")
                    else:
                        print(f"Эх.. попробую еще раз. У меня осталось {index} попытки.")
    elif choose == "2":
        print("Отлично кто будет загадывать?")
        choose = input("Я или Ты?").lower()
        sleep(1)
        if contains(choose, "ты"):
            num = randint(0, 50)
            print("Хорошо! Я загадал!")
            sleep(0.5)
            for i in range(3):
                index -= 1
                choose = int(input("У тебя 3 попытки (число от 0 до 50)"))
                sleep(0.5)
                if choose == num:
                    if index == 2:
                        print("Какая удача! Вы угадали с первого раза!")
                    else:
                        print("Повезло вам! Поздравляю!")
                    break
                else:
                    num2 = randint(0,2)
                    if num2 == 0 and i != 2:
                        print(f"Эх, неудача... у вас осталось - {index} попытки.")
                    elif num2 == 1 and i != 2:
                        print(f"Какая жалость... у вас осталось - {index} попытки.")
                    elif num2 == 2 and i != 2:
                        print(f"Невезуха, В любом случае у вас осталось - {index} попытки!")
                    else:
                        print("Не повезло вам в этот раз.")
        elif contains(choose, "я"):
            choose = int(input("Твой выбор (от 0 до 50):"))
            sleep(0.5)
            print("Загадали? Отлично! У меня есть 3 попытки.")
            sleep(1)
            print("Так... Я готов!")
            for i in range(3):
                index -=1
                num = randint(0, 50)
                for i2 in range(3):
                    print(f"{i2+1}...")
                    sleep(1)
                print(f"{num}!")
                sleep(0.5)
                answer = input("Я угадал?").lower()
                sleep(0.5)
                if contains(answer, "да") and choose == num:
                    print("Ура!!! Я выйграл!")
                    break
                elif contains(answer, "да") and choose != num:
                    print("Ты меня обманываешь! Зануда.")
                    break
                elif contains(answer, "нет") and choose == num:
                    print("Ты такой обманщик, я всё вижу! Жулик!")
                    break
                elif contains(answer, "нет") and choose != num:
                    if i == 2:
                        print("Я проиграл...")
                    else:
                        print(f"Эх.. попробую еще раз. У меня осталось {index} попытки.") 
    elif choose == "3":
        print("Отлично кто будет загадывать?")
        choose = input("Я или Ты?").lower()
        sleep(1)
        if contains(choose, "ты"):
            num = randint(0, 100)
            print("Хорошо! Я загадал!")
            sleep(0.5)
            for i in range(3):
                index -= 1
                choose = int(input("У тебя 3 попытки (число от 0 до 100)"))
                sleep(0.5)
                if choose == num:
                    if index == 2:
                        print("Вы очень везучий! Вы угадали с первого раза!")
                    else:
                        print("Повезло вам! Поздравляю!")
                    break
                else:
                    num2 = randint(0,2)
                    if num2 == 0 and i != 2:
                        print(f"Эх, неудача... у вас осталось - {index} попытки.")
                    elif num2 == 1 and i != 2:
                        print(f"Какая жалость... у вас осталось - {index} попытки.")
                    elif num2 == 2 and i != 2:
                        print(f"Невезуха, В любом случае у вас осталось - {index} попытки!")
                    else:
                        print("Не повезло вам в этот раз.")
        elif contains(choose, "я"):
            choose = int(input("Твой выбор (от 0 до 100):"))
            sleep(0.5)
            print("Загадали? Отлично! У меня есть 3 попытки.")
            sleep(1)
            print("Так... Я готов!")
            for i in range(3):
                index -=1
                num = randint(0, 10)
                for i2 in range(3):
                    print(f"{i2+1}...")
                    sleep(1)
                print(f"{num}!")
                sleep(0.5)
                answer = input("Я угадал?").lower()
                sleep(0.5)
                if contains(answer, "да") and choose == num:
                    print("Ура!!! Я выйграл!")
                    break
                elif contains(answer, "да") and choose != num:
                    print("Ты меня обманываешь! Зануда.")
                    break
                elif contains(answer, "нет") and choose == num:
                    print("Ты такой обманщик, я всё вижу! Жулик!")
                    break
                elif contains(answer, "нет") and choose != num:
                    if i == 2:
                        print("Я проиграл...")
                    else:
                        print(f"Эх.. попробую еще раз. У меня осталось {index} попытки.")
# ------------         

#     ВСЕ ПЕРЕМЕННЫЕ НИЖЕ:            
bad_mood_types = ["грустно", "одиноко", "плохо", "ужасно", "я в не настроении", "фигово", "хреново", "хочеться плакать"] # плохие типы настроения
good_mood_types = ["все хорошо", "круто", "нормально", "хорошо", "прекрасно", "отлично"] # хорошие типы настроения
hello_types = ["приветствую", "здравствуй", "привет", "здарова", "приветик", "даров", "дарова"]
commands = ["1. Команды", "2. Привет"]
games = ["1. Угадай число", "2. Камень ножницы бумага"]

print("Я ChatBot! Напишите (команды) для подробностей.")
question = input("Спросите что угодно (выкл - выключить)").lower()  # основной вопрос

while question != "офф" and question != "выкл":  # основной цикл с использованием вопроса
    if question in hello_types:
        rand = randint(0,2) # варианты ответа бота 3 штук
        hello_def()
    elif contains(question, "команды"):
        print('\n'.join(map(str, commands)))
    elif contains(question, "игры"):
        print("Отлично! Во что играть будем?")
        print('\n'.join(map(str, games)))
        choose = int(input())
        if choose == 1:
            while question != "выкл" and question != "нет":
                question = 0
                guess_number()
                question = input("Желаете продолжить? (да/нет)")
                print("--------------------------------------")
    else:
        print("Я вас не совсем понимаю.")

    sleep(1)
    print("--------------------------------------")
    question = input("Спросите что угодно (выкл - выключить)").lower()  