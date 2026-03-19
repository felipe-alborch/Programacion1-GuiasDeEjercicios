'''
16) Ingresar dos números y sin resolver la multiplicación mostrar una leyenda según el 
producto sea negativo, positivo o cero.
'''

numero1 = int (input("Ingresá un número: "))
numero2 = int (input("Ingresá otro número: "))

if numero1 == 0 or numero2 == 0:
    print("El resultado de la multiplicación es cero.")
elif numero1 < 0 and numero2 < 0:
    print("El resultado de la multiplicación es positivo.")
elif numero1 < 0 or numero2 < 0:
    print("El resultado de la multiplicación es negativo.")
else:
    print("El resultado de la multiplicación es positivo.")