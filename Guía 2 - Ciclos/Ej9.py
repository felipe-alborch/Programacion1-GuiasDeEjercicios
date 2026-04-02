'''
9) Una empresa liquida sueldos según la categoría de cada empleado y paga por hora según la
siguiente tabla:

 - categoría 1: $150
 - categoría 2: $200
 - categoría 3: $250
 - categoría 4: $280

Diseñar un programa que permita ingresar la categoría de cada empleado y las horas que trabajo
en el mes y calcule:

a. Calcular el sueldo bruto y el sueldo neto (descontar 17% de aportes) de cada empleado
b. Calcular el total de sueldos que paga la empresa
c. Determinar cuántos empleados de cada categoría hay.

NOTA: como no aclara cuantos empleados son ni la condición de corte, interpreto que, si se ingresa la categoría '0', se corta el ingreso de datos.
'''

sueldoTotalPagado = 0
empleadosCategoriaUno = 0
empleadosCategoriaDos = 0
empleadosCategoriaTres = 0
empleadosCategoriaCuatro = 0

categoria = int(input("Ingresá la catgoría del empleado: "))

while categoria > 4 or categoria < 0:
    categoria = int(input("Categoría incorrecta. Ingresá nuevamente la catgoría del empleado: "))

while categoria != 0:
    horasTrabajadas = int(input("Ingresá las horas trabajadas en el mes por ese empleado: "))
    
    if categoria == 1:
        print(f"El sueldo bruto del empleado es: {horasTrabajadas * 150}.")
        print(f"El sueldo neto del empleado es: {(horasTrabajadas * 150) * 0.83}.")
        sueldoTotalPagado += horasTrabajadas * 150
        empleadosCategoriaUno += 1
    elif categoria == 2:
        print(f"El sueldo bruto del empleado es: {horasTrabajadas * 200}.")
        print(f"El sueldo neto del empleado es: {(horasTrabajadas * 200) * 0.83}.")
        sueldoTotalPagado += horasTrabajadas * 200
        empleadosCategoriaDos += 1
    elif categoria == 3:
        print(f"El sueldo bruto del empleado es: {horasTrabajadas * 250}.")
        print(f"El sueldo neto del empleado es: {(horasTrabajadas * 250) * 0.83}.")
        sueldoTotalPagado += horasTrabajadas * 250
        empleadosCategoriaTres += 1
    else:
        print(f"El sueldo bruto del empleado es: {horasTrabajadas * 280}.")
        print(f"El sueldo neto del empleado es: {(horasTrabajadas * 280) * 0.83}.")
        sueldoTotalPagado += horasTrabajadas * 280
        empleadosCategoriaCuatro += 1
        
    categoria = int(input("\n\nIngresá la catgoría del empleado: "))

    while categoria > 4 or categoria < 0:
        categoria = int(input("Categoría incorrecta. Ingresá nuevamente la catgoría del empleado: "))
        
print(f"El sueldo total pagado por la empresa es: {sueldoTotalPagado}")