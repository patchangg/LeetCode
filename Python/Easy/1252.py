
def oddCells(m, n, indices):
    output = 0
    x = [0] * m
    y = [0] * n
    for r,c in indices:
        x[r] += 1
        y[c] += 1
    for r in range(m):
        for c in range(n):
            if (x[r] + y[c]) % 2 == 1:
                output += 1
    return output

m = 2
n = 3
indices = [[0,1],[1,1]]
oddNumbers = oddCells(m,n,indices)
print(oddNumbers)
