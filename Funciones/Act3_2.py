'''
Definir las siguientes funciones:

maximo: Esta función recibe dos números como parámetro e identifica cual es el máximo de los valores ingresados.

es_positivo: Esta función recibe como parámetro un numero e indica si el numero ingresado es un numero positivo.

modulo: Esta función recibe un numero entero como parámetro y devuelve el modulo del numero recibido.

cantidad_digitos: Esta función recibe un numero entero positivo como parámetro y retorna la cantidad de dignos del numero (No usar len)

es_capucua: esta función recibe un numero entero positivo como parámetro e indica si el numero es capicúa (EJ: 123321). (No convertir a string)

Realiza un programa que verifique el funcionamiento correcto de cada función

NOTA: Resolver las funciones utilizando lógica de programación y no soluciones que provee el lenguaje.
'''

def maximo(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2
    
def es_positivo(numero):
    if numero > 0:
        print("El número ingresado es positivo.")
    else:
        print("El número ingresado no es positivo.")

def modulo(numero):
    if numero >= 0:
        return numero
    else:
        return numero * (-1)
    
def cantidad_digitos(numero):
    contador = 0

    for i in numero:
        contador += 1

    return contador

num1 = int(input("Ingresá un número:"))
num2 = int(input("Ingresá un número:"))

maximoo = maximo(num1, num2)
print(maximoo)

print("\n")

es_positivo(num1)
es_positivo(num2)

print("\n")

mod1= modulo(num1)
mod2 = modulo(num2)
print(mod1, mod2)

print("\n")

modulo(num1)
modulo(num2)

cant1 = cantidad_digitos(str(num1))
cant2 = cantidad_digitos(str(num2))
print(cant1, cant2)