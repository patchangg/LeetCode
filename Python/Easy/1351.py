
def countNegatives(grid):
    count = 0
    for g in grid:
        for i in g:
            if i < 0:
                count += 1
    return count

grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
negatives = countNegatives(grid)
print(negatives)
