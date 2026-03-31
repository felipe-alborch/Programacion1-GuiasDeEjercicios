'''
1) Ingresar números hasta un múltiplo de 3. Mostrar el último número ingresado.
'''

contador = 0
numeroFinal = 0
multiploDeTres = int(input("Ingresá un múltiplo de '3': "))

while multiploDeTres % 3 != 0:
    multiploDeTres = int(input("No ingresaste un múltiplo de '3'. Volvé a ingresar un número: "))

while contador < multiploDeTres:
    numero = int(input("Ingresá un número: "))

    numeroFinal = numero
    contador += 1

print(f"El último número ingresado fue: {numeroFinal}")