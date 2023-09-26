#Crear una funcion que calcule el perimetro de un triangulo
def calculo_perimetro(valor_1, valor_2, valor_3):
    calculo = (valor_1 + valor_2 + valor_3)
    return calculo
lado_1 = int(input("Ingrese el valor del lado 1: "))
lado_2 = int(input("Ingrese el valor del lado 2: "))
lado_3 = int(input("Ingrese el valor del lado 3: "))
x = calculo_perimetro(lado_1,  lado_2, lado_3)
print("El valor del perimetro del triangulo es" + " " + str(x))