# 1. Pedir los coeficientes de una ecuación de segundo grado
# y muestre sus solucions reales. Si no existen, debe indicarlo.

import math

print("CALCULADORA DE ECUACIONES DE SEGUNDO GRADO:")
a = float(input("Introduce el valor de a: "))
b = float(input("Introduce el valor de b: "))
c = float(input("Introduce el valor de c: "))

discriminante = b ** 2 - 4 * a * c

if a == 0:
    print("No es una ecuación de segundo grado.")
elif discriminante < 0:
    print("No existen soluciones reales.")
elif discriminante == 0:
    x = -b / (2 * a)
    print("Existe una única solución real:", x)
else:
    x1 = (-b + math.sqrt(discriminante)) / (2 * a)
    x2 = (-b - math.sqrt(discriminante)) / (2 * a)
    print("Las soluciones reales son:")
    print("x1 =", x1)
    print("x2 =", x2)