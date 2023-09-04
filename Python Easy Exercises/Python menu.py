    #General structure of python menu
def mostrar_menu_principal():
    print("Menú Principal:")
    print("1. Categoría 1")
    print("2. Categoría 2")
    print("3. Salir")

def mostrar_menu_categoria1():
    print("Categoría 1:")
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Volver al menú principal")

def mostrar_menu_categoria2():
    print("Categoría 2:")
    print("1. Opción A")
    print("2. Opción B")
    print("3. Volver al menú principal")

def main():
    while True:
        mostrar_menu_principal()
        opcion_principal = input("Elija una opción: ")

        if opcion_principal == "1":
            while True:
                mostrar_menu_categoria1()
                opcion_categoria1 = input("Elija una opción de Categoría 1: ")
                if opcion_categoria1 == "1":
                    # Realizar acción para la opción 1 de Categoría 1
                    print("Realizando acción para la opción 1 de Categoría 1")
                elif opcion_categoria1 == "2":
                    # Realizar acción para la opción 2 de Categoría 1
                    print("Realizando acción para la opción 2 de Categoría 1")
                elif opcion_categoria1 == "3":
                    break  # Volver al menú principal
                else:
                    print("Opción no válida. Intente de nuevo.")

        elif opcion_principal == "2":
            while True:
                mostrar_menu_categoria2()
                opcion_categoria2 = input("Elija una opción de Categoría 2: ")
                if opcion_categoria2 == "1":
                    # Realizar acción para la opción A de Categoría 2
                    print("Realizando acción para la opción A de Categoría 2")
                elif opcion_categoria2 == "2":
                    # Realizar acción para la opción B de Categoría 2
                    print("Realizando acción para la opción B de Categoría 2")
                elif opcion_categoria2 == "3":
                    break  # Volver al menú principal
                else:
                    print("Opción no válida. Intente de nuevo.")

        elif opcion_principal == "3":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
