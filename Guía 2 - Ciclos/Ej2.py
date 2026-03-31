'''
2) Calcular el promedio semanal de gastos en un mes, ingresando como datos:
 - Semana número
 - Gasto semanal
El proceso termina cuando “semana número” es igual a 5.
'''

semana = int(input("Ingresá el número de semana: "))
promedioSemanal = 0
acumulador = 0

while semana <= 0:
    semana = int(input("Número invalido. Volvé a ingresar un número de semana: "))

while semana < 5:
    gasto = int(input("Ingresá el gasto de esa semana: "))
    acumulador += gasto

    semana = int(input("Ingresá el número de semana: "))
    while semana <= 0:
        semana = int(input("Número invalido. Volvé a ingresar un número de semana: "))

print(f"El promedio de lo gastado en el mes es: {acumulador / 4}")