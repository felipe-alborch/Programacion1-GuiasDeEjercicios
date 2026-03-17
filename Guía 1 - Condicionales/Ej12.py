'''
12)  Calcular los kilómetros recorridos por un automóvil conociendo el kilometraje inicial y el 
actual. Mostrar una leyenda según la distancia recorrida: 

Para 100 Km. o menos: “Paciencia, falta mucho” 
Más de 100 Km. y menos de 200: “Parar para desayunar” 
Más de 200 Km.: “Se recomienda cargar combustible” 
'''

kilometrajeInicial = int(input("Ingresá el kilometraje inicial del automóvil: "))
kilometrajeActual = int(input("Ingresá el kilometraje actual del automóvil: "))

kilometrosRecorridos = kilometrajeActual - kilometrajeInicial
print(f"\nLos kilometros recorridos por el automóvil son: {kilometrosRecorridos}")

if kilometrosRecorridos <= 100:
    print("Paciencia, falta mucho\n")
elif kilometrosRecorridos > 100 and kilometrosRecorridos < 200:
    print("Parar para desayunar\n")
else:
    print("Se recomienda cargar combustible\n")