# 4. **Verificar si es palíndromo**: Verifica si una lista es palíndromo, es
# decir, si se lee igual de izquierda a derecha que de derecha a izquierda.

# Esta solución no valdria, ya que es con frases y no listas:
phrase = input("Ingresa una frase: ")
phrase = phrase.strip().lower().replace(" ", "")
reversed_phrase = phrase[::-1]
if phrase == reversed_phrase:
    print("La frase es un palíndromo.")
else:
    print("No es un palíndromo.")
print(phrase)
print(reversed_phrase)

# Version correcta:
def palindrome(lista):
    for x in range(0, len(lista)//2):
        if not(lista[x]==lista[len(lista[]):

lista1 = [1,2,3,4,5,6,7]
lista2 = [1,2,3,4,3,2,1]

print(f"{'Es palindromo' if palindromo(lista1) else 'No es palindromo'}")
print(f"{'Es palindromo' if palindromo(lista2) else 'No es palindromo'}")