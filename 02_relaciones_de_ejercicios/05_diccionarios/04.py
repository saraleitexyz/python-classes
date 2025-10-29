# Invertir diccionario (Intermedio). Dado un diccionario con valores únicos, genera otro
# diccionario que invierta claves y valores. Después, repite el ejercicio cuando existen valores
# repetidos: en ese caso, el nuevo diccionario debe mapear cada valor a una lista de claves.

unique_dict = {"color": "azul", "fruta": "arandanos", "zumo": "naranja"}

reversed_dict = {v: k for k, v in unique_dict.items()}
print(reversed_dict)

repeated_unique_dict = {
    "color": "naranja",
    "fruta": "arandanos",
    "zumo": "naranja",
}

inverted_dict = {}
for k, v in repeated_unique_dict.items():
    if v not in inverted_dict:
        inverted_dict[v] = [k]
    else:
        inverted_dict[v].append(k)

print(inverted_dict)