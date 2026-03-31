'''
6) Ingresar 10 números mayores a 3 y menores a 8. Mostrar el valor ingresado en números y
letras.
'''

for i in range(1,11):
    numero = int(input("Ingresá un número (>3 y <8): "))
    
    while numero <= 3 or numero >= 8:
        numero = int(input("Número inválido. Ingresá un número (>3 y <8): "))
    
    if numero == 4:
        print("El número ingresado es: 4 (cuatro)")
    elif numero == 5:
        print("El número ingresado es: 5 (cinco)")
    elif numero == 6:
        print("El número ingresado es: 6 (seis)")
    elif numero == 7:
        print("El número ingresado es: 7 (siete)")