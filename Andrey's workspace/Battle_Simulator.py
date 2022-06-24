from random import randint
from operator import contains
from time import sleep

# en == enemy
# at == attack (damage)
# def == defense (defend)

en_health = 100
health = 100
en_at = 30
at = 20
healing = 10
en_is_def = 'false'
is_def = 'false'
do = 'basic'
total_defences = 0
total_attacks = 0
total_heals = 0
total_dem_taken = 0
total_en_dem_taken = 0
total_dem = 0

def attack(en_health):
#    total_attacks += 1
    if en_is_def == 'true':
        en_health -= at // 2
    else:
        en_health -= at
    return en_health

def en_attack(health):
    if is_def == 'true':
        health -= en_at // 2
    else:
        health -= en_at
    return health

def defence(is_def):
#    total_defences += 1
    is_def = 'true'
    return is_def

def en_defence(en_is_def):
    en_is_def = 'true'
    return en_is_def

def heal(health):
#    total_heals += 1
    health += healing
    return health

lang = input('Please choose language (Rus(WIP), Eng):').lower()
print('Welcome to my new (python) project! And now it is...')
sleep(2)
print('The fighting game!')
sleep(2)
input('Write something to start!')
sleep(1)
print('Enemy is approaching!')


while health != 0 and en_health != 0:
    if health < 0 and en_health < 0:
        break
    if contains(lang, 'eng'):
        print('--------------------------------')
        is_def = 'false'
        en_is_def = 'false'
        sleep(1)
        print('The round is starting...')
        sleep(1)
        print('-------------Stats--------------')
        sleep(1)
        print(f'Your stats: health = {health}, attack = {at}, only YOU can heal {healing} hp.')
        sleep(0.5)
        print(f'Enemy stats: health = {en_health}, attack = {en_at}')
        sleep(1)
        print('--------------------------------')
        sleep(1)
        # Enemy's round
        rand = randint(1,2)
        if rand == 2:
            en_defence(en_is_def)
            en_is_def = en_defence(en_is_def)
        # Player's round
        do = input('Do something! (at - attack, def - defend, heal - ...heal)').lower()
        if contains(do, 'at'):
            print('You are attacking!')
            attack(en_health)
            en_health = attack(en_health)
#            total_attacks = attack(total_attacks)
        elif contains(do, 'def'):
            print('You are defending!')
            defence(is_def)
            is_def = defence(is_def)
#            total_defences = defence(total_defences)
        elif contains(do, 'heal'):
            print('You decided to rest and heal up.')
            heal(health)
            health = heal(health)
#            total_heals = heal(total_heals)
        sleep(1)
        print('Enemy is...')
        sleep(2)
        # What enemy has done
        if rand == 1:
            print('Enemy is attacking!')
            en_attack(health)
            health = en_attack(health)
        elif rand == 2:
            print('Enemy is defending!')
if contains(lang, 'eng'):
    if en_health <= 0 and health <= 0:
        print('-------------Tie!-------------')
        print('---------Funny Stats:-----------')
        print('Coming soon!')
#        print(f'Total defences (by you): {total_defences}')
#        print(f'Total attacks (by you): {total_attacks}')
#        print(f'Total heals (by you): {total_heals}')
#        print(f'Damage taken (by you): {total_dem_taken}')
#        print(f'Damage taken (by enemy): {total_en_dem_taken}')
#        print(f'Damage taken (everybody): {total_dem}')
        print('--------------------------------')
    elif health <= 0:
        print('-----------You Lost!------------')
        print('---------Funny Stats:-----------')
        print('Coming soon!')
#        print(f'Total defences (by you): {total_defences}')
#        print(f'Total attacks (by you): {total_attacks}')
#        print(f'Total heals (by you): {total_heals}')
#        print(f'Damage taken (by you): {total_dem_taken}')
#        print(f'Damage taken (by enemy): {total_en_dem_taken}')
#        print(f'Damage taken (everybody): {total_dem}')
        print('--------------------------------')
    elif en_health <= 0:
        print('-----------You Won!-------------')
        print('---------Funny Stats:-----------')
        print('Coming soon!')
#        print(f'Total defences (by you): {total_defences}')
#        print(f'Total attacks (by you): {total_attacks}')
#        print(f'Total heals (by you): {total_heals}')
#        print(f'Damage taken (by you): {total_dem_taken}')
#        print(f'Damage taken (by enemy): {total_en_dem_taken}')
#        print(f'Damage taken (everybody): {total_dem}')
        print('--------------------------------')
    print('Thanks for playing! I dont think this game will be popular, but I still hope it will. This game was made in two days.')
    print('                                                                             - Andrey, Lead Developer')