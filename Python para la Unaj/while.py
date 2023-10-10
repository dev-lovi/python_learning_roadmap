#hacer una funcion que pida nombre y dni y lo almacene en una lista

def mi_funcion():
    print("Menu general")
    lista_nombre = []
    lista_dni = []
    lista_general = []
    a = 0
    while a == 0:
        print("1. Agregar datos")
        print("2. Mostrar lista (nombres)")
        print("3. Mostrar lista (dni)")
        print("4. Mostrar lista completa")
        print("5. Salir")
        question = int(input("Ingrese una opcion: "))

        while question == 1:
            nombre = input("Ingrese su nombre: ")
            lista_nombre.append(nombre)
            dni = input("Ingrese su DNI: ")
            lista_dni.append(dni)
            general = nombre + " " + dni
            lista_general.append(general)
            question = int(input("Continuar = 1 | Salir = 2: "))
            if question == 1:
                continue
            else:
                break
    #Tengo que seguir con esto    
        if question == 2:
            print(lista_nombre)
        elif question == 3:
            print(lista_dni)
        elif question == 4:
            print(lista_general)
        else:
            break

x = mi_funcion()
print(x)