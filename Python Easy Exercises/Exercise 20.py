#Consigna: Lista de Números Pares e Impares

#Escribe un programa en Python que genere una lista de números del 1000 al 3000, inclusive. Luego, recorre la lista y reemplaza cada número par por la palabra "Gato" y cada número impar por la palabra "Perro". Finalmente, muestra la lista resultante.

for x in range(1000, 3001):
    if x % 2 == 0:
        print("gato")
    elif x % 1 == 0:
        print("perro")
    else:
        print(x)