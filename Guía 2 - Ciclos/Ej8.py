'''
8) Se ingresan 100 números enteros positivos, por cada número ingresado se le solicita al operador
que seleccione la operación a realizar: si el operador ingresa 1, el programa debe devolver el
factorial del número ingresado; si el operador ingresa 2, el programa debe solicitarle al operador
la potencia a la cual quiere elevar el número ingresado y debe mostrar el resultado y para
cualquier otro valor de operación el programa debe informar si el número ingresado es par,
impar o nulo
'''

import math

for i in range(1,4):
    numero = int(input("Ingresá un número: "))
    
    while numero < 0:
        numero = int(input("Número inválido. Ingresá nuevamentee un número: "))
    
    opcion = int(input("Selecioná la operación a realizar: "))
    
    if opcion == 1:
        print(f"El factorial del número ingresado es: {math.factorial(numero)}.")
    elif opcion == 2:
        potencia = int(input("Ingresá la potencia a la que queres elevar el número: "))
        print(f"El resultado de elevar {numero} a la {potencia} es: {numero**potencia}.")
    else:
        if numero == 0:
            print("El número es 0 (cero).")
        elif numero % 2 == 0:
            print(f"El número {numero} es par.")
        else:
            print(f"El número {numero} es impar.")