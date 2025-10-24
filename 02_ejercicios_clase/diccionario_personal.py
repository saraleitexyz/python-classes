from pprint import pprint

# Crear diccionario de información personal
def crear_perfil():
    perfil = {
        "nombre": input("Nombre: "),
        "edad": int(input("Edad: ")),
        "hobbies": input("Hobbies (separados por coma): ").split(","),
        "contacto": {
            "email": input("Email: "),
            "telefono": input("Teléfono: ")
        }
    }
    return perfil

def mostrar_perfil(perfil):
    print(f"\nPerfil de {perfil['nombre']}")
    print(f"Edad: {perfil['edad']} años")
    print(f"Hobbies: {', '.join(perfil['hobbies'])}")
    print(f"Email: {perfil['contacto']['email']}")
    print(f"Telefono: {perfil['contacto']['telefono']}")

mostrar_perfil(crear_perfil())
print(pprint(crear_perfil()))