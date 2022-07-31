
def shiftGrid(grid, k):
    l = []
    for row in grid:
        for num in row:
            l.append(num)
    m = len(grid)
    n = len(grid[0])
    k = k % (len(grid) * len(grid[0]))
    l = l[-k:] + l[:-k]
    output = []
    for i in range(m):
        row = l[i * n: i * n + n]
        output.append(row)
    return output

grid = [[1,2,3],[4,5,6],[7,8,9]]
k = 1
shiftedGrid = shiftGrid(grid,k)
print(shiftedGrid)
