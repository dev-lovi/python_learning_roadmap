'''
Desarrollar un sistema que procese las solicitudes de vacunacion contra covid 19. 
De cada solicitud se conoce nombre, apellido, DNI, edad y ocupación. 
Se deben leer solicitudes hasta encontrar una con DNI igual a 0.
									
Funcion 1: informa la ocupacion de la persona mas joven
Funcion 2: informa el promedio de edad de las personas con ocupacion SEGURIDAD que presentaron la solicitud.
Funcion 3: cantidad de personas mayores a 50 años y que se ocupen en salud.
'''


def funcion_principal():
    lista = []
    
    DNI = int(input("Ingrese su DNI: "))

    while DNI != 0:
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        edad = int(input("Ingrese su edad: "))
        ocupacion = input("Ingrese su ocupacion: ").lower()
        total = [nombre, apellido, DNI, edad, ocupacion]

        lista.append(total)
        DNI = int(input("Ingrese su DNI: "))

    return lista

a = funcion_principal()
#print(a)


def mas_joven(lista):
    edad_min = 999
    datos_joven = 'a'

    for datos in lista:
        if datos[3] < edad_min:
            edad_min = datos[3]
            datos_joven = datos
    
    return datos_joven


b = mas_joven(a)
print(b)



def promedio_edad(lista):
    cantidad = 0
    edad = 0

    for datos in lista:
        if datos[4] == 'seguridad':
            cantidad += 1
            edad += datos[3]
    
    calculo = edad / cantidad

    return calculo

c = promedio_edad(a)
print(c)



def mayor_salud(lista):
    lista_nueva = []

    for datos in lista:
        if datos[3] > 50 and datos[4] == 'salud':
            lista_nueva.append(datos)

    return lista_nueva

d = mayor_salud(a)
print(d)