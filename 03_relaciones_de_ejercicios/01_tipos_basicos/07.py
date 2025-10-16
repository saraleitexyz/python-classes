# 7. Pedir dos números y mostrarlos ordenados de mayor a menor.

print("ORDENADOR DE NÚMEROS:")
print("----------------------------------------------")

num1 = int(input("Introduzca el primer número: "))
num2 = int(input("Introduzca el segundo número: "))

if num1 > num2:
    mayor, menor = num1, num2
elif num2 > num1:
    mayor, menor = num2, num1
else:
    mayor = menor = num1

print(f"Los números ordenados de mayor a menor son: {mayor}, {menor}")

