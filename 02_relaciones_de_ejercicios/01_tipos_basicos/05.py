# 5. Pedir un número e indicar si es positivo o negativo.

print("COMPROBADOR DE NÚMEROS POSITIVOS Y NEGATIVOS:")
print("----------------------------------------------")

num = int(input("Introduzca un número: "))

if num < 0:
    print(f"El número {num} es negativo.")
elif num > 0:
    print(f"El número {num} es positivo.")
else:
    print("El número es 0.")
