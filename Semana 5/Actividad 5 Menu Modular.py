def sumar_tupla(tupla_numeros):
    return sum(tupla_numeros)

def buscar_telefono(diccionario, nombre):
    return diccionario.get(nombre, "Contacto no encontrado")

def contar_palabras(texto):
    return len(texto.split())

def seccion_tuplas():
    print("\nTUPLAS")
    numeros = (10, 25, 30, 45, 50)
    print("Tercer elemento:", numeros[2])
    
    try:
        n1 = float(input("Número adicional 1: "))
        n2 = float(input("Número adicional 2: "))
        nueva_tupla = numeros + (n1, n2)
        
        lista_ordenada = list(nueva_tupla)
        lista_ordenada.sort()
        print("Lista ordenada:", lista_ordenada)
        
        suma_total = sumar_tupla(nueva_tupla)
        print("Suma total:", suma_total)
    except ValueError:
        print("Error: Por favor ingresa números válidos.")

def seccion_diccionarios():
    print("\n--- SECCION DICCIONARIOS ---")
    contactos = {
        "Ana": "555-0101",
        "Luis": "555-0102",
        "Mia": "555-0103"
    }
    
    nombre_nuevo = input("Nombre del nuevo contacto: ")
    telefono_nuevo = input("Telefono del nuevo contacto: ")
    contactos[nombre_nuevo] = telefono_nuevo
    
    print("\nContactos registrados:")
    for nombre in contactos.keys():
        print(nombre)
        
    nombre_buscar = input("\nNombre a buscar: ")
    telefono = buscar_telefono(contactos, nombre_buscar)
    print("El telefono es:", telefono)

def seccion_excepciones():
    print("\n--- SECCION EXCEPCIONES ---")
    try:
        num1 = int(input("Primer numero entero: "))
        num2 = int(input("Segundo numero entero: "))
        
        suma = num1 + num2
        print("La suma es:", suma)
        
        division = num1 / num2
        print(f"{num1} dividido entre {num2} es: {division}")
        
    except ValueError:
        print("Error: Tienes que meter numeros enteros.")
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero. Ingresa un divisor distinto de 0.")

def seccion_strings():
    print("\n--- SECCION STRINGS ---")
    mensaje = "Python es un lenguaje poderoso"
    print("Longitud del mensaje:", len(mensaje))
    print("En mayusculas:", mensaje.upper())
    
    mensaje_modificado = mensaje.replace("Python", "programacion")
    print("Texto reemplazado:", mensaje_modificado)
    
    total_palabras = contar_palabras(mensaje)
    print("Palabras totales:", total_palabras)

def menu_principal():
    opcion = ""
    while opcion != "5":
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Tuplas")
        print("2. Diccionarios")
        print("3. Excepciones")
        print("4. Strings")
        print("5. Finalizar")
        
        opcion = input("Selecciona una opción (1-5): ")
        
        if opcion == "1":
            seccion_tuplas()
        elif opcion == "2":
            seccion_diccionarios()
        elif opcion == "3":
            seccion_excepciones()
        elif opcion == "4":
            seccion_strings()
        elif opcion == "5":
            print("\nPrograma terminado.")
        else:
            print("Opcion no valida, pon un numero del 1 al 5.")

menu_principal()