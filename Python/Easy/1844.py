
def replaceDigits(s):
    s = list(s)
    for i in range(1,len(s),2):
        s[i] = chr(ord(s[i-1])+int(s[i]))
    return "".join(s)

s = "a1c1e1"
string = replaceDigits(s)
print(string)
