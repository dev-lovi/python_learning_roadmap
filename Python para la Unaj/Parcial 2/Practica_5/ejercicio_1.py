#Ejercicio 1: Escribir un programa que muestre la tabla de multiplicar de un número introducido por teclado por el usuario.

def tabla(x):
    cant = int(input("¿Hasta qué numero querés multiplicar?: "))
    cant = cant + 1
    for valor in range (0, cant):
        print("Para " + str(valor) + " el resultado es: " + str(x * valor))


numero = int(input("Ingresa un numero: "))
tabla(numero)

#otra forma
tabla(5)


