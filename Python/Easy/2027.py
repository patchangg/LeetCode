
def minimumMoves(s):
    output = 0
    i = 0
    while i <= len(s) - 1:
        if s[i] == "X":
            output += 1
            i += 3
        else:
            i += 1
    return output

s = "XXX"
minMoves = minimumMoves(s)
print(minMoves)
