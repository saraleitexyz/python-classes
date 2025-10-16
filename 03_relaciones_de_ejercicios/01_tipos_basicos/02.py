# 2. Pedir el radio de un círculo y calcular su área. A=PI*r²

import math

print("CALCULADORA DEL ÁREA DE UN CÍRCULO:")
print("-----------------------------------")

radio = float(input("Introduzca el radio del circulo: "))

area = math.pi * (radio ** 2)

print(f"El área del círculo de radio {radio} es: {area:.2f}")


