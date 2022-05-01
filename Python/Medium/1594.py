
def maximumProductPath(grid):
    m = len(grid)
    n = len(grid[0])
    maximum = [[0] * n for _ in range(m)]
    minimum = [[0] * n for _ in range(m)]
    maximum[0][0] = grid[0][0]
    minimum[0][0] = grid[0][0]

    for r in range(1, n):
        maximum[0][c] = maximum[0][c - 1] * grid[0][c]
        minimum[0][c] = minimum[0][c - 1] * grid[0][c]

    for c in range(1, m):
        maximum[r][0] = maximum[r - 1][0] * grid[r][0]
        minimum[r][0] = minimum[r - 1][0] * grid[r][0]

    for r in range(1, m):
        for c in range(1, n):
            if grid[r][c] > 0:
                maximum[r][c] = max(maximum[r - 1][c], maximum[r][c - 1]) * grid[r][c]
                minimum[r][c] = min(minimum[r - 1][c], minimum[r][c - 1]) * grid[r][c]
            else:
                maximum[r][c] = min(minimum[r - 1][c], minimum[r][c - 1]) * grid[r][c]
                minimum[r][c] = max(maximum[r - 1][c], maximum[r][c - 1]) * grid[r][c]

    if maximum[-1][-1] >= 0:
        return maximum[-1][-1] % (10**9 + 7)
    else:
        return -1

# Top Down DP. Since there are negative numbers, check if the negative can be
# multiplied with a negative to get a larger number or not.
# O(n * m), O(n * m) space
grid = [[-1,-2,-3],[-2,-3,-3],[-3,-3,-2]]
maximumProduct = maximumProductPath(grid)
print(maximumProduct)
