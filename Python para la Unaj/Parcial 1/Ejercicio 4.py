#Ejercicio 4: Definir una función denominada imprimo_fecha que reciba tres cadenas de caracteres como parámetros formales, que representan un día, un mes y un año e imprima la fecha de la siguiente manera: “ 21 de septiembre de 2021”.
def imprimo_fecha(dia, mes, año):
    fecha = print(str(dia) + " de " + str(mes) + " de " + str(año))
    return fecha
imprimo_fecha(21, "septiembre", 2021)

def imprimo_fecha_segunda_forma():
    fecha2 = print("21 de septiembre de 2021")
    return fecha2
imprimo_fecha_segunda_forma()