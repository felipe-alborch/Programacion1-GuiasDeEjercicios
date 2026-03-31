'''
4) Al terminar un día en un colegio secundario se hace una estadística de faltas sabiendo de cada curso:
 - Curso (1-5)
 - Presentes
 - Ausentes

Se pide calcular:
 - Por cada curso el porcentaje de presentes sobre el total
 - Cantidad de ausentes en el colegio
 - Curso con mayor cantidad de ausente
'''

totalusentes = 0
cantidadMaximaDeAusentes = 0
cursoConCantidadMaximaDeAusentes = 0

for i in range(1,6):
    print(f"Curso {i}")
    presentes = int(input("Ingresá la cantidad de alumnos presentes: "))
    ausentes = int(input("Ingresá la cantidad de alumnos ausentes: "))
    
    totalusentes += ausentes
    total = presentes + ausentes
    
    if ausentes > cantidadMaximaDeAusentes:
        cursoConCantidadMaximaDeAusentes = i
        cantidadMaximaDeAusentes = ausentes
    
    print(f"\nEl porcentaje de presentismo del curso {i} es: {(presentes * 100) / total}\n\n")

print(f"La cantidad total de ausentes en el colegio es: {totalusentes}")
print(f"El curso con mayor cantidad de ausentes es el {cursoConCantidadMaximaDeAusentes}, con {cantidadMaximaDeAusentes} alumnos ausentes.")