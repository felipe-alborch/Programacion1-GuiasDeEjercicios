'''
9) Ingresar el valor de la ganancia anual de una empresa y calcular su retención según se 
encuentre dentro de los siguientes parámetros:

Ganancia: <= 10000 
Retención: Cero 
Ganancia: >10000 y <= 15000 
Retención: 2% sobre (ganancia -10000) 
Ganancia: > 150000 
Retención: 300+5% sobre (ganancia -15000)
'''

ganancia = int(input("Ingresá la ganancia anual de una empresa: "))

if ganancia <= 10000:
    print("La retención es nula.")
elif ganancia >10000 and ganancia <= 15000:
    print(f"La retención es de {(ganancia - 10000) * 0.02} $.")
else:
    print(f"La retención es de {(((ganancia - 15000) * 0.05) + 300)} $.")