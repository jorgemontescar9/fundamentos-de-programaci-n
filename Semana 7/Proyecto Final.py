import time
import os

# ==========================================================
# 1. SOLICITAR USUARIO Y CARGA DE PANTALLA
# ==========================================================

# Guardo en la variable nickname el nombre que ingresa el usuario
nickname = input("Ingrese su nombre o nickname de usuario: ").strip()

# Formateo un mensaje con marco estético usando concatenación (+) y repetición (*)
mensaje_bienvenida = "\n" + "=" * 55 + "\n" + "  ¡BIENVENIDO/A AL SISTEMA DE INVENTARIO, " + nickname + "!  \n" + "=" * 55
print(mensaje_bienvenida)

# Hago una pausa de 5 segundos simulando que el sistema carga sus módulos
print("\n[+] Cargando programa...")
for segundo in range(1, 6):
    print(f"Cargando módulos de inventario... ({segundo}/5s)")
    time.sleep(1)
print("[✓] Sistema listo.\n")

# Creo la lista con los 4 archivos base requeridos para evitar errores de lectura
archivos = ["inventario_general.txt", "stock_almacen.txt", "reporte_materiales.txt", "historial_productos.txt"]

# Recorro la lista y creo los archivos de texto únicamente si no existen en la carpeta
for a in archivos:
    if not os.path.exists(a):
        f = open(a, "w", encoding="utf-8")
        f.write(f"--- ARCHIVO DE REGISTRO: {a} ---\nEstado: Activo\n")
        f.close()

# ==========================================================
# 2. CICLO DEL MENÚ Y CONTROL DE OPCIONES
# ==========================================================

# Defino la variable para controlar la opción seleccionada en el ciclo while
opcion = ""

