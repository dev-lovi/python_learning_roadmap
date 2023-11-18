#Ejercicio 4:
#Se desea realizar un programa para una universidad. El mismo deberá permitir guardar la
#información de todos los cursos que se dictan en la misma. La cantidad de cursos
#existentes es ingresado por el usuario del sistema. De cada curso se debe conocer:
#Nombre, Cantidad de Clases, Día de Dictado, Hora de Comienzo, Duración en minutos.
#Importante: si la duración del curso es mayor a 360 minutos, NO se debe guardar la
#información del mismo.

def agregar_curso(valor_lista):
    condicion = 'b'
    while condicion != 'aaa':
        nombre = input("Ingresar nombre del curso, 'aaa' para salir: ")
        if nombre == 'aaa':
            condicion = 'aaa'
        else:
            cant_clases = int(input("Ingresar la cantidad de clases: "))
            dia_dictado = input("Ingresar dia de dictado: ")
            hora_comienzo = input("Ingresar hora de comienzo: ")
            duracion = int(input("Ingresar duracion: "))
            curso = [nombre, cant_clases, dia_dictado, hora_comienzo, duracion]
            if duracion > 360:
                print("La duracion debe ser menor a 360 min")
            else:
                valor_lista.append(curso)
    return valor_lista

#a) Imprimir todos los cursos que tengan más de 5 clases
def curso_5_clases(valor_lista):
    cursos_mas_de_5_clases = []

    for curso in valor_lista:
        if curso[1] > 5:
            cursos_mas_de_5_clases.append(curso)    
    return cursos_mas_de_5_clases



#b) Imprimir los cursos que se dictan en un día de la semana indicado por el usuario.


def dias_de_semana(valor_lista):
    dia_elegido = input("¿Que dia de la semana?: ")
    cursos_semana = []
    
    for curso in valor_lista:
        if curso[2] == dia_elegido:
            cursos_semana.append(curso)
    return cursos_semana



#c) Imprimir el curso más intensivo (definido por la cantidad de clases y la duración de
#cada clase)

def intensivo(valor_lista):
    mas_intensivo = []
    max_intensidad = 0
    
    for curso in valor_lista:
        intensidad = curso[1] * curso[4]
        if intensidad > max_intensidad:
            max_intensidad = intensidad
            suma = [curso[0], curso[1], curso[4]]
            mas_intensivo.append(suma)
    return mas_intensivo

#D) Imprimir los datos en que se dicta un curso indicado por el usuario.
def mostrar_curso(valor_lista):
    curso_elegido = input("¿Qué curso queres ver?: ")
    elegido_lista = []

    for curso in valor_lista:
        if curso[0] == curso_elegido:
            elegido_lista.append(curso)
    return elegido_lista



#e) Imprima todos los cursos que comienzan con una letra indicada por el usuario.
#El programa escrito deberá mostrar un menú para que el usuario elija la opción deseada.

def letra_buscar(valor_lista):
    letra_elegida = input("Ingresa una letra: ")
    lista_iniciales = []

    #curso = [nombre, cant_clases, dia_dictado, hora_comienzo, duracion]
    for curso in valor_lista:
        if curso[0][0] == letra_elegida:
            lista_iniciales.append(curso)
    return lista_iniciales
    

#x = []
#agregar_curso(x)

#funcion 5 clases
#a = curso_5_clases(x)
#print(a)

#funcion semana
#a  = dias_de_semana(x)
#print(a)

#funcion intensivo
#a = intensivo(x)
#print(a)

#funcion mostrar
#a = mostrar_curso(x)
#print(a)

#funcion letra buscar
#a = letra_buscar(x)
#print(a)



#Menu Principal

x = []
#agregar_curso(x)


condicion_menu = 5
while condicion_menu != 0:
    
    print("\nMenú de opciones")
    print("1. Agregar cursos")
    print("2. Curso con mas de 5 clases")
    print("3. Curso solo una vez a la semana")
    print("4. Curso mas intensivo")
    print("5. Info del curso")
    print("6. Info del curso por su inicial")
    print("7. Salir")

    pregunta = (int(input("Ingrese una opcion: ")))

    if pregunta == 7:
        condicion_menu = 0
    elif pregunta == 1:
        agregar_curso(x)
    elif pregunta == 2:
        a = curso_5_clases(x)
        print(a)
    elif pregunta == 3:
        a = dias_de_semana(x)
        print(a)
    elif pregunta == 4:
        a = intensivo(x)
        print(a)
    elif pregunta == 5:
        a = mostrar_curso(x)
        print(a)
    elif pregunta == 6:
        a = letra_buscar(x)
        print(a)
    else:
        print("Opcion incorrecta")
        pregunta = (int(input("Ingrese una opcion: ")))

#
