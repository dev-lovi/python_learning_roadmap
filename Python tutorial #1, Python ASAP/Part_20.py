 #Scope and Global
x = 'Tim'

def func(name):
    global x
    x = name

print(x)
func('changed')
print(x)

    #Exceptions
#raise Exception('Bad')

    #Handling exceptions
try:
    x = 7 / 0
except Exception as e:
    print(e)
    
    #Lambda
x = lambda x: x + 5

print(x(2))

