# 9. Pedir tres números y mostrarlos ordenados de mayor a menor.

print("ORDENADOR DE NÚMEROS DE MAYOR A MENOR:")
print("----------------------------------------------")

num1 = int(input("Introduzca el primer número: "))
num2 = int(input("Introduzca el segundo número: "))
num3 = int(input("Introduzca el tercer número: "))

if num1 >= num2 and num1 >= num3:
    mayor = num1
    if num2 >= num3:
        medio, menor = num2, num3
    else:
        medio, menor = num3, num2
elif num2 >= num1 and num2 >= num3:
    mayor = num2
    if num1 >= num3:
        medio, menor = num1, num3
    else:
        medio, menor = num3, num1
else:
    mayor = num3
    if num1 >= num2:
        medio, menor = num1, num2
    else:
        medio, menor = num2, num1

print("Los números ordenados de mayor a menor son:", mayor, medio, menor)

