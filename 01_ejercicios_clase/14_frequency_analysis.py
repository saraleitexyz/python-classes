poetry = """Ya de mi amor la confesión sincera
Oyeron tus calladas celosías,
Y fue testigo de las ansias mías
La luna, de los tristes compañera.
Tu nombre dice el ave placentera
A quien visito yo todos los días,
Y alegran mis soñadas alegrías
El valle, el monte, la comarca entera.
Solo tú mi secreto no conoces,
Por más que el alma con latido ardiente,
Sin yo quererlo, te lo diga a voces;
Y acaso has de ignorarlo eternamente,
Como las ondas de la mar veloces
La ofrenda ignoran que les da la fuente.
"""

replace_dictionary = {'a': 'á', 'e': 'é', 'i': 'í', 'o': 'ó', 'u': 'ú','n':'ñ', '': ' '}
#replace_dictionary = {'a': 'á', 'e': 'é', 'i': 'í', 'o': 'ó', 'u': 'ú','n':'ñ', '': (' ', '\n', ';', '.', ',')}

# TODO: Ver como poner lista dentro de replace_dictionary para cambiar varios símbolos value por la key ''
clean_text = poetry.lower().replace('\n', '').replace(';', '').replace(',','').replace('.','')

#print(clean_text)

for k,v in replace_dictionary.items():
    clean_text = clean_text.replace(v, k)

# print(clean_text)

letter_frequency = {}
total_letters = len(clean_text)

for letter in clean_text:
    letter_count = clean_text.count(letter)
    # Mas eficiente
    if letter not in letter_frequency.keys():
        letter_frequency[letter] = letter_count

for k,v in letter_frequency.items():
    letter_frequency[k] = round((v/total_letters) * 100, 3)

print(letter_frequency)