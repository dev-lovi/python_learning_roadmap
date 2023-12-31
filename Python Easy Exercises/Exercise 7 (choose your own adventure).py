    #Choose your own adventure
print("El misterio en la isla perdida")
print("Tú eres el protagonista y tomarás decisiones clave en la historia. ¡Buena suerte!")

print("Estás de vacaciones en un tranquilo pueblo costero cuando escuchas un rumor intrigante sobre una isla cercana. Se dice que esta isla está llena de tesoros ocultos y misterios sin resolver. Decides embarcarte en una aventura y visitar la isla.")

print("Opción 1: Tomar un bote y explorar la isla por ti mismo.")
print("Opción 2: Buscar a un guía local que conozca la isla.")
answer = input("Elije una opción: ")
if answer.lower() == "1":
    print("Exploración solitaria")
    print("Decides tomar un bote y explorar la isla por tu cuenta. Mientras caminas por la selva densa, te encuentras con una bifurcación en el camino.")
    print("Opción 1: Tomar el camino de la izquierda.")
    print("Opción 2: Tomar el camino de la derecha.")
    answer = input("Elije una opción: ")
    if answer.lower() == "1":
        print("El camino misterioso")
        print("Tomas el camino de la izquierda y te adentras más en la selva. De repente, encuentras una cascada impresionante con un arco iris brillante sobre ella.")
        print("Opción 1: Descender por la cascada para buscar tesoros detrás de ella.")
        print("Opción 2: Continuar por el camino en busca de otros indicios sobre el misterio de la isla.")
        answer = input("Elije una opción: ")
        if answer.lower() == "1":
            print("Tesoro detrás de la cascada")
            print("Desciendes por la cascada con cuidado y llegas a una cueva oculta detrás de ella. Dentro de la cueva, encuentras un cofre antiguo lleno de monedas de oro y joyas raras.")
            print("Opción 1: Tomar el cofre y regresar al pueblo.")
            print("Opción 2: Explorar más la cueva en busca de pistas adicionales.")
            answer = input("Elije una opción: ")
            if answer.lower() == "1":
                print("El cofre del tesoro")
                print("Tomaste el cofre lleno de tesoros y regresaste al pueblo. Has encontrado suficiente riqueza para vivir cómodamente el resto de tu vida. Tu aventura en la isla ha sido un éxito.")
                print("¡Felicidades, has completado tu aventura con éxito!")
            elif answer.lower() == "2":
                print("Exploración adicional de la cueva")
                print("Decides explorar más la cueva en busca de pistas adicionales. Te adentras más en la oscuridad y encuentras un túnel misterioso que se adentra en las profundidades de la isla.")
                print("Opción 1: Seguir el túnel y descubrir a dónde lleva.")
                print("Opción 2: Retroceder y salir de la cueva.")
                answer = input("Elije una opción: ")
                if answer.lower() == "1":
                    print("Seguir el túnel")
                    print("Decides seguir el túnel y descubres que conduce a una cámara subterránea llena de tesoros. Parece que has encontrado el tesoro más grande de todos.")
                    print("Felicidades, tu aventura ha llegado a su emocionante final.")
                elif answer.lower() == "2":
                    print("Retroceso sabio")
                    print("Decides retroceder y salir de la cueva. Mientras sales, encuentras un mapa antiguo que muestra la ubicación de varios tesoros en la isla.")
                    print("Opción 1: Seguir las pistas del mapa hacia el tesoro.")
                    print("Opción 2: Regresar al pueblo y compartir el mapa con otros.")
                    answer = input("Elije una opción: ")
                    if answer.lower() == "1":
                        print("Seguir las pistas del mapa")
                        print("Decides seguir las pistas del mapa hacia el tesoro mencionado. Después de una búsqueda ardua, encuentras el tesoro escondido en una isla cercana.")
                        print("Felicidades, has completado tu aventura con éxito.")
                    elif answer.lower() == "2":
                        print("Regresar al pueblo")
                        print("Regresas al pueblo y compartes el mapa con otros. Juntos, forman un equipo de búsqueda y encuentran el tesoro escondido en la isla.")
                        print("Felicidades, has completado tu aventura con éxito.")
                    else:
                        print("Perdiste")
                else:
                    print("Perdiste")
            else:
                print("Perdiste")
        elif answer.lower() == "2":
            print("Misterio sin resolver")
            print("Sigues explorando el camino en busca de más pistas sobre el misterio de la isla. Llegas a un claro en la selva y encuentras una piedra tallada con inscripciones antiguas.")
            print("Opción 1: Intentar descifrar las inscripciones.")
            print("Opción 2: Ignorar la piedra y seguir explorando.")
            answer = input("Elije una opción: ")
            if answer.lower() == "1":
                print("Descifrar las inscripciones")
                print("Te esfuerzas por descifrar las inscripciones en la piedra tallada. Después de un tiempo, logras entender que indican la ubicación de un antiguo templo en la isla. Decides buscar este templo en busca de tesoros ocultos.")
                print("Opción 1: Ir en busca del antiguo templo.")
                print("Opción 2: Continuar explorando la selva en busca de pistas adicionales.")
                answer = input("Elije una opción: ")
                if answer.lower() == "1":
                    print("En busca del antiguo templo")
                    print("Decides buscar el antiguo templo mencionado en las inscripciones. Sigues las indicaciones de la piedra tallada y finalmente llegas al templo. Dentro del templo, encuentras un tesoro antiguo y valioso.")
                    print("Felicidades, has completado tu aventura con éxito.")
                elif answer.lower() == "2":
                    print("Explorar más la selva")
                    print("Optas por explorar más la selva en busca de pistas adicionales. Después de un tiempo, encuentras un conjunto de antiguas estatuas que te guían hacia un río subterráneo.")
                    print("Opción 1: Seguir el río subterráneo en busca de un tesoro.")
                    print("Opción 2: Regresar al pueblo y compartir tus descubrimientos.")
                    answer = input("Elije una opción: ")
                    if answer.lower() == "1":
                        print("Seguir el río subterráneo")
                        print("Sigues el río subterráneo en busca de un tesoro. Después de un tiempo, llegas a una cámara subterránea llena de tesoros y artefactos antiguos.")
                        print("Felicidades, has completado tu aventura con éxito.")
                    elif answer.lower() == "2":
                        print("Compartir tus descubrimientos")
                        print("Regresas al pueblo y compartes tus descubrimientos con otros. Tu historia se convierte en una leyenda local y tu nombre se asocia con la búsqueda de tesoros.")
                        print("Felicidades, has completado tu aventura con éxito.")
                    else:
                        print("Perdiste")
                else:
                    print("Perdiste")
            elif answer.lower() == "2":
                print("Ignorar la piedra")
                print("Decides ignorar la piedra tallada y continuar explorando la selva en busca de pistas adicionales. Después de un tiempo, te encuentras con un río que fluye hacia una cascada impresionante.")
                print("Opción 1: Seguir el río aguas arriba en busca de un tesoro.")
                print("Opción 2: Descender por la cascada en busca de una entrada secreta.")
                answer = input("Elije una opción: ")
                if answer.lower() == "1":
                    print("Seguir el río aguas arriba")
                    print("Sigues el río aguas arriba en busca de un tesoro. Después de un tiempo, encuentras una cueva oculta detrás de una cascada. Dentro de la cueva, encuentras un cofre lleno de gemas y monedas antiguas.")
                    print("Felicidades, has completado tu aventura con éxito.")
                elif answer.lower() == "2":
                    print("Descender por la cascada")
                    print("Decides descender por la cascada en busca de una entrada secreta. Al hacerlo, te sumerges en un túnel submarino que te lleva a una cámara submarina llena de tesoros hundidos.")
                    print("Felicidades, has encontrado el tesoro y completado tu aventura con éxito.")
                else:
                    print("Perdiste")
            else:
                print("Perdiste")
        else:
            print("Perdiste")
    elif answer.lower() == "2":
        print("Encuentro con una criatura misteriosa")
        print("Tomas el camino de la derecha y pronto te das cuenta de que no estás solo en la selva. Encuentras una criatura misteriosa con escamas brillantes y ojos brillantes.")
        print("Opción 1: Tratar de comunicarte con la criatura.")
        print("Opción 2: Retroceder lentamente y buscar otro camino.")
        answer = input("Elije una opción: ")
        if answer.lower() == "1":
            print("Comunicación con la criatura")
            print("Te acercas con cuidado a la criatura misteriosa y tratas de comunicarte con ella. Descubres que es amigable y te guía a través de la selva hacia un hermoso jardín secreto lleno de flores exóticas.")
            print("Opción 1: Explorar el jardín secreto.")
            print("Opción 2: Preguntar a la criatura si conoce algún tesoro en la isla.")
            answer = input("Elije una opción: ")
            if answer.lower() == "1":
                print("Continuara...")
            elif answer.lower() == "2":
                print("Continuara...")
            else:
                print("Perdiste...")
        elif answer.lower() == "2":
            print("Retroceso seguro")
            print("Decides retroceder lentamente y buscar otro camino. Te alejas de la criatura sin molestarla y continúas explorando la selva. Encuentras un arroyo cristalino que te lleva a una playa desierta.")
            print("Opción 1: Explorar la playa en busca de tesoros.")
            print("Opción 2: Seguir el arroyo mar adentro en busca de una salida.")
            answer = input("Elije una opción: ")
            if answer.lower() == "1":
                print("Continuara...")
            elif answer.lower() == "2":
                print("Continuara...")
            else:
                print("Perdiste")
        else:
            print("Perdiste")
    else: 
        print("Perdiste")


