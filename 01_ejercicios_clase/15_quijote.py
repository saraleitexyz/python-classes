# Genera un nuevo fichero llamado chiquito.txt a partir del quijote.txt que contendrá lo siguiente:
# Quijote por Chiquito
# Mancha por Málaga
# Al final, mostrar cuantos cambios ha habido.

from pathlib import Path

original_path = Path('quijote.txt')
modified_path = Path('chiquito.txt')
# Si estuviese arriba se usaria ../

replace_dictionary = {'Quijote': 'Chiquito', 'la Mancha': 'Málaga'}

def replace_words(input_path, dictionary, output_path):
    text = input_path.read_text(encoding='utf-8')
    replace_counter = 0

    for old, new in replace_dictionary.items():
        count = text.count(old)
        text = text.replace(old, new)
        replace_counter += count

    output_path.write_text(text, encoding='utf-8')
    print(f'Se han reemplazado {replace_counter} palabras.')

replace_words(original_path, replace_dictionary, modified_path)
# Hacer un contador aparte de cada uno.
# Añadir un try except (fichero no encontrado)