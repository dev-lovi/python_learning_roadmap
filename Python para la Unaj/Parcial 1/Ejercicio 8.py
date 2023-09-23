#Definir una función llamada calculo_rebaja que reciba dos números, uno con
#el precio anterior y otro para el precio rebajado y devuelva un número que represente el
#porcentaje rebajado.

def calculo_rebaja(valor1, valor2):
    porcentaje_rebajado = (valor2 * 100) / valor1
    print("El porcentaje rebajado es de " + str(porcentaje_rebajado) + " %.")
calculo_rebaja(240, 180)