#Ejercicio 12: Definir una función llamada calculo_litros que reciba tres números, el alto,
#ancho y profundidad (en metros) de una pileta y devuelva la cantidad de litros que tiene.

def calculo_litros(alto, ancho, profundidad):
    calculo = alto * ancho * profundidad
    print("La cantidad de litros es " + str(calculo))
calculo_litros(20, 40, 50)

#forma 2
def calculo_litros():
    alto = int(input("Ingrese el alto: "))
    ancho = int(input("Ingrese el ancho: "))
    profundidad = int(input("Ingrese la profundidad: "))
    calculo = alto * ancho * profundidad
    print("La cantidad de litros es " + str(calculo))
calculo_litros()