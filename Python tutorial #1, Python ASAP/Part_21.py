    #Map and Filter
x = [123,345,5462,134,12,3,5,5,34125,43,54,53,765]

mp = map(lambda i: i + 2, x)
print(list(mp))


#Para que me ordene los pares
x = list(range(1,101))

mp = filter(lambda i: i % 2 == 0, x)
print(list(mp))

#Para que me ordene los impares
mp = filter(lambda i: i % 2 == 1, x)
print(list(mp))


