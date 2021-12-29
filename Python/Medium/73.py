
def setZeroes(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    m = len(matrix)
    n = len(matrix[0])

    firstRowIsZero = False
    firstColIsZero = False

    for row in range(m):
        for col in range(n):
            if matrix[row][col] == 0:
                if row == 0:
                    firstRowIsZero = True
                if col == 0:
                    firstColIsZero = True
                matrix[0][col] = 0
                matrix[row][0] = 0

    for row in range(1,m):
        for col in range(1,n):
            if matrix[0][col] == 0 or matrix[row][0] == 0:
                matrix[row][col] = 0

    if firstRowIsZero:
        for col in range(n):
            matrix[0][col] = 0

    if firstColIsZero:
        for row in range(m):
            matrix[row][0] = 0

# Use the first row and column of the matrix to record if the row or column
# needs to be changed to all zeroes. If the first row or column, contains a
# zero, set a flag to be true so it can change the row/column at the end.
# O(m + n) where m is the number of rows and n is the number of columns,
# O(1) space
matrix = [[1,1,1],[1,0,1],[1,1,1]]
setZeroes(matrix)
print(matrix)
