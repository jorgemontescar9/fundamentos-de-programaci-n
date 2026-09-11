# --- FUNCIONES ---
def sumar_tupla(tupla):
    return sum(tupla)

def buscar_telefono(diccionario, nombre):
    return diccionario.get(nombre)

def contar_palabras(texto):
    return len(texto.split())

# --- SECCIONES ---
def seccion_tuplas():
    print("\n    TUPLAS    ")
    numeros = (10, 25, 30, 45, 50)
    print("Tercer elemento:", numeros[2])
    
    try:
        n1 = float(input("Número adicional 1: "))
        n2 = float(input("Número adicional 2: "))
        nueva_tupla = numeros + (n1, n2)
        
        lista = list(nueva_tupla)
        lista.sort()
        print("Lista ordenada:", lista)
        print("Suma total:", sumar_tupla(nueva_tupla))
    except ValueError:
        print("Error: Ingresa números válidos.")

def seccion_diccionarios():
    print("\n--- 2. DICCIONARIOS ---")
    contactos = {"Carlos": "4421234567", "Ana": "4429876543", "Sofia": "4425551234"}
    
    nombre = input("Nuevo nombre: ").strip()
    tel = input("Nuevo teléfono: ").strip()
    contactos[nombre] = tel
    
    print("\nContactos registrados:")
    for c in contactos.keys():
        print("-", c)
        
    buscar = input("\nNombre a buscar: ").strip()
    resultado = buscar_telefono(contactos, buscar)
    print(f"Teléfono: {resultado}" if resultado else "Contacto no encontrado.")

def seccion_excepciones():
    print("\n--- 3. EXCEPCIONES ---")
    try:
        n1 = int(input("Primer entero: "))
        n2 = int(input("Segundo entero: "))
        print("Suma:", n1 + n2)
        
        if n2 == 0:
            raise ZeroDivisionError("No se puede dividir entre cero.")
        print("División:", n1 / n2)
        
    except ValueError:
        print("Error: Debes ingresar números enteros.")
    except ZeroDivisionError as e:
        print("Error:", e)

def seccion_strings():
    print("\n--- 4. STRINGS ---")
    mensaje = "Python es un lenguaje de programación muy potente y sencillo"
    print("Mensaje:", mensaje)
    print("Longitud:", len(mensaje))
    print("Mayúsculas:", mensaje.upper())
    print("Reemplazo:", mensaje.replace("potente", "versátil"))
    print("Total de palabras:", contar_palabras(mensaje))

# --- MENÚ PRINCIPAL ---
def menu():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Tuplas\n2. Diccionarios\n3. Excepciones\n4. Strings\n5. Finalizar")
        opcion = input("Selecciona una opción (1-5): ").strip()
        
        if opcion == "1":
            seccion_tuplas()
        elif opcion == "2":
            seccion_diccionarios()
        elif opcion == "3":
            seccion_excepciones()
        elif opcion == "4":
            seccion_strings()
        elif opcion == "5":
            print("Programa finalizado.")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()