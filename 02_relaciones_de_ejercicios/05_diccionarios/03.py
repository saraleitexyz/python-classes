# Frecuencia de palabras (Intermedio). Dado un texto en una sola cadena, construye un
# diccionario con la frecuencia de cada palabra. Ignora mayúsculas y signos de puntuación
# básicos (comas y puntos). Devuelve el diccionario ordenado por frecuencia descendente
# (como lista de tuplas)

text = ("""
Cuando cuentes cuentos cuenta cuantos cuentos cuentas, porque si no cuentas cuantos cuentos cuentas nunca sabrás 
cuantos cuentos sabes contar.
""")

clean_text = text.lower().replace(",","").replace(".", "")

word_frequency = {}
for word in clean_text.split():
    #Split devuelve en forma de lista
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1

print(word_frequency)

# Most popular solution:
sorted_frequency = dict(sorted(word_frequency.items(), key=lambda x: x[1], reverse=True))

# Teacher option:
def frec_palabra(texto):
    pares = list(word_frequency.items())
    pares.sort()
    print(pares)

    pares_reves = [(v,k) for k,v in pares]
    print(pares_reves)
    pares_reves.sort(reverse=True)

    print(pares_reves)

print(frec_palabra(text))
print(sorted_frequency)