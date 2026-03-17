'''
11) Se ingresa el código de tipo de llamada: 1. Local 2. Interurbana 3. Internacional y la 
duración en minutos de la misma. Si el minuto cuesta $0.25 para la llamada local, 
$0.40 para la llamada interurbana y $1.05 para la llamada internacional, diseñar un 
algoritmo que permita calcular el monto a pagar por dicha llamada.
'''

tipoDeLlamada = int(input("Ingresá el tipo de llamada a realizar: "))

match(tipoDeLlamada):
    case 1:
        print("El valor por minuto del tipo de llamada LOCAL es: $0.25")
    case 2:
        print("El valor por minuto del tipo de llamada INTERURBANA es: $0.40")
    case 3:
        print("El valor por minuto del tipo de llamada INTERNACIONAL es: $1.05")
    case _: 
        print("Tipo de llamada desconocida")