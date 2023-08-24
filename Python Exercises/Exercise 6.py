def mostrar_menu_principal():
    print("Menú Principal:")
    print("1. Juegos Quiz")
    print("2. Elije tu destino")
    print("3. Salir")

def mostrar_menu_categoria1():
    print("Elegiste la opción Juegos Quiz:")
    print("1. Fútbol")
    print("2. Geografía")
    print("3. Volver al menú principal")

def mostrar_menu_categoria2():
    print("Elegiste la opción Elije tu destino:")
    print("1. Opción A")
    print("2. Opción B")
    print("3. Volver al menú principal")

def main():
    while True:
        mostrar_menu_principal()
        opcion_principal = input("Elija una opción: ")

        if opcion_principal == "1":
            while True:
                mostrar_menu_categoria1()
                opcion_categoria1 = input("Elija una opción: ")
                if opcion_categoria1 == "1":
                    #Meter código de futbol
                    print("¡Quiz de Futbol!")
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


                    print("Realizando acción para la opción 1 de Categoría 1")
                elif opcion_categoria1 == "2":
                    #Meter código de geo
                    print("¡Quiz de Geografía!")
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


                    print("Realizando acción para la opción 2 de Categoría 1")
                elif opcion_categoria1 == "3":
                    break  # Volver al menú principal
                else:
                    print("Opción no válida. Intente de nuevo.")

        elif opcion_principal == "2":
            while True:
                mostrar_menu_categoria2()
                opcion_categoria2 = input("Elija una opción de Categoría 2: ")
                if opcion_categoria2 == "1":
                    # Realizar acción para la opción A de Categoría 2
                    print("Realizando acción para la opción A de Categoría 2")
                elif opcion_categoria2 == "2":
                    # Realizar acción para la opción B de Categoría 2
                    print("Realizando acción para la opción B de Categoría 2")
                elif opcion_categoria2 == "3":
                    break  # Volver al menú principal
                else:
                    print("Opción no válida. Intente de nuevo.")

        elif opcion_principal == "3":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
