import random

def crear_lista_equipos():
    equipos_personalizados = []
    cantidad_equipos = int(input("¿Cuántos equipos quieres agregar a la lista? "))
    for i in range(cantidad_equipos):
        equipo = input(f"Ingresa el nombre del equipo {i + 1}: ")
        equipos_personalizados.append(equipo)
    return equipos_personalizados

# Lista de equipos
equipos = ["Agropecuario", "Aldosivi", "All Boys", "Almagro", "Almirante Brown", "Alvarado", "Atlanta", "Atlético Rafaela", "Brown de Adrogué", "Chacarita Juniors", "Chaco For Ever", "Club Atlético Güemes", "Defensores de Belgrano", "Defensores Unidos", "Deportivo Madryn", "Deportivo Maipú", "Deportivo Morón", "Deportivo Riestra", "Estudiantes Caseros", "Estudiantes Río Cuarto", "Ferro Carril Oeste", "Flandria", "Gimnasia Jujuy", "Gimnasia Mendoza", "Guillermo Brown", "Independiente Rivadavia", "Mitre Santiago d. Estero", "Nueva Chicago", "Patronato", "Quilmes", "Racing Córdoba", "San Martín San Juan", "San Martín Tucumán", "San Telmo", "Temperley", "Tristán Suárez", "Villa Dálmine"]

# Seleccionar un equipo al azar
equipo_seleccionado = random.choice(equipos)

# Imprimir el equipo seleccionado
print("¿Estás listo para empezar?")
print("Si querés sortear equipos de la B, escribí 1")
print("Si querés hacer tu propia lista, escribí 2")
answer = input("Escribe tu respuesta: ")
if answer == "1":
    print("El equipo seleccionado al azar es:", equipo_seleccionado)
elif answer == "2":
    equipos_personalizados = crear_lista_equipos()
    if equipos_personalizados:
        equipo_seleccionado = random.choice(equipos_personalizados)
        print("El equipo seleccionado al azar de tu lista es:", equipo_seleccionado)
    else:
        print("No agregaste ningún equipo a la lista personalizada.")
else:
    print("No seleccionaste ningun equipo.")