#more quiz games

print("Hola!!! Bienvenido a mi juego")

comienzo = input('¿Estas listo?: ')

if comienzo.lower() != "si":
        quit()

puntuaje =  0

pregunta = input('¿Qué océano está al este de África?: ')
if pregunta.lower() == 'oceano indico':
        print('¡Correcto!')
        puntuaje += 1
else:
        print('¡Incorrecto!')

pregunta = input('¿Cuál es la montaña más alta de América del Norte?: ')
if pregunta.lower() == 'el monte mckinley':
        print('¡Correcto!')
        puntuaje += 1
else:
        print('¡Incorrecto!')

pregunta = input('¿Qué país es conocido como "la Tierra de Fuego"?: ')
if pregunta.lower() == 'argentina':
        print('¡Correcto!')
        puntuaje += 1
else:
        print('¡Incorrecto!')

pregunta = input('¿Cuál es la capital de Australia?: ')
if pregunta.lower() == 'canberra':
        print('¡Correcto!')
        puntuaje += 1
else:
        print('¡Incorrecto!')

pregunta = input('¿Cuál es el país más grande del mundo por área terrestre?: ')
if pregunta.lower() == 'rusia':
        print('¡Correcto!')
        puntuaje += 1
else:
        print('¡Incorrecto!')


if puntuaje == 1:
        print('Tu puntuación final fue de ' + str(puntuaje) + ' punto!')
else:
    print('Tu puntuación final fue de ' + str(puntuaje) + ' puntos!')

