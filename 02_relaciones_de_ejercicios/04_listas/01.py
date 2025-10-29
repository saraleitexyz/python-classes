
# 1. **Contar ocurrencias**: Dada una lista y un elemento, cuenta cuántas
# veces aparece ese elemento en la lista.

lista = [1,2,3,1,5,6,7,8,9,10,11,12,13,14,15]
elemento = int(input("Ingrese un número para comprobar: "))
print(f"El número {elemento} ha salido {lista.count(elemento)} {'veces' if lista.count(elemento) != 1 else 'vez'}.")