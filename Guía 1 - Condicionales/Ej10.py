'''
10) Calcular el importe que debe pagar un auto en un estacionamiento teniendo en cuenta 
como datos las horas y minutos de uso. El valor de la hora es de $45 y si los minutos 
exceden de 15 se incrementa una hora al importe. El mínimo a cobrar es de una hora. 
'''

horas = int(input("Ingresá la cantidad de horas que estuvo el auto en el estacionamiento: "))
minutos = int(input("Ingresá la cantidad de minutos que estuvo el auto en el estacionamiento: "))

if horas == 0:
    print("El monto a cobrar es de: 45$")
elif minutos > 15:
    print(f"El monto a cobrar es: {(horas * 45) + 45}$")
else:
    print(f"El monto a cobrar es: {horas * 45}$")