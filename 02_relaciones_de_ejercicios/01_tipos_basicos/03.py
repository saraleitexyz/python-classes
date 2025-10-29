# 3. Pedir el radio de una circunferencia y calcular su longitud.

import math

print("CALCULADORA DE LONGITUD DE UNA CIRCUNFERENCIA:")
print("----------------------------------------------")

radio = float(input("Introduzca el radio de la circunferencia: "))

longitud = 2 * math.pi * radio

print(f"La longitud de la circunferencia de radio {radio} es: {longitud:.2f}")

