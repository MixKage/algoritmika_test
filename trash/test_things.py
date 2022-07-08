# ПОМОГИТЕ КТО НИБУДЬ ( В КОНЦЕ ДОЛЖНО БЫТЬ 16 А НЕ 1, 6) Я ТУПОЙ

def powers_of_two(n):
    total = ""
    for num in range(n+1):
        total += str(2**num)
    return [int(num) for num in total]

print(powers_of_two(0))