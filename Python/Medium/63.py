
def uniquePathsWithObstacles(obstacleGrid):
    row = len(obstacleGrid)
    col = len(obstacleGrid[0])
    dp = [[0 for _ in range(col)] for _ in range(row)]
    dp[0][0] = 1 - obstacleGrid[0][0]
    for r in range(1,row):
        dp[r][0] = dp[r-1][0] * (1 - obstacleGrid[r][0])
    for c in range(1,col):
        dp[0][c] = dp[0][c-1] * (1 - obstacleGrid[0][c])
    for r in range(1,row):
        for c in range(1,col):
            dp[r][c] = (dp[r][c-1] + dp[r-1][c]) * (1 - obstacleGrid[r][c])
    return dp[-1][-1]

# Create a row * col matrix to store the dp. For each row and column
# check if its possible to move there and check if there is an obstacle or not
# as if there is an obstacle, remove that path by multiplying it by zero
# O(n*m), O(n*m) space
obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
uniquePathsPossible = uniquePathsWithObstacles(obstacleGrid)
print(uniquePathsPossible)
