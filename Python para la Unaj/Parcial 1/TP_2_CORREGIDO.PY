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
    inicial = nombre[0]
    ultima = nombre[-1]
    print("Productos comprados:")
    print("El nombre del producto es: " + str(nombre) + ". El precio es: $" + str(precio) + ". El total gastado es: $" + str(total))
    print("La inicial es " + str(inicial) + " y la ultima letra es " + str(ultima))
    print("\nLos tipos de variables son: ")
    print("Nombre: " + str(type(nombre)))
    print("Cantidad: " + str(type(cantidad)))
    print("Precio: " + str(type(precio)))
    print("Total: " + str(type(total)))
    if total >= 5000:
        print("El total supera los $5.000 pesos.")
    else:
        print("El total es menor que $5.000 pesos.")


pregunta_nombre = input("\nIngrese el nombre del producto: ")
pregunta_cantidad = int(input("Ingrese la cantidad: "))
pregunta_precio = float(input("Ingrese el precio: "))
calculo_producto(pregunta_nombre, pregunta_cantidad, pregunta_precio)

pregunta_nombre_2 = input("\nIngrese el nombre del producto: ")
pregunta_cantidad_2 = int(input("Ingrese la cantidad: "))
pregunta_precio_2 = float(input("Ingrese el precio: "))
calculo_producto(pregunta_nombre_2, pregunta_cantidad_2, pregunta_precio_2)

pregunta_nombre_3 = input("\nIngrese el nombre del producto: ")
pregunta_cantidad_3 = int(input("Ingrese la cantidad: "))
pregunta_precio_3 = float(input("Ingrese el precio: "))
calculo_producto(pregunta_nombre_3, pregunta_cantidad_3, pregunta_precio_3)

pregunta_nombre_4 = input("\nIngrese el nombre del producto: ")
pregunta_cantidad_4 = int(input("Ingrese la cantidad: "))
pregunta_precio_4 = float(input("Ingrese el precio: "))
calculo_producto(pregunta_nombre_4, pregunta_cantidad_4, pregunta_precio_4)


#Resolver el mismo ejercicio pero ahora use listas o tuplas de acuerdo a su criterio. Recordar las diferentes formas de agregar elementos en una lista.
