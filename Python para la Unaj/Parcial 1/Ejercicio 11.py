#Ejercicio 11: Definir una función llamada armo_cartel que reciba una cadena de caracteres
#(para el nombre del producto) y dos números (el precio anterior y el otro para el precio
#rebajado) e imprima un cartel de la siguiente forma:

#Atención!!! Gran rebaja para el producto nombre (recibido como parámetro)
#Antes: precio anterior (dato recibido como parámetro)
#Ahora: precio rebajado (dato recibido como parámetro)


def armo_cartel(valor1, valor2, valor3):
    print("Atención!!! Gran rebaja para el producto " + str(valor1))
    print("Antes: precio anterior $" + str(valor2))
    print("Ahora: precio rebajado $" + str(valor3))
armo_cartel("Gol Trend al piso", 3000000, 2870000)