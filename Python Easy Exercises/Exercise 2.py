#Write a program that counts the number of vowels (A, E, I, O, U) 
#in a given sentence or phrase.

frase = input('Poné una frase: ')

cant_vocales = 0

for letra in frase:
    if letra.upper() in "AEIOU":
        cant_vocales += 1

print('El número de vocales en la oración es: ', cant_vocales)