# ACTIVIDAD EVALUABLE 2: COBRO DE ENTRADAS DEL MUSEO CON RESTRICCIONES DE CONTROL
# Nombre del alumno: Jorge Leonardo Montes Cardona
# Matrícula: al03083990
# Fecha: 21 de agosto de 2026

# Precios:
niños_menores_de_3_años = 0
niños_menores_de_edad_3_a_17_años = 30
mayores_de_18_años = 45

# Descuentos:
Descuento_adulto_mayor = 0.12
Descuento_profesor = 0.10
Descuento_estudiante = 0.10
Sin_descuento = 0.00

print("SISTEMA DE COBRO: MUSEO DE ANTROPOLOGÍA E HISTORIA")
monto_total_acumulado = 0
boletos_procesados = 0

# Solicitud de cantidad de visitantes:
visitante = int(input("Ingrese la cantidad visitantes: "))

# Solicitud de edad de cada visitante:
for i in range(visitante):
    print(f"\nVisitante {i+1}:")
    edad = int(input("Ingrese su edad: "))

    # Precios bases
    if edad < 3:
        precio_base = niños_menores_de_3_años
    elif edad >= 3 and edad <= 17:
        precio_base = niños_menores_de_edad_3_a_17_años
    else:
        precio_base = mayores_de_18_años

    # Solicitud de tipo de descuento (DENTRO DEL CICLO):
    Tipo_de_descuento = input("¿Perteneces a alguno de estos? (1: Estudiante, 2: Profesor, 3: Adulto Mayor, 4: Ninguno): ")
    
    es_adulto_mayor = (Tipo_de_descuento == "3") or (edad >= 60)
    es_profesor = (Tipo_de_descuento == "2") and not es_adulto_mayor
    es_estudiante = (Tipo_de_descuento == "1") and not es_adulto_mayor and not es_profesor

    if es_adulto_mayor:
        descuento = Descuento_adulto_mayor
        tipo_str = "Adulto Mayor (12%)"
    elif es_profesor:
        descuento = Descuento_profesor
        tipo_str = "Profesor (10%)"
    elif es_estudiante:
        descuento = Descuento_estudiante
        tipo_str = "Estudiante (10%)"
    else:
        descuento = Sin_descuento
        tipo_str = "Ninguno (0%)"

    # Cálculos individuales por visitante
    descuento_final = precio_base * descuento
    sub_total = precio_base - descuento_final
    
    # Acumuladores
    monto_total_acumulado += sub_total
    boletos_procesados += 1

# Impresión del resumen (FUERA DEL CICLO)
print("\n" + "="*50)
print("              RESUMEN FINAL DE COMPRA             ")
print("="*50)
print(f"Boletos cobrados    : {boletos_procesados}")
print(f"Total general a pagar: ${monto_total_acumulado:.2f}")
print("="*50)