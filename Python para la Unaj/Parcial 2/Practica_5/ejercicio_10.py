#Definir una función que imprima los primeros cien números enteros.
def enteros():
    for a in range(0, 101):
        print(a)
enteros()

#Definir una función que imprima los primeros cien números pares.
def es_par():
    for a in range(0, 101):
        if a % 2 == 0:
            print(str(a) + " es par")
es_par()

#Definir una función que imprima los primeros cien números inpares.
def es_inpar():
    for a in range(0, 101):
        if a % 2 != 0:
            print(str(a) + " es inpar")
es_inpar()

