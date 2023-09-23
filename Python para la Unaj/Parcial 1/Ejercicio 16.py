#Ejercicio 16: Definir una función llamada precio_con_iva que agrega el IVA (21%) de un
#producto dado su precio de venta sin IVA.

def precio_con_iva(precio):
    cuenta = precio * 1.21
    print("El precio del producto SIN IVA (21%) agregado es de $" + str(precio))
    print("El precio del producto CON IVA (21%) agregado es de $" + str(cuenta))
precio_con_iva(200)
precio_con_iva(50)
precio_con_iva(100)