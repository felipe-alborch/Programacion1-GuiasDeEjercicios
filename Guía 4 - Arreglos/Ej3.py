'''
3) Dados dos arreglos A y B de N<15 elementos cada uno, calcular un arreglo C tal que C = A + B.
'''

arregloA = []
arregloB = []
arregloC = []

cantidadDeComponentes = int(input("Ingrese la cantidad de componentes que tendrán los arreglos A y B: "))

print("Llenando el arreglo 'A'...")
for i in range(cantidadDeComponentes):
    dato = int(input("Ingresá un número: "))

    arregloA.append(dato)

print("\nLlenando el arreglo 'B'...")
for i in range(cantidadDeComponentes):
    dato = int(input("Ingresá un número: "))

    arregloB.append(dato)

print("\nHaciendo el arreglo 'C'...")
for i in range(cantidadDeComponentes):
    suma = arregloA[i] + arregloB[i]

    arregloC.append(suma)

# Mostrando el arreglo 'C'
print("\n\n")
for i in range(10):
    print(f"Posición {i}: {arregloC[i]}.")