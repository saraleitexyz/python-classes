# Perfil básico (Básico). Crea un diccionario con los campos 'nombre', 'edad' y 'ciudad'.
# Muestra el valor de 'nombre', actualiza 'edad' sumando 1 y elimina la clave 'ciudad'.

my_dict = {"nombre": "Cristiano", "edad": 40, "ciudad": "Funchal"}

print(my_dict["nombre"])

my_dict["edad"] += 1
print(my_dict)

lost_value = my_dict.pop("ciudad")
print(my_dict)
print(lost_value)
