'''
17) Ingresar las medidas de dos ángulos expresados en grados minutos y segundos y hallar la 
suma. (recordar que los minutos y los segundos no deben excederse de 60)
'''

segundosTotales = 0
minutosTotales = 0
gradosTotales = 0

# Ingreso de datos del primer ángulo
grados1 = int(input("Ingresá la cantidad de grados del primer ángulo: "))
minutos1 = int(input("Ingresá la cantidad de minutos del primer ángulo: "))
segundos1 = int(input("Ingresá la cantidad de segundos del primer ángulo: "))

# Ingreso de datos del segundo ángulo
grados2 = int(input("\nIngresá la cantidad de grados del segundo ángulo: "))
minutos2 = int(input("Ingresá la cantidad de minutos del segundo ángulo: "))
segundos2 = int(input("Ingresá la cantidad de segundos del segundo ángulo: "))

# Operando los segundos
segundosTotales = segundos1 + segundos2

while segundosTotales > 60:
    segundosTotales -= 60
    minutosTotales += 1

minutosTotales = minutosTotales + minutos1 + minutos2

while minutosTotales > 60:
    minutosTotales -= 60
    gradosTotales += 1
    
gradosTotales = gradosTotales + grados1 + grados2

# Mostrando los valores finales
print(f"\nLos grados totales son: {gradosTotales}")
print(f"Los minutos totales son: {minutosTotales}")
print(f"Los segundos totales son: {segundosTotales}")