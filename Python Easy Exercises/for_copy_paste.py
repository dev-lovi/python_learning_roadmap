import os
import shutil

# Carpeta de origen (donde están los archivos que deseas copiar)
carpeta_origen = "python_learning_roadmap\Python para la Unaj\Parcial 1"

# Archivo de destino (donde se copiarán todos los archivos)
archivo_destino = "python_learning_roadmap\Nueva carpeta/destino.txt"

# Abre el archivo de destino en modo de escritura
with open(archivo_destino, 'wb') as destino:
    # Itera a través de los archivos en la carpeta de origen
    for carpeta_raiz, _, archivos in os.walk(carpeta_origen):
        for archivo in archivos:
            ruta_completa = os.path.join(carpeta_raiz, archivo)
            
            # Copia el contenido de cada archivo al archivo de destino
            with open(ruta_completa, 'rb') as origen:
                shutil.copyfileobj(origen, destino)

print("Archivos copiados con éxito en", archivo_destino)
