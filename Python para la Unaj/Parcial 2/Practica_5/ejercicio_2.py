#Ejercicio 2: Escribir un programa que calcule la sumatoria desde 0 hasta m, donde m es un número introducido por la persona usuaria desde el teclado.

m = int(input("Ingresa un valor: "))
suma = 0
for valor in range(0, m + 1):
    suma += valor
    print(suma)