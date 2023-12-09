def productos(lista):
    lista= []

    codigo= int(input("ingrese codigo o 000: "))

    while codigo != 000:
        tipo= input("ingrese tipo de producto: ")
        marca= input("ingrese marca del producto: ")
        precio= int(input("ingrese precio de producto:"))
        stock= int(input("ingrese stock: "))
        refrigeracion= input("ingrese  true si necesita refriferacion o false si no lo necesita: " )

        lista.append([codigo,tipo, marca,precio, stock, refrigeracion])

        codigo= int(input("ingrese codigo o 000: "))

    return lista

#a = productos() #invoco a la primer funcion 
#a va a ser mi parametro para reemplazar en lista mas adelante

def especifico(lista, esp):
    lista_especifico = []  #agregamos lista vacia
    
    for producto in lista:
        if producto[1] == esp: #si el producto[1] (tipo) es igual a esp
            lista_especifico.append(productos) #agregalo a la lista nueva
    
    return lista_especifico #mostrame la lista nueva con todos los productos agregados

        
#x = input("ingrese producto especifico") #x reemplazaria a esp
# = especifico(a, x)

#Listar los productos del kiosco que tienen un stock de 0.
def cero(lista):
    lista_stock = [] #siempre un nombre nuevo a la lista

    for productos in lista: 
        if productos[4]== 0:
            lista_stock.append(productos)

    return lista_stock

#c = cero(a)  #invoco a la funcion

#Mostrar los productos cuyo precio supera los 650 pesos y que requieren refrigeración.
def c(lista):
    listaaux=[]
    for l in lista:
        if l[3]<=650 and l[5]== "true":
            listaaux.append(l)
    return listaaux #este lo hiciste bien, solo cambiaria los nombres para que se entienda mejor

#d = c(a) #invoco a la funcion

#Listar el código del producto y el tipo de una marca determinada. El usuario ingresará la marca del producto.
def por_marca(lista, marca_buscada):
    productos_marca = []

    for producto in lista:
        if producto[2] == marca_buscada:
            pedido = [producto[0], producto[1]]
            productos_marca.append(pedido)
    return productos_marca
    
#f = input("Ingrese la marca del producto para listar código y tipo: ")
#e = por_marca(a, f)