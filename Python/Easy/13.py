
def romanToInt(s):
    rnums = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    prev = 0
    output = 0
    for c in s[::-1]:
        curr = rnums[c]
        if prev > curr:
            output -= curr
        else:
            output += curr
        prev = curr
    return output

s = "III"
rToI = romanToInt(s)
print(rToI)
