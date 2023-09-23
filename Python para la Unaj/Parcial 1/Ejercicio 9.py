#Ejercicio 9: Definir una función llamada calculo_nuevo_precio que reciba dos números, uno con el precio anterior y otro con el número de porcentaje a aumentar y devuelva el precio aumentado.


def calculo_nuevo_precio(valor1, valor2):
    porcentaje = (valor2 * 100) / valor1
    precio = porcentaje + valor1
    print("El precio aumentado es de " + str(precio))
calculo_nuevo_precio(200, 25)