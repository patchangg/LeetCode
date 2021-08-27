
def minPathSum(grid):
    m = len(grid)
    n = len(grid[0])
    for i in range(1,m):
        grid[i][0] += grid[i-1][0]
    for i in range(1,n):
        grid[0][i] += grid[0][i-1]
    for i in range(1,m):
        for j in range(1,n):
            grid[i][j] += min(grid[i-1][j],grid[i][j-1])
    return grid[-1][-1]

# DP Problem
# Count the cost of moving from the top left to the bottom right for every
# position. After finding all the costs, get the minimum cost to move through
# the path and return the last index which should contain the minimum path sum
# to get there. O(m+n+m+(m*n)), O(1) space
grid = [[1,3,1],[1,5,1],[4,2,1]]
minimumPath = minPathSum(grid)
print(minimumPath)
