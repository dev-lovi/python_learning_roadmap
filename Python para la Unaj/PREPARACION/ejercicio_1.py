'''

Realice un programa para administrar un kiosco en Florencio Varela. 
Se dispone de información sobre los productos en venta, incluyendo código (ingrese 000 para salir), tipo (galletas, bebidas, golosinas), marca, precio, stock y refrigeración (True/False).


Funciones
1. Mostrar la lista de productos con sus respectivos precios de un tipo específico. El usuario ingresará el tipo del producto.
2. Listar los productos del kiosco que tienen un stock de 0.
3. Mostrar los productos cuyo precio supera los 650 pesos y que requieren refrigeración.
4. Listar el código del producto y el tipo de una marca determinada. El usuario ingresará la marca del producto.

    [100, "galletas", "jorgito", 200, 15, False],
    [102, "bebidas", "cocacola", 500, 20, True],

'''

def agregar():
    lista = []

    codigo = int(input("Ingrese el codigo, '000' para salir: "))

    while codigo != 000:
        tipo = input("Ingrese el tipo (galletitas, bebidas, golosinas): ").lower()
        marca = input("Ingrese la marca: ").lower()
        precio = int(input("Ingrese el precio: "))
        stock = int(input("Ingrese el stock: "))
        refrigeracion = input("Refrigeración True/False: ").lower()

        total = [codigo, tipo, marca, precio, stock, refrigeracion]
        lista.append(total)

        codigo = int(input("Ingrese el codigo, '000' para salir: "))

    return lista

a = agregar()
#print(a)


def buscar_tipo(lista, pregunta_tipo):
    lista_tipo = []

    for productos in lista:
        if productos[1] == pregunta_tipo:
            lista_tipo.append(productos)
    return lista_tipo

x = input("Ingrese el tipo (galletitas, bebidas, golosinas): ")
b = buscar_tipo(a, x)
print(b)



def stock_cero(lista):
    lista_stock = []

    for productos in lista:
        if productos[4] == 0:
            lista_stock.append(productos)

    return lista_stock


#c = stock_cero(a)
#print(c)

def mostrar_productos_precio_y_refri(lista):
    lista_precio_refri = []

    for productos in lista:
        if productos[3] >= 650 and productos[5] == 'true':
            lista_precio_refri.append(productos)

    return lista_precio_refri

#d = mostrar_productos_precio_y_refri(a)
#print(d)

def def_codigo_y_marca(lista, marca):
    lista_codigo_y_marca = []

    for productos in lista:
        if productos[2] == marca:
            pedido = [productos[0], productos[1]]
            lista_codigo_y_marca.append(pedido)

    return lista_codigo_y_marca

#x = input("Ingrese la marca: ").lower()
#e = def_codigo_y_marca(a, x)
#print(e)


a = agregar()

condicion = 'a'

while condicion == 'a':
    print("Menu de opciones")
    print("1. Mostrar la lista de productos con sus respectivos precios de un tipo específico.")
    print("2. Listar los productos del kiosco que tienen un stock de 0.")
    print("3. Mostrar los productos cuyo precio supera los 650 pesos y que requieren refrigeración.")
    print("4. Listar el código del producto y el tipo de una marca determinada.")
    print("5. Salir")

    pregunta = int(input("Ingrese una opción: "))

    if pregunta == 5:
        condicion = 'b'

    elif pregunta == 1:
        x = input("Ingrese el tipo (galletitas, bebidas, golosinas): ")
        b = buscar_tipo(a, x)
        print(b)


    elif pregunta == 2:
        c = stock_cero(a)
        print(c)

    elif pregunta == 3:
        d = mostrar_productos_precio_y_refri(a)
        print(d)

    elif pregunta == 4:
        x = input("Ingrese la marca: ").lower()
        e = def_codigo_y_marca(a, x)
        print(e)