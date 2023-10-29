#Escribir un programa que calcule el promedio de N números ingresados por el usuario. (AYUDA: al comenzar el programa debe preguntar la cantidad de números a ingresar, luego iterar y leer tantos números del teclado como se indicó al inicio.)



n = int((input("Ingrese la cantidad de numeros a promediar: ")))
suma = 0

if n > 0:
    for valor in range(1, n + 1):
        pregunta = int(input("Ingresa el valor del numero "+ str(valor) + ": ")) 
        suma += pregunta
    promedio = suma / n
    print(promedio)
else:
    print("No se puede dividir por cero.")




    