
def checkString(s):
    for i in range(len(s)-1):
        if s[i] == 'b' and s[i+1] == 'a':
            return False
    return True

s = "aaabbb"
abeforeb = checkString(s)
print(abeforeb)
