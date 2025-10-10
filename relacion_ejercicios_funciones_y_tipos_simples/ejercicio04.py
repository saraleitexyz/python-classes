def rectangulo(base, altura, relleno):
    if relleno:
        while altura > 0:
            print("*" * base)
            altura-=1
    else:
        print("*" * base)

# TAREAS:
# Escribir un menu para elegir la figura y si tiene relleno o no.
# Hacer el resto de formas y hacer un arbol (solo relleno).
