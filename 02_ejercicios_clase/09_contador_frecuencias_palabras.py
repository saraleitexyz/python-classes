from pprint import pprint

def contador_palabras(texto):
    palabras = texto.lower().replace(',', '').replace('.', '').split()

    frecuencias = {}

    for palabra in palabras:
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
    return frecuencias
# Prueba
t = "El análisis de frecuencias está basado en el hecho de que"
frecuencia2 = contador_palabras(t)
pprint(frecuencia2)