#Realice una función que procesa la información de alumnos de la UNAJ. De cada
#alumno se conoce legajo, nombre, apellido, contraseña. El procesamiento termina
#cuando se ingresa el número de legajo 0. La función deberá retornar una lista con
#la información procesada.

#alumnos
    #legajo  -> 0  que salga
    #nombre
    #apellido
    #constraseña

#devolver una lista = ["legajo, nombre, apellido, contraseña"]

def alumnos():
    lista = []
    print("Ingrese 0 para salir")
    legajo = int(input("Ingrese el numero de legajo: "))
    salir = 0
    while legajo != salir:
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        contraseña = input("Ingrese su contraseña: ")
        total = [legajo, nombre, apellido, contraseña]
        lista.append(total)
        legajo = int(input("Ingrese el numero de legajo: "))
    return lista

def imprimir_alumno(total):
    legajo = total[0]
    nombre = total[1]
    apellido = total[2]
    contraseña = total[3]
    
    print("\nLegajo: " + str(legajo))
    print("nombre: " + str(nombre))
    print("apellido: " + str(apellido))
    print("contraseña: " + str(contraseña))


def legajo_menor(lista_alumnos):

    alumno_menor_legajo = lista_alumnos[0]
    
    for alumno in lista_alumnos:
        if alumno[0] < alumno_menor_legajo[0]:
            alumno_menor_legajo = alumno
    
    return alumno_menor_legajo
        

def nombre_mas_largo(lista_alumnos):

    nombre_largo = lista_alumnos[0][1]
    for alumno in lista_alumnos:
        nombre_actual = alumno[1]
        if len(nombre_actual) > len(nombre_largo):
            nombre_largo = nombre_actual

    return nombre_largo

def controlar_clave(lista_alumnos):
    contraseñas_validas = []  # Lista para almacenar las contraseñas válidas

    for datos in lista_alumnos:
        contraseña_actual = datos[3]
        if len(contraseña_actual) >= 6 and contraseña_actual != "123456789":
            contraseñas_validas.append(datos)

    return contraseñas_validas

# Llamo a la función 1
x = alumnos() 
print(x)

# Llamo a la función 2
#pregunta = int(input("Elija un número de lista: "))
#imprimir_alumno(x[pregunta])

# Llamo a la función 3
#alumno_menor = legajo_menor(x)
#print("Datos del alumno con el menor legajo:" + str(alumno_menor))
#imprimir_alumno(alumno_menor)

#llamo a la funcion 4
#nombre_largo = nombre_mas_largo(x)
#print("Los datos del alumno con el nombre mas largo son:")
#imprimir_alumno(nombre_largo)


#llamo a la funcion 4
contraseñas_validas = controlar_clave(x)
print("Los datos de los alumnos con contraseñas válidas son:")
for alumno in contraseñas_validas:
    imprimir_alumno(alumno)
