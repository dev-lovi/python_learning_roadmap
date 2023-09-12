#EJERCICIOS A ENTREGAR TP N° 2

#Pedir datos de 4 productos comprados, con su cantidad(entero) y precio unitario(decimal).
#Mostrar cuánto se gasta por cada producto y el total gastado
#Imprimir por cada producto un mensaje que muestre los datos, por ejemplo con dos   productos, el resultado seria:

#Productos comprados:
#Nombre: nombre_producto1 Precio: precio_producto1
#Nombre: nombre_producto2 Precio: precio_producto2
#******************************Total gastado: total

#Imprimir las iniciales de cada producto
#Imprimir el ultimo caracter de cada producto
#Indicar para cada variable usada el tipo de dato de la variable.
#Indicar para cada variable usada el valor almacenado con el que queda al finalizar el programa.
#Definir dos condiciones que usen los datos de los productos, mostrando el resultado de combinar ambas condiciones en un operador lógico.
#Resolver el mismo ejercicio pero ahora use listas o tuplas de acuerdo a su criterio. Recordar las diferentes formas de agregar elementos en una lista.


def pregunta_inicial():
    producto_1 = input("Ingrese su producto 1: ")
    cant_producto_1 = int(input("Ingrese la cantidad de producto 1: "))
    precio_producto_1 = float(input("Ingrese el precio de producto 1: "))

    producto_2 = input("Ingrese su producto 2: ")
    cant_producto_2 = int(input("Ingrese la cantidad de producto 2: "))
    precio_producto_2 = float(input("Ingrese el precio de producto 2: "))

    producto_3 = input("Ingrese su producto 3: ")
    cant_producto_3 = int(input("Ingrese la cantidad de producto 3: "))
    precio_producto_3 = float(input("Ingrese el precio de producto 3: "))

    producto_4 = input("Ingrese su producto 4: ")
    cant_producto_4 = int(input("Ingrese la cantidad de producto 4: "))
    precio_producto_4 = float(input("Ingrese el precio de producto 4: "))

    costo = (cant_producto_1 * precio_producto_1 + cant_producto_2 * precio_producto_2 + cant_producto_3 * precio_producto_3 + cant_producto_4 * precio_producto_4)

    return costo

costo = pregunta_inicial()

print("El costo total es:", costo)


