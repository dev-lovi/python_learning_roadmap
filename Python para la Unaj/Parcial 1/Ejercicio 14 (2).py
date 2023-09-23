#Ejercicio 14: Definir tres funciones llamadas convertir_a_dolar, convertir_a_euro y convertir_a_real. Cada función recibe un parámetro que representa un monto en pesos y devuelve su conversión respectiva.

#OTRA FORMA DE HACERLO 

def convertir_a_dolar():
    cantidad = int(input("Ingrese la cantidad de pesos (ARS): "))
    valor_peso = cantidad / 740
    print("La cantidad de dolares es " + str(valor_peso))

def convertir_a_euro():
    cantidad = int(input("Ingrese la cantidad de pesos (ARS): "))
    valor_peso = cantidad / 812
    print("La cantidad de euroes es " + str(valor_peso))

def convertir_a_real():
    cantidad = int(input("Ingrese la cantidad de pesos (ARS): "))
    valor_peso = cantidad / 134
    print("La cantidad de reales es " + str(valor_peso))

a = 0
while a == 0:
    print("1. Pesos ars a dolar")
    print("2. Pesos ars a euro")
    print("3. Pesos ars a real")
    menu = int(input("Elija una opción: "))
    if menu == 1:
        convertir_a_dolar()
    elif menu == 2:
        convertir_a_euro()
    elif menu == 3:
        convertir_a_real()
    else:
        print("Error")

