'''
En base a los conceptos vistos, se pide realizar el siguiente ejercicio.
Diseñar un programa en Python que permita:

 - Leer dos números enteros desde el teclado y luego un operador matematico. Se pide mostrar el resultado de la operación mediante un mensaje.
 - Los operadores que se pueden ingresar son la suma, la resta, la multiplicación, la división y la potencia.
 - Si en alguno de los casos no se puede realizar la operación informarlo mediante un mensaje de error.
'''

numero1 = int(input("Ingresá un número: "))
numero2 = int(input("Ingresá otro número: "))
operador = input("Ingresá un operador matemático ('+', '-', '*', '**' o '/'): ")

if operador == '+':
    print(f"El resultado de la suma es: {numero1 + numero2}.")
elif operador == '-':
    print(f"El resultado de la resta es: {numero1 - numero2}.")
elif operador == '*':
    print(f"El resultado de la multiplicación es: {numero1 * numero2}.")
elif operador == "**":
    print(f"El resultado de la potencia es: {numero1 ** numero2}.")
elif operador == '/':
    if numero2 != 0:
        print(f"El resultado de la división es: {numero1 / numero2}.")
    else:
        print("No se puede realizar la división. El divisor es igual a cero.")
else:
    print("El operador ingresado es desconocido.")