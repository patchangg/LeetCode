
def countBinarySubstrings(s):
    curr = s[0]
    consec = 1
    groups = []
    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            consec += 1
        else:
            groups.append(consec)
            consec = 1
            curr = s[i]
    groups.append(consec)
    output = 0
    for i in range(1, len(groups)):
        output += min(groups[i],groups[i-1])
    return output

s = "00110011"
numBinarySubstrings = countBinarySubstrings(s)
print(numBinarySubstrings)
