
def getLucky(s, k):
    output = ""
    for c in s:
        output += str(ord(c) - ord('a') + 1)
    for i in range(k):
        trans = 0
        for c in str(output):
            trans += int(c)
        output = trans
    return output

s = "iiii"
k = 1
numAfterConverting = getLucky(s,k)
print(numAfterConverting)
