# 8. Pedir dos números y decir cuál es el mayor o si son iguales.

print("¿QUÉ NÚMERO ES MAYOR?")
print("----------------------------------------------")

num1 = int(input("Introduzca el primer número: "))
num2 = int(input("Introduzca el segundo número: "))

if num1 > num2:
    print(f"El primer número ({num1}) es mayor que el segundo ({num2}).")
elif num2 > num1:
    print(f"El segundo número ({num2}) es mayor que el primero ({num1}).")
else:
    print(f"Los números son iguales: {num1} = {num2}.")

