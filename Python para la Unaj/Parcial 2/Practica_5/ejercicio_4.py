 #Escribir un programa que lea letras del teclado indefinidamente hasta que el usuario ingrese “fin” e imprima el código ASCII de las mismas.

dato = 0 
while dato != "fin":
    dato = input('Ingresa una letra, ingrese "fin" para salir: ')
    if len(dato) == 1:
        #codigo
        valor = ord(dato)
        print("Para la letra " + str(dato) + " el codigo ASCII es: " + str(valor))
    elif dato == "fin":
        break
    else:
        print("No seas gato, poné una sola letra porfavor")
    
