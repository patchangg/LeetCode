address = "1.1.1.1"
def defangIPaddr(address):
    s = ""
    for i in address:
        if i != ".":
            s = s + i
        else:
            s += "[.]"
        print(s)
defangIPaddr(address)
