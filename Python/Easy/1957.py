
def makeFancyString(s):
    s = list(s)
    for i in range(len(s)-2):
        if s[i] == s[i+1] == s[i+2]:
            s[i] = ""
    return "".join(s)

s = "leeetcode"
fancyString = makeFancyString(s)
print(fancyString)
