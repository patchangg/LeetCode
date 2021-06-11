
def restoreMatrix(rowSum, colSum):
    m = len(rowSum)
    n = len(colSum)
    output = [[0] * n for i in range(m)]
    for i in range(m):
        for j in range(n):
            output[i][j] = min(rowSum[i],colSum[j])
            rowSum[i] -= output[i][j]
            colSum[j] -= output[i][j]
    return output

rowSum = [5,7,10]
colSum = [8,6,8]
matrixed = restoreMatrix(rowSum,colSum)
print(matrixed)
