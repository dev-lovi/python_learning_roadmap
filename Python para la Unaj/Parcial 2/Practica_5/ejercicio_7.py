#Escriba un programa que lea números de documentos de identidad de personas hasta que se ingrese el número “999”. Debe imprimir la cantidad de números de documentos menores que 20.000.000.


documentos = []
dni = 0

while dni != 999:
    dni = int(input("Ingrese su documento, 999 para salir: "))
    if dni == 999:
        break
    elif dni <= 20000000:
        documentos.append(dni)


print("La cantidad de documentos menores que 20.000.000 son " + '"' + str(len(documentos)) + '"' + " y los documentos son: " + str(documentos))