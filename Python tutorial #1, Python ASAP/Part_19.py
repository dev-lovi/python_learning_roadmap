 #Unpack operator / *Args and *Kwargs

#*args (Non-Keyword Arguments)
#**kwargs (Keyword Arguments)

def func(x):
    def func2():
        print(x)
    
    return func2
#notice I returned funct2 but I didnt call it
print(func(3))
print(func(3)())
func(3)()




def func(*args, **kwargs):
    pass 

x = [23,12312,123,56,43]
print(x)
print(*x)



def func(x, y):
    print(x, y)

pairs = [(1,2), (3,4)]
for pair in pairs:
    func(*pair)


    #For dictionaries
def func(x, y):
    print(x, y)

func(**{'x': 2,'y': 5})



def func(*args, **kwargs):
    print(args, kwargs)

func(1,2,3,4,5,one=0, two=1)


