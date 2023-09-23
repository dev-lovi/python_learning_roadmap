#Ejercicio 14: Definir tres funciones llamadas convertir_a_dolar, convertir_a_euro y convertir_a_real. Cada función recibe un parámetro que representa un monto en pesos y devuelve su conversión respectiva.

def convetir_a_dolar(peso):
    valor_peso = peso / 740
    print("La cantidad de dolares es " + str(valor_peso))
convetir_a_dolar(1000)

def convertir_a_euro(peso):
    valor_peso = peso / 812
    print("La cantidad de euros es " + str(valor_peso))
convertir_a_euro(1000)

def convertir_a_real(peso):
    valor_peso = peso / 134
    print("La cantidad de reales es " + str(valor_peso))
convertir_a_real(1000)