#EJERCICIOS A ENTREGAR TP N° 2

#Pedir datos de 4 productos comprados, con su cantidad(entero) y precio unitario(decimal).Mostrar cuánto se gasta por cada producto y el total gastado. Imprimir por cada producto un mensaje que muestre los datos, por ejemplo con dos   productos, el resultado seria:

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

def calculo_producto(nombre, cantidad, precio):
    total = cantidad * precio
    respuesta = print("Nombre: " + str(nombre) + " Precio: " + str(precio) + " Total gastado: " + str(total))
    return respuesta


pregunta_nombre = input("Ingrese el nombre del producto: ")
pregunta_cantidad = int(input("Ingrese la cantidad: "))
pregunta_precio = float(input("Ingrese el precio: "))
calculo_producto(pregunta_nombre, pregunta_cantidad, pregunta_precio)


