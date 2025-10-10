import math

def second_grade(num_a, num_b, num_c):
    discriminant = b**2 - 4*a*c

    if num_a == 0:
        return "No se trata de una ecuación de segundo grado.";
    elif discriminant < 0:
        return "La ecuación no tiene soluciones reales."
    elif discriminant == 0:
        x = -b/(2*a)
        return f"La ecuación solo tiene una solución real: x = {x}"
    else:
        x1 = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
        x2 = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
        return f"La ecuación tiene dos soluciones reales es: {x1} y {x2}"

print("Introduce los valores de la ecuación de segundo grado:")
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

print(second_grade(a, b, c))