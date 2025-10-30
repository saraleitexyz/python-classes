# Agrupar con setdefault() (Intermedio). Dada una lista de palabras, crea un diccionario que
# agrupe por inicial (clave: letra inicial; valor: lista de palabras que empiezan por esa letra).
# Emplea setdefault() para simplificar el código.

words = ["gato", "amarillo", "sopa", "estuche"]

word_dictionary = {}
for word in words:
    first_letter = word[0]
    word_dictionary.setdefault(first_letter, word)
    # Si hubiese mas de 1 palabra con la misma letra: []).append(word)

print(word_dictionary)