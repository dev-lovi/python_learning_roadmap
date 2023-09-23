#Ejercicio 15: Definir una función llamada calculo_dosis que reciba tres números. Uno para
#la cantidad de días que debe suministrarse el remedio, el segundo dato para la cantidad de
#veces por día que debe tomarlo, y el último dato para la cantidad de comprimidos que trae el
#envase. La función debe devolver verdadero si el envase alcanza para ese tratamiento y
#falso si no alcanza.

def calculo_dosis(dias, veces, cantidad):
    total = dias * veces
    if total <= cantidad:
        return True
    else:
        return False

print(calculo_dosis(4, 2, 20))
print(calculo_dosis(6, 4, 18))