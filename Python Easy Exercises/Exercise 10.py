import random

respuesta = ["piedra", "papel", "tijera"]
print("Bienvenido a mi juego")
print("Opciones:")
print("Piedra, Papel o Tijera")


while True:
    respuesta_seleccionada = random.choice(respuesta).lower()
    pregunta_elije = input("Elije tu respuesta (escribe 'salir' para terminar): ").lower()
    if (
            (pregunta_elije == "piedra" and respuesta_seleccionada == "tijera") or
            (pregunta_elije == "papel" and respuesta_seleccionada == "piedra") or
            (pregunta_elije == "tijera" and respuesta_seleccionada == "papel")
        ):
            print("¡Ganaste!")   
    if (
            (pregunta_elije == "tijera" and respuesta_seleccionada == "papel") or
            (pregunta_elije == "piedra" and respuesta_seleccionada == "papel") or
            (pregunta_elije == "papel" and respuesta_seleccionada == "tijera")
        ):
            print("¡Perdiste!") 
    elif pregunta_elije == "salir":
        break
    elif pregunta_elije == respuesta_seleccionada:
            print("¡Empate!")
    
 