# 11. Generar combinaciones al azar para la quiniela (14 valores dentro del conjunto 1, X o 2, por
# si hay alguien de otro planeta que no sepa cómo se rellena una quiniela). El resultado debe
# ser algo así, pero generado al azar:
# 1 - X - X - 2 - 1 - 1 - 1 - 2 - 2 - X - 1 - X - X – 2
# Modifica el ejercicio para que la probabilidad de que salga un 1 en dicha lista sea de
# 60%, la de que salga una X de un 30% y la de que salga un 2 de un 10%.

import random

print("QUINIELA MANUAL:")
print("Introduzca la probabilidad que quiere que tenga cada valor de la quiniela. Debe sumar 100.")

result_1 = int(input("Introduce una probabilidad para el 1: "))
result_X = int(input("Introduce una probabilidad para la X: "))
result_2 = int(input("Introduce una probabilidad para el 2: "))

if result_1 + result_2 + result_X != 100:
    raise "Las probabilidades son incorrectas. Estas deben sumar 100."

def quiniela_manual():
    resultados = []

    for i in range (14):
        numero = random.random()

        if numero < result_1/100:
            resultados.append('1')
        elif numero < (result_1 + result_X)/100:
            resultados.append('X')
        else:
            resultados.append('2')

    return " - ".join(resultados)

print("QUINIELA:")
print(quiniela_manual())