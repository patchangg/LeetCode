
def spiralOrder(matrix):
    output = []
    rStart = 0
    cStart = 0
    rEnd = len(matrix) - 1
    cEnd = len(matrix[0]) - 1

    while rStart <= rEnd and cStart <= cEnd:

        for r in range(cStart,cEnd+1):
            output.append(matrix[rStart][r])
        rStart += 1

        for d in range(rStart,rEnd+1):
            output.append(matrix[d][cEnd])
        cEnd -= 1

        if rStart <= rEnd:
            for l in range(cEnd,cStart-1,-1):
                output.append(matrix[rEnd][l])
        rEnd -= 1

        if cStart <= cEnd:
            for u in range(rEnd,rStart-1,-1):
                output.append(matrix[u][cStart])
        cStart += 1

    return output

# Go through the matrix in a spiral order. O(n*m), O(n*m) space
matrix = [[1,2,3],[4,5,6],[7,8,9]]
spiralMatrix = spiralOrder(matrix)
print(spiralMatrix)
