# Useless string.

from random import randint
from operator import contains
from time import sleep
from playsound import playsound

# en == enemy
# at == attack (damage)
# def == defense (defend)
# diff == difficulty

en_health = 100
health = 100
max_health = 100
en_at = 30
at = 30
healing = 10
en_healing = 10
en_is_def = 'false'
is_def = 'false'
do = 'basic'
diff = 'basic'
total_defences = 0
total_attacks = 0
total_heals = 0
total_dem_taken = 0
total_en_dem_taken = 0
total_dem = 0
battles_won = 0
sword1_taken = 'false'
armor1_taken = 'false'
boss1_won = 'false'

def attack(en_health):
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
    is_def = 'true'
    return is_def

def en_defence(en_is_def):
    en_is_def = 'true'
    return en_is_def

def heal(health):
    health += healing
    return health

def en_heal(en_health):
    en_health += en_healing
    return en_health

poss1 = 0
poss2 = 0
destination = 'basic'
wanting = 'basic'

level = 1
xp_ganing = 20
xp = 0

print('Welcome to my new (python) project! And now it is...')
sleep(2)
print('The fighting game!')
sleep(2)
diff = input('Choose difficulty level (baby, easy, normal, hard, insane, oh_god_please_no):')
#sleep(1)
#print('Enemy is approaching!')

if diff == 'baby':
    en_health = 1
    max_health = 10000
    en_at = 1
    at = 3000
    healing = 1000
    en_healing = 1
    xp_ganing = 0
elif diff == 'easy':
    en_health = 80
    max_health = 100
    en_at = 20
    at = 30
    healing = 10
    en_healing = 10
    xp_ganing = 10
elif diff == 'normal':
    en_health = 100
    max_health = 100
    en_at = 30
    at = 30
    healing = 10
    en_healing = 10
    xp_ganing = 20
elif diff == 'hard':
    en_health = 100
    max_health = 80
    en_at = 30
    at = 20
    healing = 10
    en_healing = 10
    xp_ganing = 30
elif diff == 'insane':
    en_health = 120
    max_health = 80
    en_at = 40
    at = 20
    healing = 10
    en_healing = 20
    xp_ganing = 40
elif diff == 'oh_god_please_no':
    en_health = 2000
    max_health = 1
    en_at = 500
    at = 1
    healing = 1
    en_healing = 100
    xp_ganing = 'you are hacking'

