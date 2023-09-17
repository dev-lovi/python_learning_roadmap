#password generator

import random
import string

length = int(input("Length of the password: "))
upper_c = int(input("How many uppercase characters?: "))
lower_c = int(input("How many lowercase characters?: "))
digits_c = int(input("How many numbers?: "))
special_c = int(input("How many special characters?: "))

if upper_c + lower_c + digits_c + special_c > length:
    print("Character counts exceed the password length.")
else:
    # Create a list of characters based on user input
    chars = []
    chars += random.choices(string.ascii_uppercase, k=upper_c)
    chars += random.choices(string.ascii_lowercase, k=lower_c)
    chars += random.choices(string.digits, k=digits_c)
    chars += random.choices(string.punctuation, k=special_c)

random.shuffle(chars)
password = ''.join(chars)
print(password)