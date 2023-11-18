#Sistema de Gestión de Libros en una Biblioteca:



#Cargar y guardar datos de libros en un archivo.
def cargar_libros(archivo):
    libros = []
    with open(archivo, 'r') as file:
        #'r' (read): Este modo se utiliza para abrir un archivo en modo de solo lectura.     
            for line in file:
                # Separar cada línea en una lista de valores y agregar a la lista de libros
                libros.append(line.strip().split(','))
    return libros


def agregar_libro(archivo):
    with open(archivo, 'a') as file:
        #'a' (append): Este modo se utiliza para abrir un archivo en modo de escritura , pero agrega datos al final sin eliminar el contenido del mismo.
           
        # Solicitar datos al usuario
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
                file.write(titulo + ', ' + autor + ', ' + genero + ', ' + estado + ', ' + cantidad + '\n')
                print("Libro agregado exitosamente.")



# Ejemplo de uso
ruta_archivo = 'datos.txt'
agregar_libro(ruta_archivo)


# Ejemplo de uso
libros = cargar_libros(ruta_archivo)
print(libros)






#Funciones para imprimir libros por categoría o estado (disponible, prestado).



#Consultas para retornar la cantidad de libros por género o la cantidad total de libros.



#Consultas para retornar listas de libros de un autor dado.


#Consultas booleanas para verificar la existencia de un libro en la biblioteca.


#Retornar el libro con la mayor y menor cantidad de ejemplares.


#Retornar el promedio de ejemplares existentes en la biblioteca.