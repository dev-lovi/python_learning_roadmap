#Escribir un programa que muestre la tabla de los códigos ASCII. Los códigos ASCII van de 0 a 255

for valor in range (0, 256):
    print("Para el numero " + str(valor) + " el resultado es: " + str(chr(valor)))
