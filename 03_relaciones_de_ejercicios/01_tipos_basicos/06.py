# 6. Pedir dos números y decir si uno es múltiplo del otro.

print("COMPROBADOR DE MÚLTIPLOS:")
print("----------------------------------------------")

num1 = int(input("Introduzca el primer número: "))
num2 = int(input("Introduzca el segundo número: "))

if num1 == 0 or num2 == 0:
    print("No se pueden comprobar múltiplos con 0.")
elif num1 % num2 == 0:
    print(f"El número {num1} es múltiplo de {num2}.")
elif num2 % num1 == 0:
    print(f"El número {num2} es múltiplo de {num1}.")
else:
    print("No hay múltiplos.")
