    #STRING METHODS
hello = 'hello'
print(type(hello))

#knowing that 'hello' is a string, we can use comands like the following:
hello = 'hello'.upper()
print(hello)

#or we can do this, is the same

hello = 'hello'
print(hello.upper())

#we also can...

hello = 'hello students'
print(hello.count('e'))

#or...

hello = 'hEllo studEntS'
print(hello.lower().count('e'))