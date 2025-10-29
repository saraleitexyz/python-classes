# Este programa lanza dos dados n veces y, de los resultados,
# calcula el procentaje de probabilidad de que salga esa tirada.

import random

def tirar():
    return random.randint(1,6)

tiradas=int(input("Dime cuántas veces vas a tirar los 2 dados: "))

veces=[0 for i in range(0, 13)]

for i in range(1, tiradas+1):
    veces[tirar()+tirar()]+=1
print(veces)

for i in range(2,13):
    print(f"Número: {i:5d}: Veces: {veces[i]:7d} % {(veces[i]/tiradas*100):8.2f}")



#def estadistica(veces):
#    for i in range(2, 13):
#        print(f"{i:2d} | ", end="")
#        print("*" * int((veces[i]/10)))

def imprimir_estadistica(lista):
    total = sum(lista)
    print("ESTADÍSTICAS DEL LANZAMIENTOS DE 2 DADOS")
    print("-" * 40)
    for i in range(2, 13):
        expr=int(round(lista[i]/total*100))
        cad='*' * expr
        print(f"{i:2d} | {cad}")

imprimir_estadistica(veces)

# Imprimir el gráfico de pie.