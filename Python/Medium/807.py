
def maxIncreaseKeepingSkyline(grid):
    topBot = []
    leftRight = []
    row = len(grid)
    col = len(grid[0])
    for r in grid:
        leftRight.append(max(r))
    for c in range(col):
        tallest = 0
        for r in range(row):
            if grid[r][c] > tallest:
                tallest = grid[r][c]
        topBot.append(tallest)
    output = 0
    for r in range(row):
        sum = 0
        for c in range(col):
            sum += (min(leftRight[r],topBot[c]) - grid[r][c])
        output += sum
    return output



# compare [0][0],[1][0],[2][0],[3][0]
# get the biggest value
# compare the biggest height to the original grid
# find the difference and add them togethter to get output
grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
maxSkyline = maxIncreaseKeepingSkyline(grid)
print(maxSkyline)
