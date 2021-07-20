
def rotate(matrix):
    matrix.reverse()
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

# Flip the matrix then flip it again on the side
# O(n + m) where n is the length of the matrix and m is the length of in the inner list
# O(2) space
matrix = [[1,2,3],[4,5,6],[7,8,9]]
rotated = rotate(matrix)
print(rotated)
