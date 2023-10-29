#Escriba un programa que reciba del usuario su nombre, apellido y patente hasta que ingrese AAA, e imprima si está exento de impuesto o no. Tener en cuenta que los autos cuyas patentes empiezan con R, S y T no deben pagar impuesto.

condicion = 0
excentos = []

while condicion != "AAA":
    print("Ingrese 'AAA' en el nombre para salir")
    nombre = str(input("Ingrese su nombre: "))
    if nombre.lower() == "aaa":
        break
    else:
        apellido = str(input("Ingrese su apellido: "))
        patente = input("Ingrese su patente: ").capitalize()
        if patente[0] == "R":
            excentos.append((nombre, apellido, patente))
        elif patente[0] == "S":
            excentos.append((nombre, apellido, patente))
        elif patente[0] == "T":
            excentos.append((nombre, apellido, patente))

print("Los excentos de pagar impuestos son " +  str(excentos))
