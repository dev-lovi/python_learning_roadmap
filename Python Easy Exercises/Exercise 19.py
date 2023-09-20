#La consigna del ejercicio es la siguiente: 
#Escribir un programa que imprima los números del 1 al 100, pero para múltiplos de tres imprimir 'Fizz' en lugar del número y para los múltiplos de cinco imprimir 'Buzz'. Para los números que son múltiplos tanto de tres como de cinco imprimir "FizzBuzz" 

for a in range(1, 101):
    if a % 5 == 0 and a % 3 == 0:
        print("FizzBuzz")
    elif a % 3 == 0:
        print("Fizz")
    elif a % 5 == 0:
        print("Buzz")
    else:
        print(a)



        