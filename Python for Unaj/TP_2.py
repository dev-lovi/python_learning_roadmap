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


    costo_producto_1 = cant_producto_1 * precio_producto_1
    costo_producto_2 = cant_producto_2 * precio_producto_2
    costo_producto_3 = cant_producto_3 * precio_producto_3
    costo_producto_4 = cant_producto_4 * precio_producto_4

    costo_total = (cant_producto_1 * precio_producto_1 + cant_producto_2 * precio_producto_2 + cant_producto_3 * precio_producto_3 + cant_producto_4 * precio_producto_4)

    return (
        producto_1,
        producto_2,
        producto_3,
        producto_4,
        precio_producto_1,
        cant_producto_1,
        cant_producto_2,
        cant_producto_3,
        cant_producto_4,
        costo_producto_1,
        costo_producto_2,
        costo_producto_3,
        costo_producto_4,
        costo_total,
    )

(
    producto_1,
    producto_2,
    producto_3,
    producto_4,
    precio_producto_1,
    cant_producto_1,
    cant_producto_2,
    cant_producto_3,
    cant_producto_4,
    costo_producto_1,
    costo_producto_2,
    costo_producto_3,
    costo_producto_4,
    costo_total,
) = pregunta_inicial()



# Imprimir las iniciales y el último carácter de cada producto
iniciales_producto_1 = producto_1[0]
ultimo_caracter_producto_1 = producto_1[-1]

iniciales_producto_2 = producto_2[0]
ultimo_caracter_producto_2 = producto_2[-1]

iniciales_producto_3 = producto_3[0]
ultimo_caracter_producto_3 = producto_3[-1]

iniciales_producto_4 = producto_4[0]
ultimo_caracter_producto_4 = producto_4[-1]

# Obtener el tipo de variable de algunas variables
tipo_producto_1 = type(producto_1)
tipo_cant_producto_1 = type(cant_producto_1)
tipo_precio_producto_1 = type(precio_producto_1)
tipo_costo_producto_1 = type(costo_producto_1)
tipo_costo_total = type(costo_total)


#Imprimir por cada producto un mensaje que muestre los datos, por ejemplo con dos   productos, el resultado seria:
print("\nEl costo total de " + str(producto_1) + " $" + str(costo_producto_1))
print("Las iniciales del producto 1 son:", iniciales_producto_1)
print("El último carácter del producto 1 es:", ultimo_caracter_producto_1)

print("\nEl costo total de " + str(producto_2) + " $" + str(costo_producto_2))
print("Las iniciales del producto 1 son:", iniciales_producto_2)
print("El último carácter del producto 1 es:", ultimo_caracter_producto_2)

print("\nEl costo total de " + str(producto_3) + " $" + str(costo_producto_3))
print("Las iniciales del producto 1 son:", iniciales_producto_3)
print("El último carácter del producto 1 es:", ultimo_caracter_producto_3)

print("\nEl costo total de " + str(producto_4) + " $" + str(costo_producto_4))
print("Las iniciales del producto 1 son:", iniciales_producto_4)
print("El último carácter del producto 1 es:", ultimo_caracter_producto_4)
print("\nEl costo total es:"+ " $" + str(costo_total))
#Definir dos condiciones que usen los datos de los productos, mostrando el resultado de combinar ambas condiciones en un operador lógico.
if costo_total > 10000:
    print("El costo total es mayor que $10.000")
else:
    print("El costo total es mayor que $10.000")

print("\nTipos de variables utilizadas, ejemplo con el primer producto")
print("Tipo de variable de producto_1:", tipo_producto_1)
print("Tipo de variable de cant_producto_1:", tipo_cant_producto_1)
print("Tipo de variable de precio_producto_1:", tipo_precio_producto_1)
print("Tipo de variable de costo_producto_1:", tipo_costo_producto_1)
print("Tipo de variable de costo_total:", tipo_costo_total)

