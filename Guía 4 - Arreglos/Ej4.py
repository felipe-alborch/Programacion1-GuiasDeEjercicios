'''
4) Dado un arreglo, imprimir los valores máximo y mínimo.
'''

arreglo = []
maximo = -1
minimo = -1

cantidadDeComponentes = int(input("Ingrese la cantidad de componentes que tendrá el arreglo: "))
for i in range(cantidadDeComponentes):
    dato = int(input("Ingresá un número: "))

    arreglo.append(dato)

    if i == 0 or arreglo[i] > maximo:
        maximo = arreglo[i]

    if i == 0 or arreglo[i] < minimo:
        minimo = arreglo[i]

if cantidadDeComponentes > 0 :
    print(f"\n\nEl valor máximo del arreglo es: {maximo}.")
    print(f"El valor mínimo del arreglo es: {minimo}.")
else:
    print("\n\nNo se ingresaron datos.")