elif answer.lower() == "2":
    print("Búsqueda de un guía")
    print("Buscas a un guía local que conozca la isla. Encuentras a un anciano llamado Miguel, quien accede a ayudarte a cambio de una pequeña suma de dinero. Juntos, comienzan la exploración de la isla.")
    print("Después de un rato, llegan a un antiguo templo cubierto de enredaderas y helechos. Ves una puerta misteriosa con tres símbolos tallados.")
    print("Opción 1: Intentar abrir la puerta sin tocar los símbolos.")
    print("Opción 2: Estudiar los símbolos y tratar de entender su significado.")
    answer = input("Elije una opción: ")
    if answer.lower() == "1":
        print("Puerta misteriosa")
        print("Decides intentar abrir la puerta sin tocar los símbolos. La puerta se abre lentamente y revela una habitación oscura llena de tesoros brillantes. Parece que has encontrado el tesoro perdido de la isla.")
        print("Opción 1: Comenzar a recoger los tesoros.")
        print("Opción 2: Investigar más la habitación antes de tomar algo.")
        answer = input("Elije una opción: ")
        if answer.lower() == "1":
            print("El tesoro brillante")
            print("Comienzas a recoger los tesoros en la habitación. Parece que has encontrado suficiente riqueza para cambiar tu vida para siempre. Mientras lo haces, escuchas un ruido siniestro desde el fondo de la habitación.")
            print("Opción 1: Continuar recogiendo tesoros y arriesgarte.")
            print("Opción 2: Dejar los tesoros y salir de la habitación rápidamente.")
            answer = input("Elije una opción: ")
            if answer.lower() == "1":
                print("Riesgo y recompensa")
                print("Continúas recogiendo tesoros en la habitación a pesar del ruido siniestro que escuchaste antes. De repente, una trampa se activa y quedas atrapado en la habitación oscura.")
                print("Opción 1: Intentar encontrar una salida.")
                print("Opción 2: Gritar en busca de ayuda.")
                answer = input("Elije una opción: ")
                if answer.lower() == "1":
                    print("En busca de una salida")
                    print("Intentas encontrar una salida después de quedar atrapado en la habitación oscura. Después de un tiempo, encuentras una puerta secreta que te lleva a un pasadizo subterráneo que te lleva a la libertad.")
                    print("Felicidades, has completado tu aventura con éxito.")
                elif answer.lower() == "2":
                    print("Gritar en busca de ayuda")
                    print("Gritas en busca de ayuda y pronto escuchas a otros aventureros que te rescatan. Aunque no obtuviste tesoros, tu historia se convierte en una leyenda en el pueblo.")
                    print("Felicidades, has completado tu aventura con éxito.")
                else:
                    print("Perdiste")
            elif answer.lower() == "2":
                print("Salida rápida")
                print("Decides dejar los tesoros y salir de la habitación rápidamente. Sales justo a tiempo antes de que la puerta se cierre detrás de ti. Aunque no obtuviste tesoros, has evitado un peligro desconocido.")
                print("Opción 1: Continuar explorando la isla en busca de más pistas.")
                print("Opción 2: Regresar al pueblo y contar tu experiencia.")
            else:
                print("Perdiste")
        elif answer.lower() == "2":
            print("Investigación adicional")
            print("Decides investigar más la habitación antes de tomar algo. Encuentras un diario antiguo que describe la historia de la isla y las personas que la habitaban. Parece que hay un misterio aún más profundo que resolver.")
            print("Opción 1: Leer el diario y buscar pistas adicionales.")
            print("Opción 2: Dejar el diario y tomar algunos tesoros antes de irte.")
            answer = input("Elije una opción: ")
            if answer.lower() == "1":
                print("Leer el diario")
                print("Decides leer el diario y buscas pistas adicionales. El diario te lleva a un punto específico en la isla donde se dice que se encuentra un tesoro perdido. Decides seguir las pistas y buscar el tesoro.")
                print("Opción 1: Seguir las pistas del diario hacia el tesoro.")
                print("Opción 2: Regresar al pueblo y buscar ayuda para encontrar el tesoro.")
                answer = input("Elije una opción: ")
                if answer.lower() == "1":
                    print("Seguir las pistas del diario")
                    print("Decides seguir las pistas del diario hacia el tesoro. Después de una búsqueda ardua, encuentras el tesoro mencionado y te conviertes en una leyenda local.")
                    print("Felicidades, has completado tu aventura con éxito.")
                elif answer.lower() == "2":
                    print("Buscar ayuda")
                    print("Regresas al pueblo y compartes el mapa con otros. Juntos, forman un equipo de búsqueda y encuentran el tesoro escondido en la isla.")
                    print("Felicidades, has completado tu aventura con éxito.")
                else:
                    print("Perdiste")
            elif answer.lower() == "2":
                print("Tomar algunos tesoros")
                print("Decides tomar algunos tesoros antes de irte de la habitación. Mientras lo haces, escuchas el ruido siniestro de antes acercándose rápidamente.")
                print("Opción 1: Dejar los tesoros y buscar una salida.")
                print("Opción 2: Continuar tomando tesoros y arriesgarte.")
                answer = input("Elije una opción: ")
                if answer.lower() == "1":
                    print("Continuar tomando tesoros")
                    print("Decides continuar tomando tesoros a pesar del ruido siniestro que se acerca. De repente, quedas atrapado en una trampa y tu aventura llega a un final abrupto.")
                    print("Lamentablemente, tu aventura ha llegado a su fin.")
                elif answer.lower() == "2":
                    print("Riesgo final")
                    print("Continúas tomando tesoros a pesar del peligro que se avecina. De repente, una criatura antigua despierta y pone fin a tu búsqueda de tesoros.")
                    print("Lamentablemente, tu aventura ha llegado a su fin.")
                else:
                    print("Perdiste")
            else:
                print("Perdiste")
        else:
            print("Perdiste")
    elif answer.lower() == "2":
        print("Los símbolos reveladores")
        print("Decides estudiar los símbolos tallados en la puerta. Después de un tiempo, te das cuenta de que representan los elementos naturales: tierra, agua, fuego y aire. Comienzas a tocar los símbolos en un orden específico y la puerta se abre lentamente.")
        print("Dentro de la habitación, encuentras un libro antiguo que contiene pistas sobre la ubicación de un tesoro aún más grande en la isla.")
        print("Opción 1: Tomar el libro y buscar el tesoro.")
        print("Opción 2: Salir de la habitación y seguir explorando la isla.")
        answer = input("Elije una opción: ")
        if answer.lower() == "1":
            print("En busca del tesoro oculto")
            print("Decides tomar el libro antiguo y buscar el tesoro mencionado en él. El libro proporciona pistas detalladas que te llevan a una cueva subterránea. Dentro de la cueva, encuentras un cofre aún más grande y valioso.")
            print("Opción 1: Abrir el cofre y revelar su contenido.")
            print("Opción 2: Ser cauto y salir de la cueva para buscar ayuda.")
            answer = input("Elije una opción: ")
            if answer.lower() == "1":
                print("El cofre del tesoro")
                print("Abres el cofre dentro de la cueva subterránea y encuentras una increíble cantidad de riqueza y objetos antiguos. Tu vida está cambiando de manera significativa gracias a tu descubrimiento.")
                print("Felicidades, has encontrado el tesoro y completado tu aventura con éxito.")
            elif answer.lower() == "2":
                print("Búsqueda de ayuda")
                print("Decides ser cauto y salir de la cueva para buscar ayuda. Regresas al pueblo y contratas a un equipo de expertos para explorar la cueva con seguridad. Juntos, encuentran el tesoro y te vuelves famoso por tu descubrimiento.")
                print("Felicidades, has encontrado el tesoro y completado tu aventura con éxito.")
            else:
                print("Perdiste")
        elif answer.lower() == "2":
            print("Continuar la exploración")
            print("Decides salir de la habitación sin tomar nada y continuar explorando la isla en busca de más pistas. Pronto encuentras una serie de extrañas piedras que forman un camino hacia una montaña en el centro de la isla.")
            print("Opción 1: Seguir el camino de piedras hacia la montaña.")
            print("Opción 2: Ignorar el camino y explorar otros lugares de la isla.")
            answer = input("Elije una opción: ")
            if answer.lower() == "1":
                print("El camino de piedras")
                print("Sigues el camino de piedras hacia la montaña en el centro de la isla. En la cima, encuentras un altar antiguo con un objeto brillante encima de él.")
                print("Opción 1: Tomar el objeto brillante.")
                print("Opción 2: Investigar el altar con cuidado antes de tomar algo.")
                answer = input("Elije una opción: ")
                if answer.lower() == "1":
                    print("Tomar el objeto brillante")
                    print("Decides tomar el objeto brillante en la montaña. Al hacerlo, una luz deslumbrante te rodea y sientes una conexión profunda con la isla.")
                    print("Felicidades, has completado tu aventura con éxito.")
                elif answer.lower() == "2":
                    print("Investigar el altar")
                    print("Investigas el altar con cuidado antes de tomar algo. Descubres que el objeto brillante es en realidad una llave que encaja en una puerta antigua en la montaña.")
                    print("Felicidades, has completado tu aventura con éxito.")
                else:
                    print("Perdiste")
            elif answer.lower() == "2":
                print("Exploración continua")
                print("Decides ignorar el camino de piedras y explorar otros lugares de la isla. Llegas a una playa escondida donde encuentras una botella con un mensaje dentro.")
                print("Opción 1: Leer el mensaje.")
                print("Opción 2: Continuar explorando la playa.")
                answer = input("Elije una opción: ")
                if answer.lower() == "1":
                    print("Leer el mensaje")
                    print("Decides leer el mensaje dentro de la botella y descubres una invitación a unirse a una sociedad secreta de aventureros. Tu vida toma un giro emocionante mientras te embarcas en una nueva aventura.")
                    print("Felicidades, has completado tu aventura con éxito.")
                elif answer.lower() == "2":
                    print("Continuar explorando")
                    print("Decides continuar explorando la playa en busca de más tesoros. Pronto encuentras una serie de joyas raras y antiguas que te hacen rico y famoso en todo el mundo.")
                    print("Felicidades, has completado tu aventura con éxito.")
                else:
                    print("Perdiste")
            else:
                print("Perdiste")
        else:
            print("Perdiste")
    else:
        print("Perdiste")
else: 
    print("Perdiste")



#tratar de hacer una interfaz gráfica