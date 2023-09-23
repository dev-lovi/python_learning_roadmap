#Ejercicio 5: Definir una función denominada cuantos_dias que reciba el número de mes
#como parámetro y retorne la cantidad de días que posee. Ejemplo: cuantos_dias(0),
##debería retornar 31. Ayuda: Pensar en tener una lista de la siguiente manera: [[“enero”,31],
#[“febrero”, 28], ...]

def cuantos_dias(valor):
    lista = ["Enero, 31", "Febrero, 28", "Marzo, 30"]
    print(lista[valor])

cuantos_dias(0)