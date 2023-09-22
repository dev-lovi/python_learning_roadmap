#EJERCICIOS A ENTREGAR TP N° 2

#Pedir datos de 4 productos comprados, con su cantidad(entero) y precio unitario(decimal).
#Mostrar cuánto se gasta por cada producto y el total gastado
#Imprimir por cada producto un mensaje que muestre los datos, por ejemplo con dos   productos, el resultado seria:

#Productos comprados:
#Nombre: nombre_producto1 Precio: precio_producto1
#Nombre: nombre_producto2 Precio: precio_producto2
#******************************Total gastado: total

#Imprimir las iniciales de cada producto - LISTO
#Imprimir el ultimo caracter de cada producto - LISTO
#Indicar para cada variable usada el tipo de dato de la variable.
#Indicar para cada variable usada el valor almacenado con el que queda al finalizar el programa.
#Definir dos condiciones que usen los datos de los productos, mostrando el resultado de combinar ambas condiciones en un operador lógico.
#Resolver el mismo ejercicio pero ahora use listas o tuplas de acuerdo a su criterio. Recordar las diferentes formas de agregar elementos en una lista.


def pregunta_inicial(numero_producto):
    producto = input(f"\nIngrese su producto {numero_producto}: ")
    cantidad = int(input(f"Ingrese la cantidad de {producto}: "))
    precio = float(input(f"Ingrese el precio de {producto}: "))
    costo = cantidad * precio
    return producto, cantidad, precio, costo

costo_total = 0

for i in range(1, 5):
    producto, cantidad, precio, costo = pregunta_inicial(i)
    costo_total += costo

    iniciales = producto[0]
    ultimo_caracter = producto[-1]
    tipo_producto = type(producto)
    tipo_cantidad = type(cantidad)
    tipo_precio = type(precio)
    tipo_costo = type(costo)

    print(f"\nEl costo total de {producto} es: ${costo}")
    print(f"Las iniciales del producto {i} son: {iniciales}")
    print(f"El último carácter del producto {i} es: {ultimo_caracter}")

print("\nEl costo total es: $" + str(costo_total))

#Definir dos condiciones que usen los datos de los productos, mostrando el resultado de combinar ambas condiciones en un operador lógico.
if costo_total > 10000:
    print("El costo total es mayor que $10.000")
else:
    print("El costo total es mayor que $10.000")

print("\nTipos de variables utilizadas, ejemplo con el primer producto")
print("Tipo de variable de producto:", tipo_producto)
print("Tipo de variable de cantidad:", tipo_cantidad)
print("Tipo de variable de precio:", tipo_precio)
print("Tipo de variable de costo:", tipo_costo)
print("Tipo de variable de costo_total:", tipo_costo)

