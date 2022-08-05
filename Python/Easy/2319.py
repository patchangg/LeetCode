
def checkXMatrix(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if i == j or i + j == len(grid) - 1:
                if grid[i][j] == 0:
                    return False
            elif grid[i][j] > 0:
                return False
    return True

grid = [[2,0,0,1],[0,3,1,0],[0,5,2,0],[4,0,0,2]]
isXMatrix = checkXMatrix(grid)
print(isXMatrix)
