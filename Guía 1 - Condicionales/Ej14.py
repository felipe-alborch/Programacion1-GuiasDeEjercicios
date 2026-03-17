'''
14) Ingresar un numero de dos cifras, si es mayor que 50 mostrarlo invertido. Sino mostrar la 
cifra que corresponde a las unidades. 
'''

numero = input("Ingresá un número de dos cifras: ")

if len(numero) == 2:
    if int(numero) >= 50:
        nuevoNumero = numero[1] + numero[0]
        print(f"El nuevo número es: {nuevoNumero}")
    else:
        print("El número ingresado es menor que 50.")
else:
    print("No ingresaste un número de dos cifras.")