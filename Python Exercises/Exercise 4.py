    #Quiz Game

print("¡Bienvenido a mi juego!")

starting = input('¿Querés jugar?: ')

if starting.lower() != 'si':
        quit()

print("¡Okay! ¡Empecemos!")
score = 0

answer = input('¿Quién es el máximo goleador en la historia de la Copa del Mundo de la FIFA?: ')
if answer.lower() == 'miroslav klose':
    print('¡Correcto!')
    score += 1
else:
    print('¡Incorrecto!')
    score -= 1

answer = input('¿Cuál es el equipo de fútbol más antiguo del mundo que sigue en actividad?: ')
if answer.lower() == 'sheffield fc':
    print('¡Correcto!')
    score += 1
else:
    print('¡Incorrecto!')
    score -= 1
answer = input('¿En qué año fué fundado?: ')
if answer == '1857':
    print('¡Correcto!')
    score += 1
else:
    print('¡Incorrecto!')
    score -= 1

answer = input('¿Cuál es el único país en ganar la Copa Mundial de la FIFA en su propia tierra dos veces?: ')
if answer.lower() == 'italia':
    print('¡Correcto!')
    score += 1
else:
    print('¡Incorrecto!')
    score -= 1

answer = input('¿Qué equipo de fútbol ha ganado la Liga de Campeones de la UEFA más veces?: ')
if answer.lower() == 'real madrid':
    print('¡Correcto!')
    score += 1
else:
    print('¡Incorrecto!')
    score -= 1

answer = input('¿En qué año se introdujo el sistema de tarjetas amarillas y rojas en el fútbol?: ')
if answer == '1970':
    print('¡Correcto!')
    score += 1
else:
    print('¡Incorrecto!')
    score -= 1

answer = input(' ¿Quién es el único jugador en la historia en haber ganado tres Copas Mundiales como jugador y una como entrenador?: ')
if answer.lower() == 'mário zagallo':
    print('¡Correcto!')
    score += 1
elif answer.lower() == 'mario zagallo':
    print('¡Correcto!')
    score += 1
else:
    print('¡Incorrecto!')
    score -= 1

if score >= 1:
    print('¡Anotaste ' + str(score) + ' goles!')
else:
    print('¡Perdiste! ' + str(score) + ' puntos.')
    quit()

print('Obtuviste ' + str((score / 4) * 100) + '%.')