while True:
    if boss1_won == 'true':
        break
    if diff == 'baby':
        en_health = 1
        en_at = 1
        en_healing = 1
        xp_ganing = 0
    elif diff == 'easy':
        en_health = 80
        en_at = 20
        en_healing = 10
        xp_ganing = 10
    elif diff == 'normal':
        en_health = 100
        en_at = 30
        en_healing = 10
        xp_ganing = 20
    elif diff == 'hard':
        en_health = 100
        en_at = 30
        en_healing = 10
        xp_ganing = 30
    elif diff == 'insane':
        en_health = 120
        en_at = 40
        en_healing = 20
        xp_ganing = 40
    elif diff == 'oh_god_please_no':
        en_health = 2000
        en_at = 500
        en_healing = 100
        xp_ganing = 'you are hacking'
    health = max_health
    print(f'You are now at {poss1}, {poss2}')
    destination = input('Where to go? (right, left, front, back, other)')
    if destination == 'right':
        poss2 += 1
        print('--------------------------------')
    elif destination == 'left':
        poss2 -= 1
        print('--------------------------------')
    elif destination == 'front':
        poss1 += 1
        print('--------------------------------')
    elif destination == 'back':
        poss1 -= 1
        print('--------------------------------')
    if poss1 > 5:
        print('Theres no way through.')
        poss1 = 5
        print('--------------------------------')
    elif poss1 < -5:
        print('Theres no way through.')
        poss1 = -5
        print('--------------------------------')
    elif poss2 < -5:
        print('Theres no way through.')
        poss2 = -5
        print('--------------------------------')
    elif poss2 > 5:
        print('Theres no way through.')
        poss2 = 5
        print('--------------------------------')

    elif poss1 == -4 and poss2 == 2:
        if boss1_won == 'false':
            print('--------------------------------')
            print('Something powerful is coming...')
            sleep(6)
            print('Beter get ready...')
            sleep(10)
            print('Its the GraveKeeper! He is here to dig your grave!')
            en_health *= 1.5
            en_health = int(en_health)
            en_at *= 1.5
            en_at = int(en_at)
            en_healing *= 1.5
            en_healing = int(en_healing)
            while health != 0 and en_health != 0:
                if health < 0 or en_health < 0:
                    break
                print('--------------------------------')
                is_def = 'false'
                en_is_def = 'false'
                sleep(1)
                print('The round is starting...')
                sleep(1)
                print('-------------Stats--------------')
                sleep(1)
                print(f'Your stats: health = {health}, attack = {at}, you can heal {healing} hp.')
                sleep(0.5)
                print(f'Enemy stats: health = {en_health}, attack = {en_at}, can heal {en_healing} hp.')
                sleep(1)
                print('--------------------------------')
                sleep(1)
                # Enemy's round
                rand = randint(1,3)
                if rand == 2:
                    en_defence(en_is_def)
                    en_is_def = en_defence(en_is_def)
                # Player's round
                do = input('Do something! (at - attack, def - defend, heal - ...heal)').lower()
                if contains(do, 'at'):
                    print('You are attacking!')
                    attack(en_health)
                    en_health = attack(en_health)
                    total_attacks += 1
                elif contains(do, 'def'):
                    print('You are defending!')
                    defence(is_def)
                    is_def = defence(is_def)
                    total_defences += 1
                elif contains(do, 'heal'):
                    print('You decided to rest and heal up.')
                    heal(health)
                    health = heal(health)
                    total_heals += 1
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
                elif rand == 3:
                    print('Enemy is resting.')
                    en_heal(en_health)
                    en_health = en_heal(en_health)
                if health <= 0:
                    print('-----------You Lost!------------')
                    print('Ganed xp: 0')
                    print('---------Funny Stats:-----------')
                    print(f'Total defences (by you): {total_defences}')
                    print(f'Total attacks (by you): {total_attacks}')
                    print(f'Total heals (by you): {total_heals}')
            #        print(f'Damage taken (by you): {total_dem_taken}')
                    print('--------------------------------')
                elif en_health <= 0:
                    boss1_won = 'true'
                    print('-----------You Won!-------------')
                    print(f'Ganed xp: {xp_ganing}')
                    xp += xp_ganing
                    if xp >= 100:
                        xp = 0
                        level += 1
                    print('---------Funny Stats:-----------')
                    print(f'Total defences (by you): {total_defences}')
                    print(f'Total attacks (by you): {total_attacks}')
                    print(f'Total heals (by you): {total_heals}')
            #        print(f'Damage taken (by you): {total_dem_taken}')
                    print('--------------------------------')
        en_health //= 1.5
        en_at //= 1.5
        en_healing //= 1.5

    elif poss1 == 2 and poss2 == 3:
        if sword1_taken == 'false':
            print('You found a sword! + 10 at')
            at += 10
            sword1_taken = 'true'
            print('--------------------------------')

    elif poss1 == -2 and poss2 == -3:
        if armor1_taken == 'false':
            print('You found an armor! + 25 health')
            max_health += 25
            armor1_taken = 'true'
            print('--------------------------------')
    elif poss1 == randint(-5, 6) and poss2 == randint(-5, 6) or poss1 == randint(-5, 6) and poss2 == randint(-5, 6) or poss1 == randint(-5, 6) and poss2 == randint(-5, 6):
        while health != 0 and en_health != 0:
            if health < 0 or en_health < 0:
                break
            print('--------------------------------')
            is_def = 'false'
            en_is_def = 'false'
            sleep(1)
            print('The round is starting...')
            sleep(1)
            print('-------------Stats--------------')
            sleep(1)
            print(f'Your stats: health = {health}, attack = {at}, you can heal {healing} hp.')
            sleep(0.5)
            print(f'Enemy stats: health = {en_health}, attack = {en_at}, can heal {en_healing} hp.')
            sleep(1)
            print('--------------------------------')
            sleep(1)
            # Enemy's round
            rand = randint(1,3)
            if rand == 2:
                en_defence(en_is_def)
                en_is_def = en_defence(en_is_def)
            # Player's round
            do = input('Do something! (at - attack, def - defend, heal - ...heal)').lower()
            if contains(do, 'at'):
                print('You are attacking!')
                attack(en_health)
                en_health = attack(en_health)
                total_attacks += 1
            elif contains(do, 'def'):
                print('You are defending!')
                defence(is_def)
                is_def = defence(is_def)
                total_defences += 1
            elif contains(do, 'heal'):
                print('You decided to rest and heal up.')
                heal(health)
                health = heal(health)
                total_heals += 1
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
            elif rand == 3:
                print('Enemy is resting.')
                en_heal(en_health)
                en_health = en_heal(en_health)
            if health <= 0:
                print('-----------You Lost!------------')
                print('Ganed xp: 0')
                print('---------Funny Stats:-----------')
                print(f'Total defences (by you): {total_defences}')
                print(f'Total attacks (by you): {total_attacks}')
                print(f'Total heals (by you): {total_heals}')
        #        print(f'Damage taken (by you): {total_dem_taken}')
                print('--------------------------------')
            elif en_health <= 0:
                print('-----------You Won!-------------')
                print(f'Ganed xp: {xp_ganing}')
                xp += xp_ganing
                if xp >= 100:
                    xp = 0
                    level += 1
                print('---------Funny Stats:-----------')
                print(f'Total defences (by you): {total_defences}')
                print(f'Total attacks (by you): {total_attacks}')
                print(f'Total heals (by you): {total_heals}')
        #        print(f'Damage taken (by you): {total_dem_taken}')
                print('--------------------------------')
#            print('Thanks for playing! I dont think this game will be popular, but I still hope it will. This game was made in two days.')
#            print('                                                                             - Andrey, Lead Developer')

    elif destination == 'other':
        wanting = input('What do you want? (stats, move, difficulty)')
        if wanting == 'stats':
            print('--------------------------------')
            print(f'Your level: {level}')
            print(f'Battles won: {battles_won}')
            print('--------------------------------')
        elif wanting == 'move':
            print('--------------------------------')
        else:
            diff = input('Choose difficulty level (baby, easy, normal, hard, insane, oh_god_please_no):')
            print('--------------------------------')

print('Congrats! You beat the game!')
input('')
