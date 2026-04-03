'''
10) Se realiza un censo en la provincia de Buenos Aires. Por cada persona censada se ingresa sexo
(1.F, 2.M), edad y estudios cursados (1 para estudios primarios, 2 para estudios secundarios ó
3 para estudios terciarios).
Diseñar un programa que permita ingresar los datos y calcular:

a. Cantidad de hombres mayores a 45 años.
b. Cantidad de mujeres encuestadas.
c. Promedio de edad de las personas para cada tipo de estudio.
d. Porcentaje de mujeres con estudios terciarios.
e. Porcentaje de hombres mayores a 30 años con estudios terciarios.
f. Promedio de edad de las mujeres mayores a 40 años con estudios secundarios.

La carga de datos finaliza cuando ingresa 0 en edad y en estudios cursados.
'''
cantidadMujeresMayores40ConEstudiosSecundarios = 0
hombresMayores45 = 0
mujeresEncuestadas = 0
hombresEncuestados = 0
cantidadMujeresConEstudiosTerciarios = 0
puntoE = 0 #Puse este nombre para simplificar, ya que sino me iba a quedar un choclo, pero serían el porcentaje de hombres mayores a 30 años con estudios terciarios.
puntoF = 0 #Lo mismo que 'puntoE', pero esta vez con el promedio de edad de las mujeres mayores a 40 años con estudios secundarios
cantidadPersonasConEstudiosPrimarios = 0
acumuladorEdadPersonasConEstudiosPrimarios = 0
cantidadPersonasConEstudiosSecundarios = 0
acumuladorEdadPersonasConEstudiosSecundarios = 0
cantidadPersonasConEstudiosTerciarios = 0
acumuladorEdadPersonasConEstudiosTerciarios = 0

edad = int(input("Ingresá la edad de la persona: "))
while edad < 0:
    edad = int(input("Edad inválida. Ingresá nuevamente la edad de la persona: "))

estudiosCursados = int(input("Ingresá los estudios cursados por la persona: "))
while estudiosCursados < 0 or estudiosCursados > 3:
    estudiosCursados = int(input("Nivel de estudios inválidos. Ingresá nuevamente los estudios cursados por la persona: "))
    
while edad != 0 or estudiosCursados != 0:
    #Agrego estos dos while para evitar proceesamientos incorrectos al ingresar o la edad o los estudios cursados con '0' junto a su otro valor distinto a '0'
    while edad == 0:
        edad = int(input("Para finalizar la carga, debe modificar la edad de la persona. Ingrese nuevamente la edad: "))
    
    while estudiosCursados == 0:
        estudiosCursados = int(input("Para finalizar la carga, debe modificar los estudios cursados de la persona. Ingréselo nuevamente: "))
    
    sexo = int(input("Ingresá el sexo de la persona: "))
    
    while sexo != 1 and sexo != 2:
        sexo = int(input("Sexo inválido. Ingresá nuevamente el sexo de la persona: "))
    
    if edad > 45 and sexo == 2:
        hombresMayores45 += 1
    
    if sexo == 1:
        mujeresEncuestadas += 1
    else:
        hombresEncuestados += 1
        
        
    if estudiosCursados == 1:
        cantidadPersonasConEstudiosPrimarios += 1
        acumuladorEdadPersonasConEstudiosPrimarios += edad
    elif estudiosCursados == 2:
        cantidadPersonasConEstudiosSecundarios += 1
        acumuladorEdadPersonasConEstudiosSecundarios += edad
        
        if sexo == 1 and edad > 40:
            puntoF += edad
            cantidadMujeresMayores40ConEstudiosSecundarios += 1
    else:
        cantidadPersonasConEstudiosTerciarios += 1
        acumuladorEdadPersonasConEstudiosTerciarios += edad

        if sexo == 1:
            cantidadMujeresConEstudiosTerciarios += 1
        elif sexo == 2 and edad > 30:
            puntoE += 1
            
    #Volviendo al ingreso de los datos para validar si seguir o no en el while
    edad = int(input("Ingresá la edad de la persona: "))
    while edad < 0:
        edad = int(input("Edad inválida. Ingresá nuevamente la edad de la persona: "))

    estudiosCursados = int(input("Ingresá los estudios cursados por la persona: "))
    while estudiosCursados < 0 or estudiosCursados > 3:
        estudiosCursados = int(input("Nivel de estudios inválidos. Ingresá nuevamente los estudios cursados por la persona: "))
    
            
# Printeando los resultados

#Punto A
print(f"\n\nLa cantidad de hombre mayores a 45 años es: {hombresMayores45}.")

#Punto B
print(f"La cantidad de mujeres encuestadas es: {mujeresEncuestadas}.")

#Punto C
if cantidadPersonasConEstudiosPrimarios > 0:
    print(f"El promedio de edad de las personas con estudios primarios es: {acumuladorEdadPersonasConEstudiosPrimarios / cantidadPersonasConEstudiosPrimarios}.")
else:
    print("No se registraron personas con estudios primarios.")

if cantidadPersonasConEstudiosSecundarios > 0:
    print(f"El promedio de edad de las personas con estudios secundarios es: {acumuladorEdadPersonasConEstudiosSecundarios / cantidadPersonasConEstudiosSecundarios}.")
else:
    print("No se registraron personas con estudios secundarios.")

if cantidadPersonasConEstudiosTerciarios > 0:
    print(f"El promedio de edad de las personas con estudios terciarios es: {acumuladorEdadPersonasConEstudiosTerciarios / cantidadPersonasConEstudiosTerciarios}.")
else:
    print("No se registraron personas con estudios terciarios.")

#Punto D
if mujeresEncuestadas > 0:
    print(f"El porcentaje de mujeres con estudios terciarios es: {(cantidadMujeresConEstudiosTerciarios * 100) / mujeresEncuestadas}%.")
else:
    print("No hubo mujeres encuestadas.")    

#Punto E
if hombresEncuestados > 0:
    print(f"El porcentaje de hombres mayores a 30 años con estudios terciarios es: {(puntoE * 100) / hombresEncuestados}%.")
else:
    print("No hubo hombres encuestados.")

#Punto F
if cantidadMujeresMayores40ConEstudiosSecundarios > 0:
    print(f"El promedio de mujeres mayores a 40 años con estudios secundarios es: {puntoF / cantidadMujeresMayores40ConEstudiosSecundarios}.")
else:
    print("No hubo mujeres mayores a 40 años con estudios secundarios.")