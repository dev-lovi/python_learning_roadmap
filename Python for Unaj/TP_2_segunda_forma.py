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


# Crear listas para almacenar los datos de los productos
productos = []
cantidades = []
precios = []

# Pedir datos de 4 productos
for i in range(4):
    producto = input(f"Ingrese el nombre del producto {i + 1}: ")
    cantidad = int(input(f"Ingrese la cantidad de {producto}: "))
    precio = float(input(f"Ingrese el precio de {producto}: "))

    productos.append(producto)
    cantidades.append(cantidad)
    precios.append(precio)

# Calcular el costo total de cada producto y el costo total general
costos_producto = []
costo_total = 0

for i in range(4):
    costo_producto = cantidades[i] * precios[i]
    costos_producto.append(costo_producto)
    costo_total += costo_producto

# Imprimir los resultados
for i in range(4):
    print(f"\nEl costo total de {productos[i]} es: ${costos_producto[i]}")
    print(f"Las iniciales del producto {i + 1} son: {productos[i][0]}")
    print(f"El último carácter del producto {i + 1} es: {productos[i][-1]}")

print("\nEl costo total es: $" + str(costo_total))

# Definir dos condiciones que usen los datos de los productos
if costo_total > 10000:
    print("El costo total es mayor que $10.000")
else:
    print("El costo total no es mayor que $10.000")

# Obtener y mostrar los tipos de variables
tipo_producto = type(productos[0])
tipo_cantidad = type(cantidades[0])
tipo_precio = type(precios[0])
tipo_costo_producto = type(costos_producto[0])
tipo_costo_total = type(costo_total)

print("\nTipos de variables utilizadas:")
print(f"Tipo de variable de productos: {tipo_producto}")
print(f"Tipo de variable de cantidades: {tipo_cantidad}")
print(f"Tipo de variable de precios: {tipo_precio}")
print(f"Tipo de variable de costos_producto: {tipo_costo_producto}")
print(f"Tipo de variable de costo_total: {tipo_costo_total}")


