def datoscorreo():
    lista = []
    print("Cuando ingrese fin se cierra el programa")
    destinatario = input("Ingrese destinatario: ")
    finaliza = "fin"
    while destinatario != finaliza:
        remitente = input("Ingrese remitente: ")
        cp = int(input("Ingrese cp de entrega: "))
        peso = float(input("Ingrese peso del paquete: "))
        paquete = [remitente,destinatario,cp,peso]
        lista.append(paquete)
        destinatario = input("Ingrese destinatario: ")
    return lista

x = datoscorreo()
print(x)


def maspeso(a):
    maspeso = a[0]
    for paquete in a:
        if paquete[3] > maspeso [3]:
            maspeso = paquete
    print(maspeso)



maspeso(x)