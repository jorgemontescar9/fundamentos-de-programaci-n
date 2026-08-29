# Avance de Proyecto
# Registro de Inventario y Cálculo de Descuentos

print("==========================================================")
print("     SISTEMA BASE DE INVENTARIO Y DESCUENTOS")
print("==========================================================")

#Datos
nombre_producto = input("Ingrese el nombre del producto: ")
precio_por_unidad = float(input("Ingrese el precio por unidad: "))
stock_inicial = int(input("Ingrese el stock inicial disponible: "))

print("\n REGISTRO DE SALIDA")
cantidad_de_productos_solicitados = int(input(f"¿Cuántas unidades de '{nombre_producto}' desea retirar?: "))

# Acumulacion de descuentos
porcentaje_descuento = 0.0

# Estructuras de control para aplicar reglas de descuento
if cantidad_de_productos_solicitados <= stock_inicial:
    # Regla de negocio: Descuento por 5 o mas unidades
    if cantidad_de_productos_solicitados >= 5:
        porcentaje_descuento += 0.10
        print("Se aplico un 10% de descuento por volumen.")
        
    # Regla de negocio: Descuento por retirar la mitad o más del stock
    if cantidad_de_productos_solicitados >= (stock_inicial / 2):
        porcentaje_descuento += 0.05
        print("Se aplico un 5% de descuento adicional.")

    #Calculos matematicos:
    subtotal = cantidad_de_productos_solicitados * precio_por_unidad
    monto_descuento = subtotal * porcentaje_descuento
    total_pagar = subtotal - monto_descuento
    stock_final = stock_inicial - cantidad_de_productos_solicitados

    # Salida de datos
    print("\n==========================================================")
    print("                RESUMEN DE LA OPERACIÓN")
    print("==========================================================")
    print(f"Producto:                    {nombre_producto}")
    print(f"Precio por unidad:           ${precio_por_unidad:.2f}")
    print(f"Unidades retiradas:          {cantidad_de_productos_solicitados}")
    print(f"Subtotal:                    ${subtotal:.2f}")
    print(f"Descuento total  ({porcentaje_descuento * 100:.0f}%):     -${monto_descuento:.2f}")
    print(f"Total a pagar:               ${total_pagar:.2f}")
    print("----------------------------------------------------------")
    print(f"Stock restante en almacén:   {stock_final} unidades")
    print("==========================================================")

else:
    print("\n==========================================================")
    print(f"ERROR: Stock insuficiente en almacén.")
    print(f"Intentaste retirar {cantidad_de_productos_solicitados} unidades, pero solo hay {stock_inicial} disponibles.")
    print("==========================================================")