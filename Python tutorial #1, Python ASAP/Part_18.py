    #Functions
#def means define
def func():
    print('Run')

func()

def func(x, y):
    print('Jump', x, y)
    return x * y, x / y
print(func(10, 5))

def func(x, y):
    print('Lovinho', x, y)
    return x * y, x / y

r1, r2= func(20, 2)
print(r1, r2)

def func(x, y, z=None):
    print('Lovin', x, y, z)
    return x * y, x / y

r1, r2= func(20, 2, 9)
print(r1, r2)