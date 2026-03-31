'''
3) Ingresar números hasta que el último sea cero. Calcular la cantidad de positivos.
'''

cantidadDePositivos = 0
numero = int(input("Ingresá un número: "))

while numero != 0:
    if numero > 0:
        cantidadDePositivos += 1

    numero = int(input("Ingresá un número: "))

print(f"La cantidad de números positivos ingresados es: {cantidadDePositivos}")