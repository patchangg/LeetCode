
def islandPerimeter(grid):
    output = 0
    m = len(grid)
    n = len(grid[0])
    for r in range(m):
        for c in range(n):
            output += 4 * grid[r][c]
            if r > 0:
                output -= grid[r][c] * grid[r-1][c]
            if r < m-1:
                output -= grid[r][c] * grid[r+1][c]
            if c > 0:
                output -= grid[r][c] * grid[r][c-1]
            if c < n-1:
                output -= grid[r][c] * grid[r][c+1]
    return output

grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
perimeter = islandPerimeter(grid)
print(perimeter)
