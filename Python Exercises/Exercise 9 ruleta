import random

def crear_lista_equipos():
    equipos_personalizados = []
    cantidad_equipos = int(input("¿Cuantos items queres agregar a la ruleta? "))
    for i in range(cantidad_equipos):
        equipo = input(f"Ingresa el nombre del item {i + 1}: ")
        equipos_personalizados.append(equipo)
    return equipos_personalizados


# Imprimir el equipo seleccionado
print("Ruleta personalizada")

equipos_personalizados = crear_lista_equipos()
if equipos_personalizados:
    equipo_seleccionado = random.choice(equipos_personalizados)
    print("La ruleta eligió:", equipo_seleccionado)
else:
     print("Error, vuelve a intentarlo.")
