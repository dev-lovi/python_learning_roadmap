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


def cargar_datos():
    lista = []

    codigo = int(input("Ingrese el codigo, ponga '000' para salir: "))

    while codigo != 000:
        tipo = input("Ingrese el tipo (galletas, bebidas, golosinas): ")
        marca = input("Ingrese la marca: ")
        precio = int(input("Ingrese el precio: "))
        stock = int(input("Ingrese el stock: "))
        refrigeracion = input("Refrigeracion True/False: ").lower() 

        total = [codigo, tipo, marca, precio, stock, refrigeracion]
        lista.append(total)

        codigo = int(input("Ingrese el codigo, ponga '000' para salir: "))

    return lista

#a = cargar_datos()
#print(a)


def buscar_tipo(lista, tipo_usuario):
    lista_tipo = []

    for productos in lista:
        if productos[1] == tipo_usuario:
            lista_tipo.append(productos)

    return lista_tipo


#input_tipo_usuario = input("Ingrese el tipo (galletas, bebidas, golosinas): ")
#b = buscar_tipo(a, input_tipo_usuario )
#print(b)




def stock_cero(lista):
    lista_stock = []

    for productos in lista:
        if productos[4] == 0:
            lista_stock.append(productos)

    return lista_stock

#c = stock_cero(a)
#print(c)


def precio_true(lista):
    lista_precio_true = []

    for productos in lista:
        if productos[3] > 650 and productos[5] == 'true':
            lista_precio_true.append(productos)

    return lista_precio_true

#d = precio_true(a)
#print(d)


def buscar_marca(lista, input_marca):
    lista_marca = []

    for productos in lista:
        if productos[2] == input_marca:
            total = [productos[0], productos[1]]
            lista_marca.append(total)

    return lista_marca

#x = input("Ingrese la marca: ")
#e = buscar_marca(a, x)
#print(e)



a = cargar_datos()

print("Programa para administrar un kiosco en Florencio Varela")
print("Menu de opciones")
print("1. Mostrar la lista de productos por tipo.")
print("2. Listar los productos del kiosco que tienen un stock de 0.")
print("3. Precio supera los 650 pesos y que requieren refrigeración.")
print("4. Listar el código del producto y el tipo de una marca determinada.")
print("5. Salir")

pregunta = int(input("Elija una opcion: "))

while pregunta != 5:

    if pregunta == 1:
        input_tipo_usuario = input("Ingrese el tipo (galletas, bebidas, golosinas): ")
        b = buscar_tipo(a, input_tipo_usuario )
        print(b)

    elif pregunta == 2:
        c = stock_cero(a)
        print(c)

    elif pregunta == 3:
        d = precio_true(a)
        print(d)

    elif pregunta == 4:
        x = input("Ingrese la marca: ")
        e = buscar_marca(a, x)
        print(e)

    else:
        print("Opcion incorrecta")
    
    pregunta = int(input("Elija una opcion: "))
    