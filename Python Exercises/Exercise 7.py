    #Choose your own adventure
print("El misterio en la isla perdida")
print("Tú eres el protagonista y tomarás decisiones clave en la historia. ¡Buena suerte!")

print("Estás de vacaciones en un tranquilo pueblo costero cuando escuchas un rumor intrigante sobre una isla cercana. Se dice que esta isla está llena de tesoros ocultos y misterios sin resolver. Decides embarcarte en una aventura y visitar la isla.")

print("Opción 1: Tratar de comunicarte con la criatura.")
print("Opción 2: Retroceder lentamente y buscar otro camino.")
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
                print("Continuara...")
            elif answer.lower() == "2":
                print("Continuará...")
            else:
                print("Perdiste")
        elif answer.lower() == "2":
            print("Misterio sin resolver")
            print("Sigues explorando el camino en busca de más pistas sobre el misterio de la isla. Llegas a un claro en la selva y encuentras una piedra tallada con inscripciones antiguas.")
            print("Opción 1: Intentar descifrar las inscripciones.")
            print("Opción 2: Ignorar la piedra y seguir explorando.")
            answer = input("Elije una opción: ")
            if answer.lower() == "1":
                print("Continuara...")
            elif answer.lower() == "2":
                print("Continuará...")
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
                print("Continuará...")
            elif answer.lower() == "2":
                print("Continuará")
            else:
                print("Perdiste")
        elif answer.lower() == "2":
            print("Investigación adicional")
            print("Decides investigar más la habitación antes de tomar algo. Encuentras un diario antiguo que describe la historia de la isla y las personas que la habitaban. Parece que hay un misterio aún más profundo que resolver.")
            print("Opción 1: Leer el diario y buscar pistas adicionales.")
            print("Opción 2: Dejar el diario y tomar algunos tesoros antes de irte.")
            answer = input("Elije una opción: ")
            if answer.lower() == "1":
                print("Continuará...")
            elif answer.lower() == "2":
                print("Continuará")
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
        if answer.lower() == "1":
            print("En busca del tesoro oculto")
            print("Decides tomar el libro antiguo y buscar el tesoro mencionado en él. El libro proporciona pistas detalladas que te llevan a una cueva subterránea. Dentro de la cueva, encuentras un cofre aún más grande y valioso.")
            print("Opción 1: Abrir el cofre y revelar su contenido.")
            print("Opción 2: Ser cauto y salir de la cueva para buscar ayuda.")
            answer = input("Elije una opción: ")
            if answer.lower() == "1":
                print("Continuará...")
            elif answer.lower() == "2":
                print("Continuará")
            else:
                print("Perdiste")
        elif answer.lower() == "2":
            print("Continuar la exploración")
            print("Decides salir de la habitación sin tomar nada y continuar explorando la isla en busca de más pistas. Pronto encuentras una serie de extrañas piedras que forman un camino hacia una montaña en el centro de la isla.")
            print("Opción 1: Seguir el camino de piedras hacia la montaña.")
            print("Opción 2: Ignorar el camino y explorar otros lugares de la isla.")
            answer = input("Elije una opción: ")
            if answer.lower() == "1":
                print("Continuará...")
            elif answer.lower() == "2":
                print("Continuará")
            else:
                print("Perdiste")
        else:
            print("Perdiste")
    else:
        print("Perdiste")
else: 
    print("Perdiste")