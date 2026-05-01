'''
2) Ingresar un arreglo de 10 componentes: 

a. Imprimir la cuarta componente. 
b. Imprimir las componentes en orden invertida. 
c. Imprimir el producto entre la primera y la última componente. 
d. Imprimir las componentes de índice impar. 
e. Imprimir la suma de las componentes de índice par. 
f. Imprimir la multiplicación de las componentes de índice impar. 
g. Imprimir el arreglo que resulta de intercambiar la primera con la última componente
'''

arreglo = []

# Llenando el arreglo
for i in range(10):
    dato = int(input("Ingresá un número: "))

    arreglo.append(dato)

# Punto A
print(f"\n\nComponente 4: {arreglo[3]}.")

# Punto B
arreglo.reverse()

for i in range(10):
    print(f"Posición {i}: {arreglo[i]}.")

arreglo.reverse()

# Punto C
print(f"\n\nEl producto entre {arreglo[0]} y {arreglo[9]} es: {arreglo[0] * arreglo[9]}.")

# Punto D
for i in range(10):
    if i % 2 != 0:
        print(f"Exponente {i}, valor: {arreglo[i]}")

# Punto E
suma = 0

for i in range(10):
    if i % 2 == 0:
        suma += arreglo[i]

print(f"\n\nLa suma de las componentes de índice par es: {suma}.")

# Punto F
multiplicacion = 1

for i in range(10):
    if i % 2 != 0:
        suma *= arreglo[i]

print(f"La múltiplicación de las componentes de índice impar es: {multiplicacion}.")

# Punto G
auxiliar = arreglo[0]
arreglo[0] = arreglo[9]
arreglo[9] = auxiliar

for i in range(10):
    print(f"Posición {i}: {arreglo[i]}.")