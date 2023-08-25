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
        print("Continuará...")
    elif answer.lower() == "2":
        print("Encuentro con una criatura misteriosa")
        print("Tomas el camino de la derecha y pronto te das cuenta de que no estás solo en la selva. Encuentras una criatura misteriosa con escamas brillantes y ojos brillantes.")
        print("Continuará...")
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
        print("Continuará...")
    elif answer.lower() == "2":
        print("Los símbolos reveladores")
        print("Decides estudiar los símbolos tallados en la puerta. Después de un tiempo, te das cuenta de que representan los elementos naturales: tierra, agua, fuego y aire. Comienzas a tocar los símbolos en un orden específico y la puerta se abre lentamente.")
        print("Dentro de la habitación, encuentras un libro antiguo que contiene pistas sobre la ubicación de un tesoro aún más grande en la isla.")
        print("Continuará...")
    else:
        print("Perdiste")
else: 
    print("Perdiste")

