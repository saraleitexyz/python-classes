# 11. Generar combinaciones al azar para la quiniela (14 valores dentro del conjunto 1, X o 2, por
# si hay alguien de otro planeta que no sepa cómo se rellena una quiniela). El resultado debe
# ser algo así, pero generado al azar:
# 1 - X - X - 2 - 1 - 1 - 1 - 2 - 2 - X - 1 - X - X – 2
# Modifica el ejercicio para que la probabilidad de que salga un 1 en dicha lista sea de
# 60%, la de que salga una X de un 30% y la de que salga un 2 de un 10%.

import random

print("QUINIELA MANUAL:")
print("Introduzca la probabilidad que quiere que tenga cada valor de la quiniela. Debe sumar 100.")

def quiniela_manual(a, b, c):
    resultados = []

    for i in range (14):
        numero = random.random()

        if numero < a/100:
            resultados.append('1')
        elif numero < (a + b)/100:
            resultados.append('X')
        else:
            resultados.append('2')
    return " - ".join(resultados)

for i in range (100):
    a = random.randint(1,100)
    b = random.randint(a,100)
    c = random.randint(b,100)
    b -= a
    c = 100 - a - b
    resultado = quiniela_manual(a, b, c)
    total_1 = resultado.count("1")
    total_X = resultado.count("X")
    total_2 = resultado.count("2")
    print(f"QUINIELA ({a:2d}, {b:2d}, {c:2d}) : {quiniela_manual(a, b, c)} | 1s: {total_1}  | Xs: {total_X} "
          f"| 2s: {total_2}")






