# Coger un texto, pasar to do a minuscula y la funcion debe
# a : 5`72 , b: 8'9
# Quitar: ñ
# Convertir tilde en la letra base.

# Buscar como se suele poner el texto largo
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
print(poetry)

eliminar=

#Optmizar con una diccionario a: á; e:é???
clean_text = poetry.lower().replace('\n', ' ').replace(".", "").replace(",", "").replace(";","").replace("á","a").replace("é","e").replace("í", "i").replace("ó","o").replace("ú","u")
print(clean_text)

word_frequency = {}
for word in clean_text.split():
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1

for word, count in word_frequency.items():

print(word_frequency)
