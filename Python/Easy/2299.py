
def strongPasswordCheckerII(password):
    if len(password) < 8:
        return False

    seen = set()

    for i in range(len(password)):
        if i > 0 and password[i] == password[i-1]:
            return False
        if password[i].islower():
            seen.add("l")
        elif password[i].isupper():
            seen.add("u")
        elif password[i].isdigit():
            seen.add("d")
        else:
            seen.add("s")

    return len(seen) == 4

password = "IloveLe3tcode!"
isStrongPassword = strongPasswordCheckerII(password)
print(isStrongPassword)
