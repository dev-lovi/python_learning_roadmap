#Escriba un programa que solicite códigos postales de localidades e imprima si esa localidad es La Plata, Florencio Varela u otra. Recordar que el código postal de La Plata es 1900 y el de Florencia Varela es: 1887. El programa termina cuando se ingresa el código postal 0

codigo = 1
while codigo != 0:
    codigo = int(input("Ingresa tu CP, pone '0' para salir: "))
    if codigo == 1900:
        print("Sos de la plata perro, aguante Varela y DyJ.")
    elif codigo == 1887:
        print("Vos sabes turro.")
    elif codigo == 0:
        break
    else:
        print("No se encontró localidad.")
