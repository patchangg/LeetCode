
def construct2DArray(original, m, n):
    if m * n != len(original):
        return []
    output = []
    i = 0
    for r in range(m):
        col = []
        for c in range(n):
            col.append(original[i])
            i += 1
        output.append(col)
    return output

original = [1,2,3,4]
m = 2
n = 2
converted2DArray = construct2DArray(original,m,n)
print(converted2DArray)
