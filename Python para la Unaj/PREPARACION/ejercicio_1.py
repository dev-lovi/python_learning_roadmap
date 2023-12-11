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

a = cargar_datos()
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



#AGREGAMOS 3 FUNCIONES MÁS

#FUNCION 5
#PROMEDIO DE PRECIO (el usuario ingresa el tipo (galletitas, bebidas, etc))

def promedio_tipo(lista, tipo_usuario):
    cantidad = 0
    precio = 0

    for productos in lista:
        if productos[1] == tipo_usuario:
            cantidad += 1
            precio += productos[3]
    
    promedio = precio / cantidad
    return promedio


#x = input("Ingrese el tipo (galletas, bebidas, golosinas): ")
#f = promedio_tipo(a, x)
#print(f)

            
    

#FUNCION 6
#EL PRODUCTO MAS CARO DE TOOODO MI CATALOGO
 
def el_mas_caro(lista):

    precio_inicial = 0
    producto_caro = "a"

    for productos in lista:
        if productos[3] > precio_inicial:
            precio_inicial = productos[3]
            producto_caro = productos

    return producto_caro


#g = el_mas_caro(a)
#print(g)


#FUNCION 7
#BUSCAR POR LETRA DE MARCA

def buscar_letra(lista, input_usuario):

    lista_letra = []

    for productos in lista:
        if productos[2][0] == input_usuario:
            lista_letra.append(productos)

    return lista_letra

#x = input("Ingresa una letra: ")
#h = buscar_letra(a, x)
#print(h)





a = cargar_datos()

print("Programa para administrar un kiosco en Florencio Varela")
print("Menu de opciones")
print("1. Mostrar la lista de productos por tipo.")
print("2. Listar los productos del kiosco que tienen un stock de 0.")
print("3. Precio supera los 650 pesos y que requieren refrigeración.")
print("4. Listar el código del producto y el tipo de una marca determinada.")
print("5. PROMEDIO DE PRECIO (el usuario ingresa el tipo (galletitas, bebidas, etc)).")
print("6. EL PRODUCTO MAS CARO DE TOOODO MI CATALOGO.")
print("7. BUSCAR POR LETRA DE MARCA.")
print("8. Salir")

pregunta = int(input("Elija una opcion: "))

while pregunta != 8:

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

    elif pregunta == 5:
        x = input("Ingrese el tipo (galletas, bebidas, golosinas): ")
        f = promedio_tipo(a, x)
        print(f)


    elif pregunta == 6:
        print("funcion 6")

    elif pregunta == 7:
        print("funcion 7")

    else:
        print("Opcion incorrecta")
    
    pregunta = int(input("Elija una opcion: "))
    


