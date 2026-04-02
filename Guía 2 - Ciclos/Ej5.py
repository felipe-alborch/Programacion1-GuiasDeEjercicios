'''
5) Leer el número de mes y mostrar cuantos días tiene ese mes (año actual).

NOTA: Para agregar algo de ciclos, tomo que se ingresan datos hasta ingresar el mes '0'
'''

mes = int(input("Ingresá el número de mes (1-12): "))

while mes > 12 or mes < 0:
    mes = int(input("Mes inválido. Ingresá nuevamente el número de mes (1-12): "))

while mes != 0:
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        print("El mes tiene 31 días.")
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        print("El mes tiene 30 días.")
    elif mes == 2:
        print("El mes tiene 28 días.")
    else:
        print("Mes inválido.")
        
    mes = int(input("\n\nIngresá el número de mes (1-12): "))

    while mes > 12 or mes < 0:
        mes = int(input("Mes inválido. Ingresá nuevamente el número de mes (1-12): "))