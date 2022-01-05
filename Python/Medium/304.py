class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        for row in range(len(matrix)):
            for col in range(1, len(matrix[0])):
                matrix[row][col] = matrix[row][col - 1] + matrix[row][col]

        for row in range(1, len(matrix)):
            for col in range(len(matrix[0])):
                matrix[row][col] = matrix[row][col] + matrix[row - 1][col]
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        regionSum = self.matrix[row2][col2]
        if row1 != 0:
            topRight = self.matrix[row1-1][col2]
        else:
            topRight = 0
        if col1 != 0:
            bottomLeft = self.matrix[row2][col1-1]
        else:
            bottomLeft = 0
        if row1 != 0 and col1 != 0:
            topLeft = self.matrix[row1-1][col1-1]
        else:
            topLeft = 0
        return regionSum - topRight - bottomLeft + topLeft

# Create a prefix sum for the matrix by adding each row first then each column
# Sum query in a 2D matrix is the regionSum - topRight - bottomLeft + topLeft
# O(m*n), O(1) space
numMatrix = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
numMatrix.sumRegion(2, 1, 4, 3); # return 8 (i.e sum of the red rectangle)
numMatrix.sumRegion(1, 1, 2, 2); # return 11 (i.e sum of the green rectangle)
numMatrix.sumRegion(1, 2, 2, 4); # return 12 (i.e sum of the blue rectangle)
