num = 0

def menu():
    print("Conversor de temperatura:")
    print("1. Cº a K")
    print("2. Cº a F")
    print("3. K a Cº")
    print("4. K a F")
    print("5. F a K")
    print("6. F a Cº")
    print("7. Salir del programa.")

while num != 7:
    menu()
    num = int(input("Introduzca una opción: "))

    match num:
        case 1:
            c = float(input("Introduzca la temperatura en Celsius: "))
            k = c + 273.15
            print("La temperatura en Kelvin es: ", k)
        case 2:
            c = float(input("Introduzca la temperatura en Celsius: "))
            f = (c * 9 / 5) + 32
            print("La temperatura en Fahrenheit es: ", f)
        case 3:
            k = float(input("Introduzca la temperatura en Kelvin: "))
            c = k - 273.15
            print("La temperatura en Celsius es: ", c)
        case 4:
            k = float(input("Introduzca la temperatura en Kelvin: "))
            f = (k - 273.15) * 9 / 5 + 32
            print("La temperatura en Fahrenheit es: ", f)
        case 5:
            f = float(input("Introduzca la temperatura en Fahrenheit: "))
            k = (f - 32) * 5 / 9 + 273.15
            print("La temperatura en Kelvin es: ", k)
        case 6:
            f = float(input("Introduzca la temperatura en Fahrenheit: "))
            c = (f - 32) * 5 / 9
            print("La temperatura en Celsius es: ", c)
        case 7:
            break
        case _:
            print("Número incorrecto. Introduzca otro número.\n")

print("Saliendo. ¡Hasta luego!")





