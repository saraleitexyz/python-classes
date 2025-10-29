# 5. **Intersección de dos listas**: Dadas dos listas, encuentra la intersección
# (los elementos comunes) entre ellas.

numbers1 = [1,2,3,5,5,6,7]
numbers2 = [1,2,3,4,5,6,7,8,9]
intersection = []

for i in range(0, len(numbers1)):
    for j in range(0, len(numbers2)):
        if numbers1[i] == numbers2[j]:
            intersection.append(numbers1[i])
            break

def elimina_duplicados(lista):
    for x in lista:
        if lista.count(x) > 1:
            lista.remove(x)


intersection = elimina_duplicados(intersection)

print(f"Las intersecciones son {intersection}")