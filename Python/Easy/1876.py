
def countGoodSubstrings(s):
    output = 0
    for i in range(len(s)-2):
        unique = set(s[i:i+3])
        if len(unique) == 3:
            output += 1
    return output

s = "xyzzaz"
numGoodSubstrings = countGoodSubstrings(s)
print(numGoodSubstrings)
