#Password strength checker

def password_checker(password):
    if len(password) < 8:
        return "Weak: password should contain at least 8 characters"
    if not any(c.isupper() for c in password) or not any(c.islower() for c in password):
        return "Weak: Password should contain both uppercase and lowercase characters."
    special = "!#$%&/()=?¡¿}+'"
    if not any(c in special for c in password):
        return "Weak: Password should contain at least 1 special character."
    else:
        return "Strong: Password meets basic security criteria."

while True:
    password = str(input("Enter your password: "))
    result = password_checker(password)
    print(result)
    if "Strong" in result:
        break