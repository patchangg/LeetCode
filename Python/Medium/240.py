
def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    for row in matrix:
        if target in row:
            return True
    return False

# Go through each row of the matrix and check if target is in the row
# O(n), O(1) space
matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5
inMatrix = searchMatrix(matrix,target)
print(inMatrix)
