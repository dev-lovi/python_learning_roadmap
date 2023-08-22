#Python en la facu, clase 1

nombre = input('Decime tu nombre: ')
if nombre == ('Santiago'):
    print('Te detecta el sistema')
elif nombre == ('santiago'):
    print('Te detecta el sistema')
else:
    print('No te detecta el sistema, registrando...')

edad = int(input('¿Cuántos años tenés?: '))
if edad > 18:
    print('Sos mayor de edad')
else:
    print('Sos menor de edad')
    quit()

dni = input('Ingrese su DNI: ')
print('Tu DNI es ' + dni)
pregunta = input('¿Correcto? ')
if pregunta == 'Si':
    print('Ingreso al sistema')
elif pregunta == 'Sí':
    print('Ingreso al sistema')
elif pregunta == 'si':
    print('Ingreso al sistema')
elif pregunta == 'sí':
    print('Ingreso al sistema')
else:
    print('ERROR 404')

