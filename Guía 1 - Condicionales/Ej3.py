'''
3) Convertir longitudes de millas a Km. y de pulgadas a cm., si: 

1 milla = 1.60935 Km. 
1 pulgada = 2.534 cm
'''

millasIngresadas = int(input("Ingrese un número de millas: "))
pulgadasIngresadas = int(input("Ingrese un número de pulgadas: "))

pasajeKms = millasIngresadas * 1.60935
pasajeCms = pulgadasIngresadas * 2.534

print(f"KMs obtenidos de la conversión: {pasajeKms}")
print(f"CMs obtenidos de la conversión: {pasajeCms}")