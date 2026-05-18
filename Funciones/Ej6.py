'''
6. Se ingresan n números. Diseñar un programa que, usando una función, muestre la mitad de aquellos que
son pares
'''

numerosPares = []
n = int(input("Ingrese una cantidad de números a ingresar: "))

def devolverMitad(numeros):
    for i in range(len(numeros)):
        numeros[i] = numeros[i] // 2

for i in range(n):
    numero = int (input("Ingrese un número: "))
    
    if numero % 2 == 0:
        numerosPares.append(numero)
        
devolverMitad(numerosPares)
print(f"\n\nLa mitad de los números pares del arreglo es: {numerosPares}")