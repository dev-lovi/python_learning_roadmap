import random

valores = []

print("Bienvenido a mi juego")

elegir = int(input("Elija la cantidad de valores: "))

# Usa un bucle for para generar y agregar los valores a la lista
for i in range(1, elegir + 1):
    valores.append(i)

valor_correcto = random.choice(valores)
vidas = int(input("Elegí la cantidad de vidas: "))

while vidas > 0:
    rta = int(input("\nElegí un número: "))
    if rta == valor_correcto:
        print("GANASTE")
        break
    else:
        vidas -= 1
        if vidas > 0:
            print("\nVOLVE A INTENTARLO. Te quedan", vidas, "vidas.")
        else:
            print("\nPERDISTE. El número correcto era:", valor_correcto)
