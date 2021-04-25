
def diagonalSum(mat):
    lenx = len(mat)
    leny = len(mat[0]) - 1
    i = 0
    sum = 0
    while i < lenx:
        sum += mat[i][i]
        mat[i][i] = 0
        sum += mat[i][leny]
        mat[i][leny] = 0
        leny -= 1
        i += 1
    return sum

#mat = [[1,2,3],[4,5,6],[7,8,9]]
mat = [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]
sum = diagonalSum(mat)
print(sum)
