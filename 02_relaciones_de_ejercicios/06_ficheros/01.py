# 1. Escribe un programa que escriba los 100 primeros números primos en un
# archivo llamado "primos.txt". Posteriormente el programa deberá leer dichos
# números desde primos.txt y calcular su suma total mostrándola en pantalla.

from pathlib import Path

file = Path("primos.txt").read_text(encoding="utf-8")

total_prime_numbers = 0
checking_num = 2

def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

with open("primos.txt", 'w', encoding='utf-8') as f:
    while total_prime_numbers < 100:
        if is_prime(checking_num):
            f.write(f"{checking_num}\n")
            total_prime_numbers += 1
        checking_num += 1

with open('primos.txt','r', encoding='utf-8') as f:
    total_sum = 0
    for line in f:
        total_sum += int(line)

print(f'La suma total de la primos es: {total_sum}')