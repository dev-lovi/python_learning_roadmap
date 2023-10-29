#Ejercicio 15: Escriba un programa que le muestre a la persona usuaria el siguiente menú de opciones. El mismo debe estar siempre activo y, de acuerdo a la opción elegida, le solicite los datos restantes para imprimir el área de la figura elegida:

#Menú de opciones
#1.- Círculo
#2.- Cuadrado
#3.- Rectángulo
#4.- Salir


while True:
    print("Menu de opciones")
    print("1. Circulo")
    print("2. Cuadrado")
    print("3. Rectangulo")
    print("4. Salir")
    opcion = int(input("Elegí una opción wachin: "))

    if opcion == 1:
        print("Circulo")
        pregunta = int(input("Ingrese el radio, ponga 0 para salir: "))
        if pregunta == 0:
            break
        else:
            calculo = 3.14 * (pregunta * pregunta)
            print("El area es " + str(calculo))
    elif opcion == 2:
        print("Cuadrado")
        pregunta = int(input("Ingrese el lado, ponga 0 para salir: "))
        if pregunta == 0:
            break
        else:
            calculo = pregunta * pregunta
            print("El area es " + str(calculo))
    elif opcion == 3:
        print("Rectangulo")
        pregunta = int(input("Ingrese el lado 1, ponga 0 para salir: "))
        pregunta2 = int(input("Ingrese el lado 2, ponga 0 para salir: "))
        if pregunta == 0:
            break
        else:
            calculo = pregunta * pregunta2
            print("El area es " + str(calculo))
    elif opcion == 4:
        break