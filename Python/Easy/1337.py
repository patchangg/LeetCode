
def kWeakestRows(mat, k):
    numSol = []
    for i in range(len(mat)):
        sum = mat[i].count(1)
        numSol.append([sum,i])
    numSol.sort()
    output = []
    for s in range(k):
        output.append(numSol[s][1])
    return output




mat = [[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]]
k = 3
kWeakest = kWeakestRows(mat,k)
print(kWeakest)
