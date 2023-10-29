#Ejercicio 13: Escriba un programa que solicite nombres de localidades y códigos postales al usuario hasta que se ingresa el código postal 0. Debe generar una lista con todos los valores ingresados e imprimirla 

valores = []

while True:
    print("\nMenu del programa") #La \n solo hace un salto de linea para que quede mas prolijo
    print("Opcion 1. Ingresar localidades.")
    print("Opcion 2. Mostrar datos.")
    print("Opcion 3. Salir.")
    opcion = int(input("Elija una opción: "))

    if opcion == 1:
        while True: #Mientras mi condición sea verdadera
            pregunta_nombre = input("Ingrese el nombre de su localidad, ponga '0' para salir: ")
            if pregunta_nombre == "0":
                break #Si la opcion es "0", se que salga del bucle While y vuelve a Elija una opcion
            pregunta_cp = int(input("Ingrese su codigo postal: "))
            valores.append((pregunta_nombre, pregunta_cp))

    elif opcion == 2:
        print("Los datos ingresados por el momento son:")
        print(str(valores)) #Me muestra la lista, si la pongo al inicio no va a mostrar nada porque esta vacia

    elif opcion == 3:
        break #sale del bucle principal while, sale del programa

    else:
        break #sale del bucle principal while, sale del programa

