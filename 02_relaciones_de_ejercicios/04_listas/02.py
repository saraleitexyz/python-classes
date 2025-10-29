# 2. **Eliminar duplicados**: Dada una lista, crea una nueva lista que
# contenga los mismos elementos pero sin duplicados.

lista = [1,1,5,4,5,1]

for x in lista:
    if lista.count(x) > 1:
        lista.remove(x)

print(lista)