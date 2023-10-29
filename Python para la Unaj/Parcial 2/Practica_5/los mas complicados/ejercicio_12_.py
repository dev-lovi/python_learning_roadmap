#Ejercicio 12: Dada la siguiente lista [1, 14, 56, 43, 23, 46, 58, 123, 67 ] escribir un programa que muestre el número más alto.

lista = [1, 14, 56, 43, 58, 123, 67]

#forma 1, no creo que la profe nos deje usar esto
def num_mas_alto(valor):
    valor.sort()
    x = valor[-1]  #Me da el ultimo dato de la lista ["Z", "X", "A", "ESTE"]
    print(x)
num_mas_alto(lista)


#entonces...

def num_max(valor):
    inicio = valor[0] #Empieza con el primer dato de la lista ["ESTE", "X", "A", "B"]
    for maximo in valor:
        if maximo > inicio:
            inicio = maximo
    print("El num mas grande es " + str(inicio))


num_max(lista)