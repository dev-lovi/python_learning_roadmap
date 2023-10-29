#Escriba un programa que lea nombres de personas hasta que se ingrese el nombre “zzz”. Debe imprimir la cantidad de nombres que comienzan con “A”.


nombres_a = []
nombre = 0
while nombre != "zzz":
    nombre = str(input("Ingrese su nombre, 'zzz' para salir: "))
    if nombre.lower()[0] == "a":
        nombres_a.append(nombre.capitalize())

print(nombres_a)