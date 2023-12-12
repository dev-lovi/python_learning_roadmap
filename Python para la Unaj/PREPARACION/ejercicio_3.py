'''
Realice el siguiente programa que presenta un menú con opciones sobre los países y sus
restricciones de ingreso por el tema de la pandemia. El programa debe permitir la carga de la información sobre una cantidad de PAISES, con  información sobre el nombre del país, idioma, moneda, tipo de Restricción (que puede ser verde, amarillo o rojo). La cantidad de países la ingresa el usuario.

Respecto a los tipos de restricciones que hay para el ingreso a los países, éstas pueden
ser:
Verde: las fronteras están abiertas, no hay restricciones ni requisitos para la mayoría de
los viajeros en este momento.

Amarillo: las fronteras están abiertas, pero con restricciones. Piden vacunación completa o resultado negativo del hisopado.

Rojo: las fronteras están cerradas. Solo ciudadanos y residentes pueden ingresar.

Armar la lista de PAÍSES y otra lista de RESTRICCIONES que tenga la información anterior
(color y descripción).

Luego, el programa debe mostrar en forma permanente, el siguiente menú, donde TODAS
las opciones deben ser realizadas mediante FUNCIONES:
Menú de opciones:
1. Mostrar la descripción de un tipo de restricción determinada (ingresada por el usuario) con los países que la acatan.
2. Mostrar la descripción del tipo de restricción que acata un país determinado
(ingresado por el usuario).
3. Mostrar el porcentaje de países de ingreso abierto (con tipo de restricción en Verde),
respecto del total.
4. Salir
'''



def carga_paises():
    lista = []

    nombre = input("Ingrese el nombre del país, 'fin' para salir: ")

    while nombre != 'fin':
        idioma = input("Ingrese el idioma: ")
        moneda = input("Ingrese la moneda: ")
        restricción = input("Ingrese la restricción (Verde, Amarillo o Rojo): ").lower()
        total = [nombre, idioma, moneda, restricción]

        lista.append(total)
        nombre = input("Ingrese el nombre del país, 'fin' para salir: ")

    return lista

a = carga_paises()
#print(a)




def lista_restricciones():
    lista = []

    verde = 'Las fronteras están abiertas, no hay restricciones ni requisitos para la mayoría de los viajeros en este momento.'
    amarillo = 'Las fronteras están abiertas, pero con restricciones. Piden vacunación completa o resultado negativo del hisopado.'
    rojo = 'Las fronteras están cerradas. Solo ciudadanos y residentes pueden ingresar.'

    total = [verde, amarillo, rojo]
    lista.append(total)

    return lista

b = lista_restricciones()



#funcion 1
def datos_restriccion(lista, input_usuario, lista_condiciones):
    lista_paises = []

    #para agregar la descripcion
    for condiciones in lista_condiciones:
        if input_usuario == 'verde':
            print(condiciones[0])
        elif input_usuario == 'amarillo':
            print(condiciones[1])
        elif input_usuario == 'rojo':
            print(condiciones[2])

    for paises in lista:
        if input_usuario == paises[3]:
           lista_paises.append(paises)
        elif input_usuario == paises[3]:
            lista_paises.append(paises)
        elif input_usuario == paises[3]:
            lista_paises.append(paises)

    return lista_paises

x = input("Ingrese la restricción (Verde, Amarillo o Rojo): ").lower()
c = datos_restriccion(a, x, b)
print(c)

#a => lista principal
#b => condiciones




#funcion 2
def descripcion_por_pais(lista, input_usuario, lista_condiciones):

    for paises in lista:
        if paises[0] == input_usuario:
            valor = paises[3]


    for condiciones in lista_condiciones:
        if valor == 'verde':
            a = condiciones[0]
        elif valor == 'amarillo':
            a = condiciones[1]
        elif valor == 'rojo':
            a = condiciones[2]

    return a

pregunta = input("Ingrese el nombre del país: ")
d = descripcion_por_pais(a, pregunta, b)
print(d)

#a => lista principal
#b => condiciones




#funcion 3
def paises_ingreso_abierto(lista):

    cantidad_general = 0
    cantidad_condicion = 0

    for paises in lista:
        cantidad_general += 1
        if paises[3] == 'verde':
            cantidad_condicion += 1
            
    #por regla de 3 simple
    calculo = (cantidad_condicion * 100) / cantidad_general

    return calculo

e = paises_ingreso_abierto(a)
print(e)