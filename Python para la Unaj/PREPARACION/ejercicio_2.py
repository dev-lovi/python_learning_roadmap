'''
Realice un programa para una universidad. 
El mismo deberá permitir ingresar datos de todos los alumnos de la comisión 13 que realizaron el parcial correspondiente para poder aprobar la materia de fundamentos de informática. 
El programa deberá permitir cargar los siguientes datos (nombre, apellido, mail y nota del alumno), la carga finalizará cuando en nombre se ingrese "zzz".

En otra función se deben crear 2 listas. Una con nombre y apellido de todos los alumnos que aprobaron y otra con los mismos datos de los que desaprobaron (la materia se aprueba con una nota igual o mayor a 4). 

También mostrar el porcentaje de los alumnos aprobados y el promedio de todas las notas. 

Además, con otra función imprimir el nombre, apellido y nota del mejor y del peor alumno.

Para finalizar, el programa creado debe permitir conocer si un alumno aprobó o no la materia ingresando nombre y apellido del mismo. El alumno será indicado por el usuario (si el nombre y apellido no están en la lista, imprimir el siguiente mensaje "el alumno que ingresó no está en la lista").


'''




def datos_del_alumno():
    lista = []
    nombre = input("Ingrese nombre del alumno/a: ")
    
    while nombre != "zzz":
        apellido = input("Ingrese apellido del alumno/a: ")
        mail = input("Ingrese MAIL del alumno/a: ")
        nota = float(input("Ingrese nota de alumno/a: "))
        total = [nombre, apellido, mail, nota]
        lista.append(total)
        nombre = input("Ingrese nombre de alumno/a o zzz para finalizar: ")

    return lista

a = datos_del_alumno()

def aprobados_y_desaprobados(lista):
    aprobados = []
    desaprobados = []

    for x in lista:
        if x[3] >= 4:
            aprobados.append([x[0], x[1]])
        else:
            desaprobados.append([x[0], x[1]])

    print("\nLISTA DE APROBADOS Y DESAPROBADOS")
    print("Aprobados:", aprobados)
    print("Desaprobados:", desaprobados)

aprobados_y_desaprobados(a)