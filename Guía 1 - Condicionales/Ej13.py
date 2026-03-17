'''
13) El usuario deberá pensar en uno de los siguientes personajes: Lio Messi, Mauricio Macri y 
Mirtha Legrand. El programa mediante algunas preguntas convenientes (edad, sexo, 
ocupación, etc.) deberá mostrar de que personaje se trata. Ejemplo: si es hombre y 
deportista tendrá que decir Lio Messi
'''

sexo = input("Ingrese el sexo del personaje (hombre/mujer): ")
ocupacion = input("Ingrese la ocupación (deportista/politico/conductora): ")
edad = int(input("Ingrese la edad: "))

if sexo == "hombre":
    if ocupacion == "deportista":
        if edad == 38:
            print("El personaje es Lionel Messi")
        else:
            print("No se pudo determinar el personaje")

    elif ocupacion == "politico":
        if edad == 67:
            print("El personaje es Mauricio Macri")
        else:
            print("No se pudo determinar el personaje")

    else:
        print("No se pudo determinar el personaje")

elif sexo == "mujer":
    if ocupacion == "conductora":
        if edad == 99:
            print("El personaje es Mirtha Legrand")
        else:
            print("No se pudo determinar el personaje")

    else:
        print("No se pudo determinar el personaje")

else:
    print("Sexo inválido")