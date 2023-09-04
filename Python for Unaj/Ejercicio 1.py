
#codigo de propiedad
#tipo (casa, departamentos, local, terreno)
#operacion (venta, alquiler permanente, alquiler temporario)
#operador (inmobiliaria, dueño)
#precio
#metros totales
#metros cubiertos
#antiguedad
#zona (centro, barrio, suburbana)

propiedades = []

def ingresar_propiedad():
    codigo = input("Ingrese el codigo de la propiedad (0 para salir): ")
    if codigo == "0":
        return None

    tipo = input("Ingrese el tipo de propiedad (casa, departamento, local, terreno): ")
    operacion = input("Ingrese la operación (venta, alquiler permanente, alquiler temporario): ")
    operador = input("Ingrese el operador (inmobiliaria, dueño): ")
    precio = float(input("Ingrese el precio: "))
    metros_total = float(input("Ingrese los metros totales: "))
    metros_cubiertos = float(input("Ingrese los metros cubiertos: "))
    antiguedad = int(input("Ingrese la antigüedad en años: "))
    zona = input("Ingrese la zona (centro, barrio, suburbana): ")

    propiedad = {
        "Codigo": codigo,
        "Tipo": tipo,
        "Operacion": operacion,
        "Operador": operador,
        "Precio": precio,
        "Metros Total": metros_total,
        "Metros Cubiertos": metros_cubiertos,
        "Antiguedad": antiguedad,
        "Zona": zona
    }

    return propiedad

# Ingresar las propiedades hasta que el usuario ingrese '0'
while True:
    nueva_propiedad = ingresar_propiedad()
    if nueva_propiedad is None:
        break
    propiedades.append(nueva_propiedad)

# Mostrar las propiedades ingresadas
print("Propiedades ingresadas:")
for propiedad in propiedades:
    print(propiedad)


def mostrar_menu_principal():
    print("Menú Principal:")
    print("1. Mostrar la propiedad más cara en venta cuyo tipo de propiedad sea ingresada por el usuario.")
    print("2. Mostrar un listado con cada zona y la cantidad de propiedades en venta, en alquiler permanente y temporario, que posee.")
    print("3. Mostar los locales en alquiler permanente que se encuentren en el centro o barrio y que lo alquilan dueños.")
    print("4. Mostrar el promedio de precios de un determinado tipo de propiedad y una determinada zona. Datos solicitados al usuario")
    print("5. Salir")

def mostrar_menu_opcion1():
    print("hola1")
    print("hoasddsa1")

def mostrar_menu_opcion2():
    print("hola2")

def mostrar_menu_opcion3():
    print("aa")

def mostrar_menu_opcion4():
    print("aaa")

def main():
    while True:
        mostrar_menu_principal()
        opcion_principal = input("Ingrese una opción: ")

        if opcion_principal == "1":
            while True:
                mostrar_menu_opcion1()
            
        elif opcion_principal == "2":
            while True:
                mostrar_menu_opcion2()

        elif opcion_principal == "3":
            while True:
                mostrar_menu_opcion3()

        elif opcion_principal == "4":
            while True:
                mostrar_menu_opcion4()

        elif opcion_principal == "5":
            break #volver al menu principal
        else:
            print("Opcion no valida")

if __name__ == "__main__":
    main()