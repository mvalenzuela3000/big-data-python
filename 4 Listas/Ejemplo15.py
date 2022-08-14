materias = ["Seguridad informática", "Big Data", "Inteligencia Artificial", "Redes", "Machine Learning"]
aprobadas = []
for materia in materias:
    calificacion = float(input("¿Qué calificación ha obtenido en: " + materia + "? "))
    if calificacion >= 51:
        aprobadas.append(materia)
for materia in aprobadas:
    materias.remove(materia)
print("Usted debe repetir las materias: " + str(materias))