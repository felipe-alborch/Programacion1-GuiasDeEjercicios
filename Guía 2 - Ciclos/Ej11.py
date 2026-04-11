'''
Una empresa textil desea procesar sus ventas. Cada vez que una persona realiza una compra se le entrega una factura donde consta:

 - Nro. de Factura
 - Código de artículo
 - Cantidad del artículo
 - Precio Unitario

En cada factura se registra solamente un código de artículo y los códigos de artículos pueden
ser 1, 3, 5 y 7. Diseñar un programa que permita el Ingreso de los datos y calcular:

a. Total de cada factura
b. Total general facturado
c. Cantidad vendida (en unidades) para cada uno de los artículos.
d. Total de artículos vendidos
e. Cantidad de facturas emitidas para cada uno de los artículos.
f. Nro. de factura con mayor valor (en $)
g. Nro. de artículo con menor cantidad pedida (por factura, "no" el total)
h. Porcentaje de ventas (en pesos) de cada uno de los artículos sobre el total. 

La entrada de datos finaliza con un número de factura igual a cero.
'''

totalFacturado = 0

numeroFacturaDeMayorValor = 0
montoDeFacturaDeMayorValor = 0

menorCantPedidaDeUnProducto = 0
numFactDelProductoMenosPedido = 0
codArtDeLaFacturaMenosPedida = 0

#Acumuladores
cantVendidaArticulo1 = 0
cantVendidaArticulo3 = 0
cantVendidaArticulo5 = 0
cantVendidaArticulo7 = 0
cantFacturadoArticulo1 = 0
cantFacturadoArticulo3 = 0
cantFacturadoArticulo5 = 0
cantFacturadoArticulo7 = 0

#Contadores
cantFacturasEmitidasArticulo1 = 0
cantFacturasEmitidasArticulo3 = 0
cantFacturasEmitidasArticulo5 = 0
cantFacturasEmitidasArticulo7 = 0

numeroDeFactura = int(input("Ingresá un número de factura: "))

while numeroDeFactura != 0:
    codigoDeArticulo = int(input("Ingresá un código de artículo: "))
    while codigoDeArticulo != 1 and codigoDeArticulo != 3 and codigoDeArticulo != 5 and codigoDeArticulo != 7:
        codigoDeArticulo = int(input("Código inválido. Ingresá nuevamente un código de artículo: "))
    
    cantidadArticulo = int(input("Ingresá la cantidad de unidades del artículo comprado: "))
    while cantidadArticulo < 0:
        cantidadArticulo = int(input("Cantidad inválida. Ingresá nuevamente la cantidad de unidades del artículo comprado: "))
    
    precioUnitario = int(input("Ingresá el precio unitario del artículo: "))
    while precioUnitario <= 0:
        precioUnitario = int(input("Precio inválido. Ingresá nuevamente el precio unitario del artículo: "))
    
    totalFacturado += cantidadArticulo * precioUnitario
    
    if numeroFacturaDeMayorValor == 0 or (cantidadArticulo * precioUnitario) > montoDeFacturaDeMayorValor:
        numeroFacturaDeMayorValor = numeroDeFactura
        montoDeFacturaDeMayorValor = cantidadArticulo * precioUnitario
        
    if numFactDelProductoMenosPedido == 0 or cantidadArticulo < menorCantPedidaDeUnProducto:
        numFactDelProductoMenosPedido = numeroDeFactura
        menorCantPedidaDeUnProducto = cantidadArticulo
        codArtDeLaFacturaMenosPedida = codigoDeArticulo
    
    if codigoDeArticulo == 1:
        cantVendidaArticulo1 += cantidadArticulo
        cantFacturasEmitidasArticulo1 += 1
        cantFacturadoArticulo1 += cantidadArticulo * precioUnitario
    elif codigoDeArticulo == 3:
        cantVendidaArticulo3 += cantidadArticulo
        cantFacturasEmitidasArticulo3 += 1
        cantFacturadoArticulo3 += cantidadArticulo * precioUnitario
    elif codigoDeArticulo == 5:
        cantVendidaArticulo5 += cantidadArticulo
        cantFacturasEmitidasArticulo5 += 1
        cantFacturadoArticulo5 += cantidadArticulo * precioUnitario
    else:
        cantVendidaArticulo7 += cantidadArticulo
        cantFacturasEmitidasArticulo7 += 1
        cantFacturadoArticulo7 += cantidadArticulo * precioUnitario
    
    #Punto A
    print(f"El total de la factura {numeroDeFactura} es : {cantidadArticulo * precioUnitario}")
    
    numeroDeFactura = int(input("\nIngresá un número de factura: "))

#Punto B
print(f"\n\nEl total general facturado es: {totalFacturado}")

#Punto C
print(f"\nLa cantidad de unidades vendidad para el artículo 1 es: {cantVendidaArticulo1}.")
print(f"La cantidad de unidades vendidad para el artículo 3 es: {cantVendidaArticulo3}.")
print(f"La cantidad de unidades vendidad para el artículo 5 es: {cantVendidaArticulo5}.")
print(f"La cantidad de unidades vendidad para el artículo 7 es: {cantVendidaArticulo7}.")

#Punto D
print(f"\nLa cantidad total de artículos vendidos es: {cantVendidaArticulo1 + cantVendidaArticulo3 + cantVendidaArticulo5 + cantVendidaArticulo7}")

#Punto E
print(f"\nLa cantidad de facturas emitidas para el artículo 1 es: {cantFacturasEmitidasArticulo1}.")
print(f"La cantidad de facturas emitidas para el artículo 3 es: {cantFacturasEmitidasArticulo3}.")
print(f"La cantidad de facturas emitidas para el artículo 5 es: {cantFacturasEmitidasArticulo5}.")
print(f"La cantidad de facturas emitidas para el artículo 7 es: {cantFacturasEmitidasArticulo7}.")

#Punto F
print(f"\nLa factura {numeroFacturaDeMayorValor} es la de mayor valor, con {montoDeFacturaDeMayorValor} $.")

#Punto G
print(f"\nLa factura {numFactDelProductoMenosPedido} registró la menor cantidad de productos pedidos. Con {menorCantPedidaDeUnProducto} del producto {codArtDeLaFacturaMenosPedida}.")

#Punto H
if totalFacturado != 0:
    print(f"\nDe la totalidad de artículos vendidos, el artículo 1 presentó el {(cantFacturadoArticulo1 * 100) / totalFacturado}% de las ventas.")
    print(f"De la totalidad de artículos vendidos, el artículo 3 presentó el {(cantFacturadoArticulo3 * 100) / totalFacturado}% de las ventas.")
    print(f"De la totalidad de artículos vendidos, el artículo 5 presentó el {(cantFacturadoArticulo5 * 100) / totalFacturado}% de las ventas.")
    print(f"De la totalidad de artículos vendidos, el artículo 7 presentó el {(cantFacturadoArticulo7 * 100) / totalFacturado}% de las ventas.")
else:
    print("No se registaron facturas.")