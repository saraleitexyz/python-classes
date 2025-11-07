# Leer ese fichero linea a linea donde la clave es el pais y la clave el nombre del pais
# Juego donde te pidan la capital del pais, si acierta 1 punto y falla nada.
# Cuando el ponga fin: se han hecho x aciertos y x fallos en x intentos.

# Leer el fichero linea a linea y guardarlo en un dictionario.

from pathlib import Path

path = Path('../03_text_files/capitalPaises.txt')
# Investigar uso del path y luego open

capitals = {}

with open('../03_text_files/capitalPaises.txt', encoding='utf-8') as f:
    for line in f:
        value_pairs = line.rstrip().split(', ')
        for k,v in capitals.items():
            capitals[k] = line.get(value_pairs[0])
            capitals[v] = line.get(value_pairs[1])

print(capitals)



