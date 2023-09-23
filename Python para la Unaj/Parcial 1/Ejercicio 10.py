#Ejercicio 10: Definir una función llamada calculo_transporte que reciba cuatro números: la cantidad de alumnos de 1era, 2da y 3er. salita de un jardín de infantes y la cantidad de asientos del transporte escolar. La función debe retornar cuántos micros necesito contratar para una excursión sabiendo que cada salita es acompañada por tres adultos.

def calculo_transporte(valor1, valor2, valor3, valor4):
    cant_alumnos = (valor1 + valor2 + valor3 + 9)
    calculo = cant_alumnos / valor4
    print("Se necesitaran " + str(round(calculo)) + " micros.") #round se usa para redondear
calculo_transporte(20, 22, 25, 20)
