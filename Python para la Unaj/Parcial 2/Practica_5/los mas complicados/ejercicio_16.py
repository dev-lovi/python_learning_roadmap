#Ejercicio 16: Escriba un programa que le solicite al usuario que ingrese un monto de dinero y una opción del siguiente menú que debe mostrarse permanentemente hasta que se ingrese la opción D:
#A: convertir_a_dolar
#B: convertir_a_euro
#C: convertir_a_real
#D: salir

def dolar(peso):
    dolar = 990
    calculo = peso/dolar
    print("El valor en dolares es " + str(calculo))

def euro(peso):
    euro = 1043
    calculo = peso/euro
    print("El valor en euros es " + str(calculo))

def real(peso):
    real = 70
    calculo = peso/real
    print("El valor reales es " + str(calculo))


while True:
    print("\nMenu de opciones papá")
    print("1. Convertir a dolar")
    print("2. Convertir a euro")
    print("3, Convertir a real")
    print("4. Salir")

    pregunta = int(input("Elegí una opción: "))

    if pregunta == 1:
        x = int(input("Ingrese la cantidad de pesos: "))
        dolar(x)
    elif pregunta == 2:
        x = int(input("Ingrese la cantidad de pesos: "))
        euro(x)
    elif pregunta == 3:
        x = int(input("Ingrese la cantidad de pesos: "))        
        real(x)
    elif pregunta == 4:
        break

