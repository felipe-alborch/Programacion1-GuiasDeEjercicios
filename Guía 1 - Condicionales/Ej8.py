'''
8) Ingresar dos números, calcular y mostrar el cociente del primero por el segundo, siempre 
que el divisor no sea cero. En este último caso mostrar la leyenda “no se puede realizar el 
cociente”. 
'''

dividendo = int(input("Ingresá un dividiendo: "))
divisor = int(input("Ingresá un divisor: "))

if(divisor > 0):
    print(dividendo / divisor)
else:
    print("No se puede realizar el cociente")