    #Comprenhensions
x = [x for x in range(5)]
print(x)

x = [x + 5 for x in range(5)]
print(x)

x = [[0 for x in range(20)] for x in range(3)]
print(x)

x = [i for i in range(100) if i % 5==0]
print(x)

#For Dictionaries
x = {i:0 for i in range(100) if i % 5==0}
print(x)

#For a Set
x = {i for i in range(100) if i % 5==0}
print(x)
