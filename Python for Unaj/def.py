#vimos funciones en clase y sus usos

#ejemplo
def suma():
    precio = 10
    cantidad = 5
    costo = precio * cantidad
    return costo
print(suma()) #me imprime 50

#ejemplo 2
def suma(precio, cantidad):
    costo = precio * cantidad
    return costo
x = 20
y = 3
print(suma(x, y)) #me imprime 60

#ejemplo 3
def perimetro(alto, ancho):
    p = 2*alto + 2*ancho
    return p
a = 3
b = 5
print(perimetro(b, a)) #me imprime 16

