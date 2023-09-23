#Ejercicio 13: Definir una función llamada a_pagar que reciba 4 números: la cantidad de personas, el monto gastado en bebida, el monto gastado en comida y el del alquiler del lugar, y retorne cuánto le toca pagar a cada uno.


def llamada_a_pagar(cant_personas, gasto_bebida, gasto_comida, alquiler): #no se hagan los ratas jaj
    suma = gasto_bebida + gasto_comida + alquiler
    calculo = suma / cant_personas
    print("A cada uno le toca pagar " + str(calculo))
llamada_a_pagar(5, 3000, 9000, 1500)
