#1)

def hechoshistoricos():
    lista = []
    
    
    nombre = input("Ingrese el nombre, 'zzz' para salir: ")  #condicion
    
    while nombre != 'zzz':
       año = int(input('Ingrese el año del hecho: ')) 
       abreviacion = input('Ingrese la abreviacion del hecho: ')
       
       todo = [nombre,año,abreviacion]

       lista.append(todo)  

       nombre = input("Ingrese el nombre, 'zzz' para salir: ")  #condicion
    
    return lista

a = hechoshistoricos()
#print(a)






#2)

def incialhecho(lista,letra):
    lista2 = []
    
    for x in lista:
        if x[0][0] == letra: #los input afuera
            lista2.append(x)
    
    return lista2




let = input('Ingrese una letra: ')

b = incialhecho(a,let)
print(b)








#3)

def fechahecho(lista,fecha):
    lista3 = []
    
    for x in lista:
        if x[1] > fecha:
            lista3.append(x)
    
    return lista3



fec = int(input('Ingrese un año: '))
c = fechahecho(a,fec)
print(c)


