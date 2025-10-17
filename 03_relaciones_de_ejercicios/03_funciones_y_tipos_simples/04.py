def rectangulo(base, altura, relleno):
    if relleno:
        for i in range(altura):
            print("* " * base)
    else:
        print("* " * base)
        for i in range(altura-2):
            print("* " + "  " * (base-2) + "* ")
        print("* " * base)

def triangulo(altura, relleno):


# TAREAS:
# Escribir un menu para elegir la figura y si tiene relleno o no.
# Hacer el resto de formas y hacer un arbol (solo relleno).
