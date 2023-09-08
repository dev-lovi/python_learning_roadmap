import datetime
import pickle

# Función para iniciar el contador de tiempo
def iniciar_estudio():
    inicio = datetime.datetime.now()
    return inicio

# Función para detener el contador de tiempo y registrar el estudio
def detener_estudio(inicio, registro):
    fin = datetime.datetime.now()
    tiempo_estudiado = fin - inicio
    registro.append(tiempo_estudiado)
    guardar_registro(registro)

# Función para guardar el registro en un archivo
def guardar_registro(registro):
    with open('registro_estudio.pkl', 'wb') as archivo:
        pickle.dump(registro, archivo)

# Función para cargar un registro existente desde un archivo
def cargar_registro():
    try:
        with open('registro_estudio.pkl', 'rb') as archivo:
            return pickle.load(archivo)
    except FileNotFoundError:
        return []

# Programa principal
registro = cargar_registro()

while True:
    accion = input("Presiona 's' para iniciar el estudio o 'e' para detenerlo ('q' para salir): ")
    
    if accion == 's':
        inicio_estudio = iniciar_estudio()
        print("Estudio iniciado.")
    elif accion == 'e':
        if 'inicio_estudio' in locals():
            detener_estudio(inicio_estudio, registro)
            print("Estudio detenido.")
        else:
            print("Primero debes iniciar el estudio con 's'.")
    elif accion == 'q':
        break
    else:
        print("Comando no reconocido.")

print("Registro anual de estudio:")
total_estudiado = sum(registro, datetime.timedelta())
print(f"Tiempo total de estudio: {total_estudiado}")
