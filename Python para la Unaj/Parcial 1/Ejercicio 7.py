#Ejercicio 7: Definir una función que calcule el área de un círculo, otra que calcule el área de
#un rectángulo y otra que calcule el área de un cuadrado. Analice qué parámetros deberían
#recibir dichas funciones.


def area_circulo(valor):
    circulo = ((valor **2) * 3.14)
    print("El area del circulo es " + str(circulo))
area_circulo(5)

def area_rectangulo(valor1, valor2):
    rectangulo = valor1 * valor2
    print("El area del rectangulo es " + str(rectangulo))
area_rectangulo(5, 10)

def area_cuadrado(valor):
    cuadrado = valor **2
    print("El area del cuadrado es " + str(cuadrado))
area_cuadrado(5)