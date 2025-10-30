# 6. Filtrado y transformación (comprensión) (Intermedio). A partir de un diccionario
# alumno→nota, construye con comprensión de diccionarios uno nuevo que contenga solo
# alumnos con nota ≥ 5 y cuyas notas estén normalizadas a una escala 0–10 (por ejemplo,
# multiplicando por un factor).

student_grades = {"Manolo": 100, "Paco": 52, "Juan": 23, "Ramona": 72, "Mario": 10}

above_5_grades = {k: v * 0.1 for k, v in student_grades.items() if v >= 50}
print(above_5_grades)
