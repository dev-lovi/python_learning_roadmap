import datetime

nombre_archivo = "mi_diario.txt"

def escribir_en_diario():
    entrada = input("Escribe tu entrada de diario: ")
    fecha_actual = datetime.datetime.now()
    fecha_formateada = fecha_actual.strftime("%d/%m/%Y %H:%M:%S")
    # Crea el archivo si no existe
    with open(nombre_archivo, "a") as archivo:
        archivo.write(fecha_formateada + " - " + entrada + "\n")
    print("Entrada guardada en el diario.")

def buscar_por_semana():
    fecha_str = input("Ingresa la fecha de la semana que deseas buscar (en formato dd/mm/yyyy): ")
    try:
        fecha_busqueda = datetime.datetime.strptime(fecha_str, "%d/%m/%Y")
        with open(nombre_archivo, "r") as archivo:
            lineas = archivo.readlines()
            print(f"Entradas del {fecha_busqueda.strftime('%d/%m/%Y')}:\n")
            for linea in lineas:
                partes = linea.split(" - ")
                fecha_entrada = datetime.datetime.strptime(partes[0], "%d/%m/%Y %H:%M:%S")
                if fecha_busqueda.date() == fecha_entrada.date():
                    print(linea.strip())
    except ValueError:
        print("Formato de fecha incorrecto. Debe ser dd/mm/yyyy.")

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
    print("\n¿Qué deseas hacer?")
    print("1. Escribir en el diario")
    print("2. Buscar entradas por semana")
    print("3. Leer todas las entradas")
    print("4. Borrar una entrada")
    print("5. Salir")
    
    opcion = input("Selecciona una opción: ")
    
    if opcion == "1":
        escribir_en_diario()
    elif opcion == "2":
        buscar_por_semana()
    elif opcion == "3":
        leer_diario()
    elif opcion == "4":
        borrar_entrada()
    elif opcion == "5":
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")
