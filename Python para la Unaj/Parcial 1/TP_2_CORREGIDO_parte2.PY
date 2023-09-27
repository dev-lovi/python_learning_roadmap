#Resolver el mismo ejercicio pero ahora use listas o tuplas de acuerdo a su criterio. Recordar las diferentes formas de agregar elementos en una lista.

nombre = []
cantidad = []
precio = []
inicial = []
ultima = []

pregunta_inicial = int(input("¿Cuantos productos deseas agregar a la lista?: "))
for x in range(pregunta_inicial):
    pregunta_producto = input("Ingrese el nombre del producto: ")
    pregunta_cantidad = int(input("Ingrese la cantidad de " + str(pregunta_producto) + ": "))
    pregunta_precio = float(input("Ingrese el precio de " + str(pregunta_producto) + ": "))

    nombre.append(pregunta_producto)
    cantidad.append(pregunta_cantidad)
    precio.append(pregunta_precio)
    inicial.append(pregunta_producto[0])
    ultima.append(pregunta_producto[-1])

total = 0
for y in range(pregunta_inicial):
    total += cantidad[y] * precio[y]

if len(nombre) >1:
    print("\nProductos comprados:")
else:
    print("\nLista producto:")
if len(nombre) > 1:
    print("El nombre de los productos son: " + str(nombre) + ". El precio es: $" + str(precio) + ". El total gastado es: $" + str(total))
else:
    print("El nombre del producto es: " + str(nombre) + ". El precio es: $" + str(precio) + ". El total gastado es: $" + str(total))
if len(nombre) > 1:
    print("Las iniciales son " + str(inicial) + " y las ultimas letras son " + str(ultima))
else:
    print("La inicial es " + str(inicial) + " y la ultima letra es " + str(ultima))
print("\nLos tipos de variables son: ")
print("Nombre: " + str(type(nombre)))
print("Cantidad: " + str(type(cantidad)))
print("Precio: " + str(type(precio)))
print("Total: " + str(type(total)))

