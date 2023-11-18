

def ingreso_info (lista):

	puntos = "none"
	equipo = "none"
	while puntos != 0 and equipo !="A":
		equipo =  input("Ingrese el nombre del equipo o A para salir :")
		puntos = int (input("Ingrese un numero o 0 para salir :"))
		if puntos !=0 and equipo !="A":
			lista.append ((equipo,puntos))
	 	
	return 	(lista)


def tabla(lista_numeros):
	lista_ordenada = []
	
	while lista_numeros: #recorre la lista hasta quedar vacia (por eso al final removemos valores de la lista original)
		max_puntaje = -1
		max_equipo = None

		for x in lista_numeros:
			if x[1] > max_puntaje: #x[1] es el puntaje
				max_puntaje = x[1]
				max_equipo = x[0] #x[0] es el equipo
			
		lista_ordenada.append((max_equipo, max_puntaje))
		lista_numeros.remove((max_equipo, max_puntaje)) #los va sacando porque si no el while seria infinito
    
	return lista_ordenada

#def suma (lista_numeros):
#	a=sum (lista_numeros)
#	return (a)	
	
	
	
def maximo(lista_numeros):
	lista = []
	valor_max = 0
	equipo_max= ""
	for x in lista_numeros:
		if x[1] > valor_max:
			valor_max = x[1]
			equipo_max = x[0]
	z = (equipo_max, valor_max)		
	lista.append (z)	
			
	return (lista) 	
	
		
	
def minimo(lista_numeros):
	lista = []
	valor_min =  0
	equipo_min= ""
	valor_max = 0
	
	for x in lista_numeros:
		if x[1] > valor_max:
			valor_max = x[1]
			equipo_max = x[0]
			
	for x in lista_numeros:
		if x[1] < valor_max:
			equipo_min = x[0]
			valor_min = x[1]
			
	z = (equipo_min, valor_min)		
	lista.append (z)	
			
	return (lista) 	

	
def promedio (lista):
	
	total = 0 
	valor = 0
	x = lista[0][1]
	for x in lista :
		total+=1
	for x in lista :
		valor+= x[1]		
	a=(valor/total)
	return (a)		
	

numero="none"

a=[]	
b= ingreso_info (a)	
print 	(b)
									
print ("1_Ver el promedio de todos los equipós")
print ("2_Ver la tabla de la liga")
#print ("3_Ver la cantidad de números")
print ("4_Ver el equipo con mas puntos")
print ("5_Ver el equipo con menos puntos")
#print ("6_Calcular porcentaje")
print ("7_Salir")

while numero != 7 :
	
	numero = int(input("seleccione una opcion:"))
	if numero == 1 :					
		print ("el promedio de los numeros que usted agrego es:",promedio(a))
	elif numero == 2 :
		print ("la tabla de la liga es la siguiente:",tabla(a))
#	elif numero == 3 :
#		cantidad=len (a)
#		print ("la cantidad de numeros que agrego es:",(cantidad))
	elif numero == 4 :	
		print ("el equipo con mas puntos es:",maximo(a))
	elif numero ==	5:
		print ("el equipo con menos puntos es :",minimo(a))
#	elif numero == 6:
#		print ("el porcentaje de su lista es :",(promedio(a))*100)
#	elif numero ==7:
#		print("usted salio del sitema ")	
#	else:
#		("selecciono un numero incorrecto")	
			
