# Diccionarios anidados (alumnado) (Avanzado). Crea un diccionario de alumnos donde cada
# valor sea otro diccionario con 'edad' y lista de 'notas'. Calcula el promedio por alumno, el
# mejor promedio del grupo y añade la clave 'aprobado' (True/False) según la media.

students = {
    "Cristiano": {
        "age": 40,
        "grades": [5, 8, 10]
    },
    "Ramona": {
        "age": 24,
        "grades": [7, 8, 9]
    },
    "Manuel": {
        "age": 33,
        "grades": [4, 2, 2, 1]
    }
}

for student, student_info in students.items():
    grades = student_info["grades"]
    avg_grade = sum(grades) / len(grades)
    #Evalua y pone automaticamente el true false
    student_info["aprobado"] = avg_grade >= 5

for student, student_info in students.items():
    print(f'{student}: {student_info["aprobado"]}')