# Repito el programa continuamente hasta que el usuario elija la opción 4
while opcion != "4":
    # Defino una matriz (lista de listas) que almacena la estructura visual del menú
    matriz_menu = [
        ["1", "Registrar Producto", "Captura datos del producto y los guarda en un archivo"],
        ["2", "Consultar Archivos", "Muestra el diccionario de archivos y permite leer su contenido"],
        ["3", "Cambiar Usuario", "Permite actualizar el nickname del usuario actual"],
        ["4", "Salir", "Cierra el sistema de inventarios"]
    ]
    
    # Imprimo los encabezados y bordes de la tabla del menú
    print("\n" + "=" * 62)
    print(f"         MENÚ DE INVENTARIO (Usuario activo: {nickname})")
    print("=" * 62)
    print(f"{'ID':<4} | {'OPCIÓN':<20} | {'DESCRIPCIÓN'}")
    print("-" * 62)
    
    # Recorro la matriz para imprimir cada fila ordenada en columnas
    for fila in matriz_menu:
        print(f"{fila[0]:<4} | {fila[1]:<20} | {fila[2]}")
        
    print("=" * 62)
    
    # Solicito al usuario que elija un número de opción de la matriz
    opcion = input("\nSeleccione una opción de la matriz (1-4): ").strip()
    
    # ------------------------------------------------------
    # OPCIÓN 1: CAPTURA DE DATOS, CÁLCULO Y ESCRITURA EN ARCHIVO
    # ------------------------------------------------------
    if opcion == "1":
        print("\n" + "=" * 55)
        print("           REGISTRAR Y MODIFICAR PRODUCTO")
        print("=" * 55)
        
        # Pido los datos de la fecha por separado para armar la tupla
        print("\nIngresa la fecha de hoy:")
        dia = int(input("Día (DD): "))
        mes = int(input("Mes (MM): "))
        anio = int(input("Año (AAAA): "))
        
        # Guardo la fecha en formato de tupla como lo pide la instrucción (dia, mes, anio)
        fecha_tupla = (dia, mes, anio)
        fecha_texto = f"{fecha_tupla[0]:02d}/{fecha_tupla[1]:02d}/{fecha_tupla[2]}"
        
        # Pido la información general del producto y existencias
        nombre = input("Nombre del producto: ")
        material = input("Material del producto (ej. Plástico, Madera, Metal): ")
        precio = float(input("Precio por unidad: "))
        stock = int(input("Stock inicial disponible: "))
        
        # Pregunto cuántas piezas se van a retirar del almacén
        cantidad = int(input(f"¿Unidades a retirar de '{nombre}'?: "))
        
        # Evalúo si hay suficiente inventario disponible para realizar la operación
        if cantidad <= stock:
            descuento = 0.0
            
            # Verifico si aplica el primer descuento por llevar 5 piezas o más (10%)
            if cantidad >= 5:
                descuento = descuento + 0.10
                print(" -> Se aplicó 10% de descuento por volumen.")
                
            # Verifico si aplica el segundo descuento por llevarse la mitad o más del stock (5%)
            if cantidad >= (stock / 2):
                descuento = descuento + 0.05
                print(" -> Se aplicó 5% de descuento adicional por retiro de stock.")
                
            # Calculo el subtotal, descuento aplicado y total final
            subtotal = cantidad * precio
            monto_descuento = subtotal * descuento
            total = subtotal - monto_descuento
            stock_restante = stock - cantidad
            
            # Formateo el bloque de texto que voy a mostrar y guardar en el archivo
            resumen = (
                f"\n--- REGISTRO [{fecha_texto}] | Registrado por: {nickname} ---\n"
                f"Producto: {nombre} | Material: {material}\n"
                f"Precio Unitario: ${precio:.2f} | Retirados: {cantidad}\n"
                f"Subtotal: ${subtotal:.2f} | Descuento: -${monto_descuento:.2f}\n"
                f"Total Pagado: ${total:.2f} | Stock Restante: {stock_restante}\n"
                f"----------------------------------------------------------\n"
            )
            print(resumen)
            
            # Pregunto en qué archivo de texto se desea guardar el registro
            nom_archivo = input("Nombre del archivo a guardar (ej. inventario_general.txt): ").strip()
            
            # Abro el archivo en modo "a" (append) para agregar la información sin borrar lo anterior
            try:
                f = open(nom_archivo, "a", encoding="utf-8")
                f.write(resumen)
                f.close()
                print(f"  [✓] Registro guardado exitosamente en '{nom_archivo}'.")
            except Exception:
                print("  [ERROR]: No se pudo escribir en el archivo.")
        else:
            # Muestro mensaje de error si la cantidad solicitada supera el stock
            print(f"\n  [ERROR]: Stock insuficiente. Disponible: {stock}.")
            
    # ------------------------------------------------------
    # OPCIÓN 2: DICCIONARIO DE ARCHIVOS Y LECTURA DE CONTENIDO
    # ------------------------------------------------------
    elif opcion == "2":
        print("\n" + "=" * 55)
        print("            CONSULTAR LISTA DE ARCHIVOS")
        print("=" * 55)
        
        # Busco en la carpeta local únicamente los archivos con extensión .txt
        archivos_txt = []
        for a in os.listdir():
            if a.endswith('.txt'):
                archivos_txt.append(a)
                
        # Construyo un diccionario {clave_numérica: nombre_del_archivo}
        diccionario = {}
        posicion = 1
        for a in archivos_txt:
            diccionario[posicion] = a
            posicion = posicion + 1
            
        # Muestro en pantalla las claves y nombres de los archivos disponibles
        print("Diccionario de archivos disponibles:")
        for clave in diccionario:
            print(f"  [{clave}] {diccionario[clave]}")
            
        # Pido el nombre del archivo de texto que el usuario quiere leer
        archivo_elegido = input("\nIngrese el nombre exacto del archivo que desea abrir: ").strip()
        
        # Intento abrir y leer el archivo capturando posibles excepciones
        try:
            f = open(archivo_elegido, "r", encoding="utf-8")
            print("\n" + "-" * 50)
            print(f" CONTENIDO Y STOCK DE: {archivo_elegido}")
            print("-" * 50)
            print(f.read())
            f.close()
            print("-" * 50)
        except FileNotFoundError:
            # Capturo el error si el usuario escribió mal el nombre del archivo
            print(f"\n  [ERROR]: El archivo '{archivo_elegido}' no existe o está mal escrito.")
            
    # ------------------------------------------------------
    # OPCIÓN 3: ACTUALIZAR NOMBRE O NICKNAME DEL USUARIO
    # ------------------------------------------------------
    elif opcion == "3":
        nickname = input("\nIngrese el nuevo nombre o nickname: ").strip()
        print(f"¡Usuario cambiado exitosamente a: {nickname}!")
        
        # Muestro la pantalla de espera de 5 segundos al cambiar de usuario
        print("\n[+] Cargando programa...")
        for segundo in range(1, 6):
            print(f"Cargando módulos de inventario... ({segundo}/5s)")
            time.sleep(1)
        print("[✓] Sistema listo.\n")
        
    # ------------------------------------------------------
    # OPCIÓN 4: SALIR DEL PROGRAMA
    # ------------------------------------------------------
    elif opcion == "4":
        print(f"\nSaliendo del sistema... ¡Hasta luego, {nickname}!")
        
    # Manejo de opción inválida fuera del rango 1-4
    else:
        print("\n  [X] Opción no válida. Ingrese un número de la matriz (1-4).")