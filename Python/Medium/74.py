
def searchMatrix(matrix, target):
    if not matrix or not matrix[0]:
        return False
    n = len(matrix)
    m = len(matrix[0])
    left = 0
    right = m * n - 1
    while left < right:
        middle = (left + right) // 2
        if matrix[middle//m][middle%m] < target:
            left = middle + 1
        else:
            right = middle
    return matrix[left//m][left%m] == target

# Instead of a 2d array, think of it just as a sorted list.
# Use binary search on the sorted list, using matrix[middle//m][middle%m]
# to check if the element is smaller or larger than the target.
# Once the index is found, check if it equals the target. O(logm*logn), O(1) space
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
targetFound = searchMatrix(matrix,target)
print(targetFound)
