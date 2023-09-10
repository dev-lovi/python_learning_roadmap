nombre_archivo = "mi_listado.txt"

def escribir_en_diario():
    entrada = input("Escribí producto y precio: ")
    # Crea el archivo si no existe
    with open(nombre_archivo, "a") as archivo:
        archivo.write(entrada + "\n")  # Agregar '\n' para separar las entradas
    print("Entrada guardada.")

def buscar_por_alfabeto():
    rango = input("Ingresa un rango de letras para buscar entradas (por ejemplo, A-G): ")
    rango = rango.upper()
    
    if len(rango) != 3 or rango[1] != '-':
        print("Formato de rango no válido. Debe ser en el formato A-G.")
        return
    
    inicio = ord(rango[0])
    fin = ord(rango[2])

    with open(nombre_archivo, "r") as archivo:
        lineas = archivo.readlines()

    encontradas = []
    for linea in lineas:
        primera_letra = linea.strip()[0].upper()
        if inicio <= ord(primera_letra) <= fin:
            encontradas.append(linea.strip())

    if encontradas:
        print(f"Entradas que comienzan con letras en el rango '{rango}':")
        for entrada in encontradas:
            print(entrada)
    else:
        print(f"No se encontraron entradas que coincidan con el rango '{rango}'.")


def rescribir_entrada():
    with open(nombre_archivo, "r") as archivo:
        lineas = archivo.readlines()

    if not lineas:
        print("El diario está vacío.")
        return

    print("Entradas disponibles para reescribir:")
    for i, linea in enumerate(lineas):
        print(f"{i + 1}. {linea.strip()}")

    try:
        numero_entrada = int(input("Selecciona el número de la entrada que deseas reescribir: "))
        if 1 <= numero_entrada <= len(lineas):
            nueva_entrada = input("Escribe la nueva entrada: ")
            lineas[numero_entrada - 1] = nueva_entrada + "\n"
            with open(nombre_archivo, "w") as archivo:
                archivo.writelines(lineas)
            print("Entrada reescrita con éxito.")
        else:
            print("Número de entrada no válido.")
    except ValueError:
        print("Entrada no válida. Debe ser un número.")


def buscar_por_letra():
    letra = input("Ingresa una letra para buscar entradas que comiencen con esa letra: ")
    with open(nombre_archivo, "r") as archivo:
        lineas = archivo.readlines()

    encontradas_letra = []
    for linea in lineas:
        if linea.strip().lower().startswith(letra.lower()):
            encontradas_letra.append(linea.strip())

    if encontradas_letra:
        print(f"Entradas que comienzan con '{letra}':")
        for entrada in encontradas_letra:
            print(entrada)
    else:
        print(f"No se encontraron entradas que comiencen con '{letra}'.")

def leer_diario():
    with open(nombre_archivo, "r") as archivo:
        contenido = archivo.read()
        print("Contenido del diario:\n")
        print(contenido)

def borrar_entrada():
    with open(nombre_archivo, "r") as archivo:
        lineas = archivo.readlines()

    if not lineas:
        print("El diario está vacío.")
        return

    print("Entradas disponibles para borrar:")
    for i, linea in enumerate(lineas):
        print(f"{i + 1}. {linea.strip()}")

    try:
        numero_entrada = int(input("Selecciona el número de la entrada que deseas borrar: "))
        if 1 <= numero_entrada <= len(lineas):
            entrada_borrada = lineas.pop(numero_entrada - 1)
            with open(nombre_archivo, "w") as archivo:
                archivo.writelines(lineas)
            print(f"Entrada borrada: {entrada_borrada.strip()}")
        else:
            print("Número de entrada no válido.")
    except ValueError:
        print("Entrada no válida. Debe ser un número.")


while True:
    print("Lista de precios")
    print("¿Qué deseas hacer?")
    print("1. Escribir en la lista")
    print("2. Buscar por alfabeto")
    print("3. Buscar por letra")
    print("4. Leer todas las entradas")
    print("5. Rescribir una entrada")
    print("6. Borrar una entrada")
    print("7. Salir")
    
    opcion = input("Selecciona una opción: ")
    
    if opcion == "1":
        escribir_en_diario()
    elif opcion == "2":
        buscar_por_alfabeto()
    elif opcion == "3":
        buscar_por_letra()
    elif opcion == "4":
        leer_diario()
    elif opcion == "5":
        rescribir_entrada()
    elif opcion == "6":
        borrar_entrada()
    elif opcion == "7":
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")