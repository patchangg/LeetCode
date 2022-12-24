
def largeGroupPositions(s):
    i = 0
    j = 0
    output = []
    n = len(s)
    while i < n:
        while j < n and s[i] == s[j]:
            j += 1
        if j - i >= 3:
            output.append([i,j-1])
        i = j
    return output

s = "abbxxxxzzy"
largeGroupPos = largeGroupPositions(s)
print(largeGroupPos)
