import random

valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

valor_correcto = random.choice(valores)

puntaje = 0

print("¡Bienvenido!")
while puntaje < 5:
    pregunta = int(input("Elegí un número del 1 al 10: "))
    if pregunta == valor_correcto:
        print("¡Ganaste!")
        break
    else:
        print("incorrecto")
        puntaje += 1