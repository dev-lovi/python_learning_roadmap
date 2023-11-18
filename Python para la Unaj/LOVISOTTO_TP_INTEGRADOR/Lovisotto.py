#Sistema de Gestión de Libros en una Biblioteca:

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
                autor = input("Ingrese el nombre del autor: ").capitalize()
                genero = input("Ingrese el género del libro: ").capitalize()
                estado = input("Ingrese el estado del libro (Disponible/Prestado): ").capitalize()
                n_inventario = input("Ingrese el N° de inventario en el formato XXXX: ")

            # Escribir los datos en el archivo
                file.write(titulo + ',' + autor + ',' + genero + ',' + estado + ',' + n_inventario + '\n')
                print("Libro agregado exitosamente.")


# Ejemplo de uso
#libros = cargar_libros(ruta_archivo)
#print(libros)

# PUNTO 2. Incluir funciones que realicen una tarea
#Imprimir libros prestados/disponible 
def estado(archivo):
    estado_elegido = input("¿Qué estado desea consultar? (Disponible/Prestado): ").capitalize()
    estado_lista = []

    for libro in archivo:
        if libro[3] == estado_elegido:
            estado_dato = [libro[0],libro[4]]
            estado_lista.append(estado_dato)
    if not estado_lista:
        print("No se encuentra en los documentos.")                
    return estado_lista

#archivos = estado(libros)
#print(archivos)

# PUNTO 2. Incluir funciones que realicen una tarea
#Funciones para imprimir libros por N° de articulo.
def articulo(archivo):
    articulo_elegido = input("¿Qué N° de articulo? Formato XXXX: ")
    articulo_lista = []

    for libro in archivo:
        if libro[4] == articulo_elegido:
            articulo_lista.append(libro)
    if not articulo_lista:
        print("No se encuentra en los documentos.")                
    return articulo_lista

#archivos = articulo(libros)
#print(archivos)


# PUNTO 3. Incluir consultas que retornen valores
#Devuelve el total de libros almacenados
def total_libros(archivo):
    total = 0
    for libro in archivo:
        total += 1
    rta = str("El total de libros es " + str(total))
    return rta
#archivos = total_libros(libros)
#print(archivos)


# PUNTO 4. Incluir consultas que retornen listas
#Consultas para retornar la cantidad de libros por nombre.
def cantidad_nombre(archivo):
    libro_elegido = input("Ingrese el nombre del libro: ")
    libro_lista = []

    for libro in archivo:
        if libro[0] == libro_elegido:
            libros_dato =  [libro[3], libro[4]]
            libro_lista.append(libros_dato)
    if not libro_lista:
        print("No se encuentra en los documentos.")              
    
    cantidad = len(libro_lista)
    resultado = str("La cantidad es " + str(cantidad) + " , con los siguientes datos: " + str(libro_lista))
    return resultado

#archivos = cantidad_nombre(libros)
#print(archivos)


# PUNTO 4. Incluir consultas que retornen listas
#Consultas para retornar la cantidad de libros por genero.
def cantidad_genero(archivo):
    genero_elegido = input("Ingrese el genero deseado: ").capitalize()
    genero_lista = []

    for libro in archivo:
        if libro[2] == genero_elegido:
            libros_dato =  [libro[0], libro[3], libro[4]]
            genero_lista.append(libros_dato)
    if not genero_lista:
        print("No se encuentra en los documentos.")               
    
    cantidad = len(genero_lista)
    resultado = str("La cantidad es " + str(cantidad) + " , con los siguientes datos: " + str(genero_lista))
    return resultado

#archivos = cantidad_genero(libros)
#print(archivos)



# PUNTO 5. Incluir consultas que retornan un valor booleano
#Consultas booleanas para verificar la existencia de un libro en la biblioteca.
def stock(archivo):
    print("\nTenga en cuenta que:")
    print("True = disponible")
    print("False = no se encuentra disponible")
    pregunta = input("Ingrese el nombre para verificar su estado : ")

    for libro in archivo:
        estado = 'Disponible'
        #Si el libro existe y si esta disponible
        if pregunta == libro[0] and libro[3] == estado:
            return True
    # Si no se encuentra el libro o no está disponible
    return False

#archivos = stock(libros)
#print(archivos)


