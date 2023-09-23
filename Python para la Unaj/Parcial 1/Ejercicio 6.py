#Ejercicio 6: Definir una función que reciba un número como parámetro y mostrar la tabla de
#multiplicar de dicho número.


def multiplicar_tabla(valor):
    for a in range(1, 101):
        resultado = valor * a
        print(resultado)
    
multiplicar_tabla(2)
print("Se imprimen los valores en un rango de 1 a 100 del numero seleccionado")