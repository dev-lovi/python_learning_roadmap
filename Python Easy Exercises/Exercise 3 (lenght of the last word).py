    #Length of Last Word
#Given a string s consisting of words and spaces, 
#return the length of the last word in the string.

    #Example 1:
#Input: s = "Hello World"
#Output: 5
#Explanation: The last word is "World" with length 5.

    #Example 2:
#Input: s = "   fly me   to   the moon  "
#Output: 4
#Explanation: The last word is "moon" with length 4.

    #Example 3:
#Input: s = "luffy is still joyboy"
#Output: 6
#Explanation: The last word is "joyboy" with length 6.




def largo_de_la_ultima_palabra(s):
    palabras = s.split()

    if len(palabras) == 0:
        return 0
    
    ultima_palabra = palabras[-1]
    return len(ultima_palabra)

xd = input('Escribí una frase: ')

resultado = largo_de_la_ultima_palabra(xd)

print("La longitud de la última palabra es:", resultado)
