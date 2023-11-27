
x = []


def agregar_arboles(lista):

    condicion = 0
    print("Bienvenido adsfasdf")

    while condicion < 3:
        nombre = input("Ingrese el nombre: ")
        inventario = int(input("Ingrese el n inventario: "))
        edad = int(input("Ingrese la edad: "))
        tipo = input("Ingrese el tipo: ").upper()
        altura = int(input("Ingrese la altura: "))


        total = [nombre, inventario, edad, tipo, altura]


        lista.append(total)
        condicion += 1

agregar_arboles(x)


def viejos_altura(lista):
    lista_viejos_altura = []

    for arboles in lista:
        if arboles[2] > 10 and arboles[4] > 40:
            lista_viejos_altura.append(arboles[0])

    a = len(lista_viejos_altura)
    print("El total de arboles con la condicion ... es: " + str(a))

#viejos_altura(x)




def inventario_nashe(lista, pregunta):
    lista_inventario = []

    for arboles in lista:
        if arboles[1] == pregunta:
            lista_inventario.append(arboles)

    print(lista_inventario)

#pregunta = int(input("¿Que numero de inventario?: "))
#inventario_nashe(x, pregunta)


def altura_arbol(lista):
    lista_altura_arbol = []
    altura = 0

    for arboles in lista:
        if arboles[2] > 5 and arboles[3] == 'PINO':
            altura += arboles[4]
            lista_altura_arbol.append(arboles)
    

    cantidad = len(lista_altura_arbol)
    calculo = altura / cantidad
    print("El promedio es" + str(calculo))

altura_arbol(x)


