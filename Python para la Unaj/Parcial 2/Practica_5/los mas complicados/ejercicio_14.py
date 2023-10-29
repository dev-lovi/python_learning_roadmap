#Ejercicio 14: Realice un programa para manejar equipos de fútbol.
#a) Definir una función que arme una lista con la información de los equipos. De cada equipo se quiere guardar el nombre del equipo, puntaje en la tabla de posiciones y la cantidad de goles a favor. El ingreso finaliza cuando se lee el nombre del equipo igual a ‘ZZZ’.
#b) Usando la lista anterior, imprimir la cantidad de goles a favor que tienen los equipos que están en la primera y última posición de la lista.
#c) Imprimir el nombre del equipo Campeón de la lista del ejercicio anterior


#uh que paja este pa eh jajaj
#datos
    #nombre del equipo  --> si es igual a 'zzz' que se salga
    #puntaje en la tabla
    #cantidad de goles a favor

#Punto A    

def mis_equipos(valor):
    while True:
        nombres = input("Ingrese el nombre del equipo, 'zzz' para salir: ")
        if nombres == 'zzz':
            break
        puntajes = int(input("¿Cual es su puntaje?: "))
        goles = int(input("¿Cuantos goles tiene a favor?: "))
        valor.append((nombres, puntajes, goles))
        print("Por el momento, los equipos ingresados son: " + str(valor))
    
    #print(str(valor[0]) + str(valor[-1]))

lista = []
mis_equipos(lista)

#Punto B imprimir la cantidad de goles a favor que tienen los equipos que están en la primera y última posición de la lista
print("El primer equipo tiene " + str(lista[0][1]) + " goles y el segundo tiene " + str(lista[-1][1] + " goles."))


# Punto C (Encontrar el equipo campeón)
def campeon(equipos):
    puntaje_maximo = 0
    equipo_campeon = ""
        
    for equipo in equipos:
        nombre = equipo[0]
        puntaje = equipo[1]
            
        if puntaje > puntaje_maximo:
            puntaje_maximo = puntaje
            equipo_campeon = nombre
        
    print("El equipo campeón es:", equipo_campeon)

campeon(lista)






