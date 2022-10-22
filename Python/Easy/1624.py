
def maxLengthBetweenEqualCharacters(s):
    pos = {}
    output = -1
    for i, c in enumerate(s):
        if c not in pos:
            pos[c] = [i]
        else:
            pos[c].append(i)
    for i in pos:
        if len(pos[i]) > 1:
            output = max(output, pos[i][-1] - pos[i][0] - 1)
    return output

s = "aa"
maxLenBetweenChars = maxLengthBetweenEqualCharacters(s)
print(maxLenBetweenChars)
