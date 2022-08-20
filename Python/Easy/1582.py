
def numSpecial(mat):
    row = [0] * len(mat)
    col = [0] * len(mat[0])
    output = 0
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 1:
                row[i] += 1
                col[j] += 1
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 1 and row[i] == 1 and col[j] == 1:
                output += 1
    return output

mat = [[1,0,0],[0,0,1],[1,0,0]]
specialPositions = numSpecial(mat)
print(specialPositions)
