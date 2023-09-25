#Ejercicio 4: Definir una función denominada imprimo_fecha que reciba tres cadenas de caracteres como parámetros formales, que representan un día, un mes y un año e imprima la fecha de la siguiente manera: “ 21 de septiembre de 2021”.
def imprimo_fecha(dia, mes, año):
    fecha = print(str(dia) + " de " + str(mes) + " de " + str(año))
    return fecha

variable_1 = input("Ingrese el día: ")
varibale_2 = input("Ingrese el mes: ")
varibale_3 = input("Ingrese el año: ")

imprimo_fecha(variable_1, varibale_2, varibale_3)


