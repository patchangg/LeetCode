
def transpose(matrix):
    output = []
    for m in range(len(matrix[0])):
        tmp = []
        for n in range(len(matrix)):
            tmp.append(matrix[n][m])
        output.append(tmp)
    return output

matrix = [[1,2,3],[4,5,6],[7,8,9]]
transposedMatrix = transpose(matrix)
print(transposedMatrix)
