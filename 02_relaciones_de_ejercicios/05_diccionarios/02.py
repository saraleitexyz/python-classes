# 2. get() y setdefault() (Básico). Escribe una función que reciba un diccionario de conteo y una
# clave. Debe incrementar el conteo usando get() y, si la clave no existe, inicializarla con
# setdefault() a 0 antes de incrementar.

def increase_value(dict, key):
    # setdefault no hace nada con aquellas claves que ya existen
    dict.setdefault(key, 0)
    dict[key] = dict.get(key) + 1
    return dict

fruit_count = {"peaches": 3, "apples": 2}

increase_value(fruit_count, "peaches")
print(fruit_count)

increase_value(fruit_count, "bananas")
print(fruit_count)