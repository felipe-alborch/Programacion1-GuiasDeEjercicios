'''
1) Ingresar un arreglo e imprimirlo. Se da como dato el número de componentes del vector.
'''

longitud = int(input("Ingresá la cantidad de elementos que va a tener el arreglo: "))
arreglo = [] 

for i in range(longitud):
    dato = int(input("Ingresá un número: "))

    arreglo.append(dato)

for i in range(longitud):
    print(f"Posición {i}: {arreglo[i]}")