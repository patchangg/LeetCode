
def minOperations(grid, x):
    if len(grid) == 1 and len(grid[0]) == 1:
        return 0
    arr = []
    for g in grid:
        for num in g:
            arr.append(num)
    arr = sorted(arr)
    median = arr[len(arr) // 2]
    output = 0
    for n in arr:
        if abs(median - n) % x != 0:
            return -1
        else:
            output += abs(median - n) // x
    return output

# Sort the array and get the median number. Find the number of operations to
# get each number in the array from adding or subtracting x from it.
# If the edge case of a 1x1 grid or a number in the array cannot be changed to
# another through adding or subtracting x, return -1.
# O(2n + m) where n is the length of the grid and m is the length of the grid
# subarrays. O(n * m) space
grid = [[2,4],[6,8]]
x = 2
numOperations = minOperations(grid,x)
print(numOperations)
