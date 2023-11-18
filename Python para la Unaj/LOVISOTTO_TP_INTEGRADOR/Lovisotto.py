#Sistema de Gestión de Libros en una Biblioteca:

#En este caso estamos utilizando un bloc de notas como archivo, donde cargamos datos con la siguiente estructura: 
# Libro, Autor, Genero, Estado, Cantidad
# Ejemplo:
# Wizard and glass, Stephen King, Terror, Prestado, 1


#PUNTO 1. Carga de datos en una lista a partir de un archivo o descarga de datos a un archivo. Este punto es para que el alumno pueda investigar libremente.

#Para cargar y guardar datos de libros en un archivo.
def cargar_libros(archivo):
    libros = []
    #Como el enunciado indicaba, este punto es para que el alumno pueda investigar libremente.
    #Encontré el metodo 'with' para abrir archivos en python, entre sus comandos, use r para lectura y a para escritura

    with open(archivo, 'r') as file:
        #'r' (read): Este modo se utiliza para abrir un archivo en modo de solo lectura.     
            for line in file:
                # Separar cada línea en una lista de valores y agregar a la lista de libros
                libro_actual = [valor.strip() for valor in line.split(',')]
                libros.append(libro_actual)
    return libros


def agregar_libro(archivo):
    with open(archivo, 'a') as file:
        #'a': Este modo se utiliza para abrir un archivo en modo de escritura , pero agrega datos al final sin eliminar el contenido del mismo.
           
        # Solicitar datos al usuario (para Agregar más libros)
        condicion = 'a'
        while condicion != 'z':
            titulo = input("Ingrese el título del libro, ponga 'z' para salir: ")
            if titulo == 'z':
                 condicion = 'z'
            else:
                autor = input("Ingrese el nombre del autor: ")
                genero = input("Ingrese el género del libro: ")
                estado = input("Ingrese el estado del libro (Disponible/Prestado): ")
                cantidad = input("Ingrese la cantidad de ejemplares: ")

            # Escribir los datos en el archivo
                file.write(titulo + ',' + autor + ',' + genero + ',' + estado + ',' + cantidad + '\n')
                print("Libro agregado exitosamente.")



# Ejemplo de uso
ruta_archivo = 'datos.txt' #acá pongo el nombre del archivo que cree anteriormente (un bloc de notas vacio)
agregar_libro(ruta_archivo)


# Ejemplo de uso
libros = cargar_libros(ruta_archivo)
print(libros)



#Funciones para imprimir libros por categoría o estado (disponible, prestado).
def categoria(archivo):
    genero_elegido = input("¿Qué género?: ")
    genero_lista = []

    for libro in archivo:
        # Comparar el género sin utilizar strip
        if libro[2] == genero_elegido:
            genero_lista.append(libro)
    
    return genero_lista

archivos = categoria(libros)
print(archivos)


def autor(archivo):
    autor_elegido = input("¿Qué autor?: ")
    autor_lista = []

    for libro in archivo:
        # Comparar el género sin utilizar strip
        if libro[1] == autor_elegido:
            autor_lista.append(libro)
    
    return autor_lista

archivos = autor(libros)
print(archivos)

#Consultas para retornar la cantidad de libros por género o la cantidad total de libros.



#Consultas para retornar listas de libros de un autor dado.


#Consultas booleanas para verificar la existencia de un libro en la biblioteca.


#Retornar el libro con la mayor y menor cantidad de ejemplares.


#Retornar el promedio de ejemplares existentes en la biblioteca.