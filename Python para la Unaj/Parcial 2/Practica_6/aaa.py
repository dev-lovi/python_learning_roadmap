def datoscorreo():
    lista = []
    destinatario = input("Ingrese destinatario, ponga 'fin' para salir: ") #condicion
    while destinatario != 'fin': #ingreso al bucle
        remitente = input("Ingrese remitente: ")
        cp = int(input("Ingrese cp de entrega: "))
        peso = float(input("Ingrese peso del paquete: "))
        paquete = [remitente,destinatario,cp,peso]
        lista.append(paquete)
        destinatario = input("Ingrese destinatario, ponga 'fin' para salir: ") #repito la condicion
    return lista

x = datoscorreo()
print(x)


def maspeso(a):
    maspeso = a[0]
    for paquete in a:
        if paquete[3] > maspeso [3]:
            maspeso = paquete
    print(maspeso)



#maspeso(x)