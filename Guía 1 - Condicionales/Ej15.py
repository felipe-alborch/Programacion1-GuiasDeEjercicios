'''
15) Ingresar la medida de un ángulo y determinar si es agudo, obtuso, recto, nulo o llano. Si el 
valor ingresado es mayor a 180º mostrar la leyenda “ángulo no válido” e ingresar un nuevo 
valor. 
'''

angulo = int(input("Ingrese el valor del angulo a analizar: "))

if angulo == 0:
    print("El ángulo es nulo.")
elif angulo > 0 and angulo < 90:
    print("El ángulo es agudo.")
elif angulo == 90:
    print("El ángulo es recto.")
elif angulo > 90 and angulo < 180:
    print("El ángulo es obtuso.")
else:
    print("El ángulo ingresado es invalido.")