#Retornar el libro con la mayor cantidad de ejemplares.
def libro_max(archivo):
    conteo_libros = {} #iniciamos diccionario
    
    max_repetido = 0
    libro_mas_repetido = None
    
    for libro in archivo:
        titulo = libro[0]
        if titulo in conteo_libros:
            conteo_libros[titulo] += 1 #si ya existe, sumale 1
        else:
            conteo_libros[titulo] = 1 #si no estaba en el diccionario,agregalo
        
        if conteo_libros[titulo] > max_repetido: #si la cantidad de ese libro es mas grande que la cantidad maxima, actualiza los datos
            max_repetido = conteo_libros[titulo]
            libro_mas_repetido = titulo
    
    a = str("El libro mas repetido es " + str(libro_mas_repetido) + " con " + str(max_repetido) + " ejemplares.")
    return a


#archivos = libro_max(libros)
#print(archivos)



#Retornar el promedio de ejemplares existentes en la biblioteca.
def promedio(archivo):
    print("Tenga en cuenta que este programa solo toma en cuenta libros disponibles")
    print("No se tienen en cuenta los libros prestados")
    libro_lista = []
    pregunta = input("Ingrese el nombre para verificar su estado: ")

    for libro in archivo:
        estado = 'Disponible'
        # Si el libro existe y si está disponible
        if pregunta == libro[0] and libro[3] == estado:
            libro_lista.append(libro)

    cantidad_elegida = len(libro_lista)

    total_lista = []  # para tener un registro de TODOS los libros disponibles
    for libro in archivo:
        estado = 'Disponible'
        if libro[3] == estado:
            total_lista.append(libro)

    cantidad_total = len(total_lista)

    calculo = (cantidad_elegida * 100 ) / cantidad_total
    rta = str("El promedio  del libro " + str(pregunta) + " es de " + str(calculo) + "% con un total de " + str(cantidad_elegida) + " ejemplares.")
    return rta

#archivos = promedio(libros)
#print(archivos)



#CONSTRUCCION DEL MENU

print("Bienvenido: ")
print("Gestion de biblioteca")

menu_condicion = 'c'

while menu_condicion != 'x':
    print("\nMenu de opciones")
    print("1. Mostrar lista completa de libros")
    print("2. Agregar libros")
    print("3. Mostrar libros prestados/disponibles")
    print("4. Mostrar libros por N° de articulo")
    print("5. Ver total de libros almacenados")
    print("6. Retornar la cantidad de libros por nombre")
    print("7. Retornar la cantidad de libros por genero")
    print("8. Verificar la existencia de un libro en la biblioteca")
    print("9. Mostrar libro con mayor cantidad de ejemplares")
    print("10. Mostrar promedio de un libro")
    print("11. SALIR")
    
    #Cargar archivo
    ruta_archivo = 'datos.txt' #(un bloc de notas)
    libros = cargar_libros(ruta_archivo)
    
    pregunta = int(input("\nElija una opción: "))
    
    if pregunta == 11:
        menu_condicion = 'x'
    
    elif pregunta == 1:
        print("Opción elegida: Mostrar lista completa de libros")
        print(libros)

    elif pregunta == 2:
        print("Opción elegida: Agregar libros")
        ruta_archivo = 'datos.txt' #acá pongo el nombre del archivo que cree anteriormente (un bloc de notas vacio)
        agregar_libro(ruta_archivo)


    elif pregunta == 3:
        print("Opción elegida: Mostrar libros prestados/disponibles")
        archivos = estado(libros)
        print(archivos)

    elif pregunta == 4:
        print("Mostrar libros por N° de articulo")
        archivos = articulo(libros)
        print(archivos)

    elif pregunta == 5:
        print("Ver total de libros almacenados")
        archivos = total_libros(libros)
        print(archivos)

    elif pregunta == 6:
        print("Retornar la cantidad de libros por nombre")
        archivos = cantidad_nombre(libros)
        print(archivos)

    elif pregunta == 7:
        print("Retornar la cantidad de libros por genero")
        archivos = cantidad_genero(libros)
        print(archivos)

    elif pregunta == 8:
        print("Verificar la existencia de un libro en la biblioteca")
        archivos = stock(libros)
        print(archivos)
    
    elif pregunta == 9:
        print("Mostrar libro con mayor cantidad de ejemplares")
        archivos = libro_max(libros)
        print(archivos)
    
    elif pregunta == 10:
        print("Opción elegida: Mostrar promedio de un libro")
        archivos = promedio(libros)
        print(archivos)

