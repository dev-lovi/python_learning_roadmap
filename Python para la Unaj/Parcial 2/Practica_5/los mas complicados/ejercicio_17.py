#Ejercicio 17:
#a) Definir una función que permita el ingreso de números por teclado hasta ingresar el 0, y retorne esa lista.
def num_list(x):
    while True:
        pregunta = int(input("Ingresa un numero, pone 0 para salir: "))
        if pregunta == 0:
            break
        x.append(pregunta)
    return x
#lista = []
#a = num_list(lista)
#print(a)

#b) Definir una función que reciba como parámetro una lista de números y retorne como resultado el promedio.
def calc_promedio(x):
    n = len(x)
    suma = 0
    for cant in x:
        suma += cant        
    promedio = suma / n
    return promedio

#lista_2 = [20, 30, 50, 40, 30]
#a = calc_promedio(lista_2)
#print(a)

#c) Definir una función que reciba como parámetro una lista de números y retorne como resultado la suma de los números.
def calc_suma(x):
    suma = 0
    for cant in x:
        suma += cant
    return suma

#lista_3 = [20, 30, 50, 40, 30]
#a = calc_suma(lista_3)
#print(a)

#d) Definir una función que reciba como parámetro una lista de números y retorne el número más grande de la lista (máximo).
def calc_grande(x):
    inicio = x[0]

    for max in x:
        if max > inicio:
            inicio = max
    return ("El  mas grande es " + str(inicio))

#lista_4 = [20, 30, 50, 40, 30]
#a = calc_grande(lista_4)
#print(a)

#0e) Definir una función que reciba como parámetro una lista de números y retorne el número más pequeño de la lista (mínimo).
def calc_min(x):
    inicio = x[0]

    for min in x:
        if min < inicio:
            inicio = min
    return ("El  mas chico es " + str(inicio))

#lista_5 = [20, 30, 50, 40, 30]
#a = calc_min(lista_5)
#print(a)


#f) Definir una función denominada porcentaje, que tenga 2 parámetros formales, que representan el total y un valor y retorna el porcentaje de ese valor respecto del total.

def porcentaje(x, y):
    calculo = (x * 100) / y
    return calculo 

#a = 50 #valor
#b = 200 #total
#z = porcentaje(a, b)
#print(z)


while True:

    print("Menu")
    print("1. Ver el promedio de los números")
    print("2. Ver la suma de los números")
    print("3. Ver la cantidad de números")
    print("4. Ver el número máximo")
    print("5. Ver el número mínimo")
    print("6. Calcular porcentaje")
    print("7. Salir")
    h = int(input("Elegi una opcion: "))

    lista = [20, 30, 50, 60]
    
    if h == 7:
        break
    elif h == 1:
        a = calc_promedio(lista)
        print(a)
    elif h == 2:
        a = calc_suma(lista)
        print(a)
    elif h == 3:
        a = len(lista)
        print(a)
    elif h == 4:
        a = calc_grande(lista)
        print(a)
    elif h == 5:
        a = calc_min(lista)
        print(a)
    elif h == 6:
        a = calc_promedio(lista)
        b = len(lista)
        z = porcentaje(a, b)
        print(z)


    
    
    
    
    
    