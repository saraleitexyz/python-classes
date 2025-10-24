from pprint import pprint

def contador_palabras(texto):
    """Cuenta la frecuencia de cada palabra en un texto"""
    # Limpiar y dividir el texto
    palabras = texto.lower().replace(',', '').replace('.', '').split()

    frecuencias = {}
    for palabra in palabras:
        if palabra in frecuencias:
            frecuencias[palabra] += 1
    else:
        frecuencias[palabra] = 1

    # Alternativa más pythónica con get()
    #for palabra in palabras:
    #    frecuencias[palabra] = frecuencias.get(palabra, 0) + 1

    return frecuencias
# Prueba
texto = "El análisis de frecuencias está basado en el hecho de que, dado un texto, ciertas letras o combinaciones de letras aparecen más a menudo que otras, existiendo distintas frecuencias para ellas. Es más, existe una distribución característica de las letras que es prácticamente la misma para la mayoría de ejemplos de ese lenguaje. Por ejemplo, en inglés la letra E es muy común, mientras que la X es muy rara. Igualmente, las combinaciones ST, NG, TH y QU son pares de letras comunes, mientras que NZ y QJ son raros. La frase mnemotécnica ETAOIN SHRDLU agrupa las doce letras más frecuentes en los textos ingleses. En español, las vocales son muy frecuentes, ocupando alrededor del 45 % del texto, siendo la E y la A las que aparecen en más ocasiones, mientras que la frecuencia sumada de F, Z, J, X, K y W no alcanza el 2 %. La regla mnemotécnica para el español sería EAOSR NIDLC o bien EAOSN RILDUT"
frecuencias = contador_palabras(texto)
pprint(frecuencias) # {"el": 2, "gato": 1, ...}