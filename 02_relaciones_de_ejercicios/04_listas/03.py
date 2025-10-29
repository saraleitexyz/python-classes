# 3. **Invertir lista**: Dada una lista, inviértela sin usar la función `reverse()`.

list1 = [1,1,5,4,5,1]
lista_invertida = list1[::-1]

# Nunca iterar sobre una estructura que está cambiando.

# Alternative versions:
def inv_iter (user_list):
    i = 0
    j = len(user_list) - 1
    while i <= len(user_list)/2:
        user_list[i], lista_invertida[j] = lista_invertida[j], user_list[i]
        i+=1
        j-=1
    return lista_invertida

def inv_iter2(l):
    for i in range(0, len(l)//2):
        l[i], l[len(l)-i-1] = l[len(l)-i-1], l[i]
    return l

def inv_rec (l):
    if len(l) < 2:
        return l
    else:
        return [l[len(l)-1]] + inv_rec(l[1:-1] + [l[0]])

print(list)
print(lista_invertida)
print(inv_iter(list1))
print(inv_rec(list1))
