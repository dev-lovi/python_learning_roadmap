def cargar_datos(valor_lista):
    #valor_lista = []

    condicion = 'a'
    while condicion != 'FIN':
        legajo = int(input("Ingrese su legajo: "))
        nombre = (input("Ingrese su nombre: "))
        apellido = (input("Ingrese su apellido, 'FIN' para salir: "))
        if apellido == 'FIN':
            condicion = 'FIN'
        else:
            sexo = (input("Ingrese sexo: "))
            antiguedad = int(input("Ingrese su antiguedad: "))
            print("Categorias: maestranza, técnico, ventas, administrativo o auxiliar")
            categoria = (input("Ingrese su categoria: "))
            sueldo = float(input("Ingrese su sueldo: "))
            num_sucursal = int(input("Ingrese el numero de la sucursal donde trabaja: "))
            empleados = [legajo, nombre, apellido, sexo, antiguedad, categoria, sueldo, num_sucursal]
            valor_lista.append(empleados)

    return valor_lista

x = []
a = cargar_datos(x)
print(a)


def cant_total(valor_lista):
    total = len(valor_lista)
    return total


#a = cant_total(x)
#print(a)


def cant_hombres(valor_lista):
    hombres = 0
    mujeres = 0
    no = 0
    total = len(valor_lista)


    for empleados in valor_lista:
        if empleados[3].upper() == 'H':
            hombres += 1
        elif empleados[3].upper() == 'F':
            mujeres += 1
        else:
            no += 1

    promedio_hombres = (hombres / total) * 100
    promedio_mujeres = (mujeres / total) * 100
    promedio_no = (no / total) * 100
    
    total = ('El promedio de hombres es ' + str(promedio_hombres) + " el de mujeres " + str(promedio_mujeres) + " y el de no binario es " + str(promedio_no))

    return total


a = cant_hombres(x)
print(a)