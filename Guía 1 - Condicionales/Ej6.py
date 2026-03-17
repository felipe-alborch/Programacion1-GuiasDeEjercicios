'''
6) Ingresar un número. Si es positivo, calcular su raíz cuadrada, si es negativo mostrar su 
cuadrado y si es cero mostrar “Error. Ha ingresado un valor nulo”. 
'''

import math

numero = int(input("Ingresá un número: "))

if numero > 0:
    print(math.sqrt(numero))
elif numero < 0:
    print(numero**2)
else:
    print("Error. Ha ingresado un valor nulo")