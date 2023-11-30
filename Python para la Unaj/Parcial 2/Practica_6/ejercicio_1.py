#1) Defina una función que reciba como argumento una cadena de texto y retorne un valor entero indicando la cantidad de vocales que contiene la cadena Ejemplo: “agua” -> 3, “pepe” ->2

def mi_funcion(x):
    cantidad_de_vocales = 0
    for datos in x:
        if datos in "aeiouAEIOU":
            cantidad_de_vocales += 1
    return cantidad_de_vocales


#b) Defina una función que genere una lista de palabras hasta que se ingrese la
#palabra “fin” la cual NO debe ser almacenada en la lista, por cada palabra,
#también se guardara la cantidad de vocales que contiene la misma, para esto
#deberá utilizar la función definida en el punto 1) a, al finalizar la función deberá
#retornar la lista generada.


def punto_b(valor):
    pregunta = input("Ingrese una palabra, 'fin' para salir: ")


    while pregunta != "fin":
        a = mi_funcion(pregunta)
        lista.append((str(pregunta) , (a)))
        pregunta = input("Ingrese una palabra, 'fin' para salir: ")

    return valor
    
#lista = []
#a = punto_b(lista)

#print(a)

#defina una función que reciba como argumento la lista generada en el punto 1.b e imprimir las palabras que tienen mas de 3 vocales.

def vocales(valor):
    lista_vocales = []

    for elemento in valor:
        nombre = elemento[0]
        vocal = elemento[1]

        if vocal > 3:
            lista_vocales.append(nombre)
            
    return lista_vocales


#f = vocales(a)
#print(f)


condicion = 0
print("Menu")
print("1. Funcion 1")
print("2. Funcion 2")
print("3. Funcion 3")
print("4. Salir")

while condicion != 4:
    pregunta = int(input("Elija una opcion: "))
    if pregunta == 4:
        condicion = 4 #deja de cumplir la condicion, se sale
    elif pregunta == 1:
        #invocacion funcion 1
        print("hola")
    elif pregunta == 2:
        print("hola")
        #invocacion funcion 1
    elif pregunta == 3:
        print("hola")
        #invocacion funcion 1

