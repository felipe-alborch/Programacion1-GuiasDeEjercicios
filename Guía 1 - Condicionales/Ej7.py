'''
7) Ingresar las edades de dos personas. Si una de ellas es mayor de edad y la otra menor de edad, 
calcular y mostrar su promedio. En caso contrario mostrar las dos edades. 
'''

personaUno = int(input("Ingresá la edad de la primera persona: "))
personaDos = int(input("Ingresá la edad de la segunda persona: "))

if personaUno >= 18 and personaDos < 18:
    print((personaUno + personaDos) / 2)
else:
    print(f"La edad de la persona uno es {personaUno} y la edad de la persona dos es {personaDos}")