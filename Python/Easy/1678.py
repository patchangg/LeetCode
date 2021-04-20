
def interpret(command):
    i = len(command)
    s = 0
    string = ""
    while s < i:
        if command[s] == "G":
            string += "G"
            s += 1
        elif command[s] == "(":
            if command[s+1] == "a":
                string += "al"
                s += 4
            else:
                string += "o"
                s += 2
    return string

command = "(al)G(al)()()G"
parsed = interpret(command)
print(parsed)
