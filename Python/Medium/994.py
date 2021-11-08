from collections import deque

def orangesRotting(grid):
    rows = len(grid)
    if rows == 0:
        return -1
    cols = len(grid[0])
    rotten = deque()
    fresh = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                rotten.append((r,c))
            elif grid[r][c] == 1:
                fresh += 1
    output = 0
    while rotten and fresh > 0:
        output += 1
        for _ in range(len(rotten)):
            x, y = rotten.popleft()
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                xx = x + dx
                yy = y + dy
                if xx < 0 or xx == rows or yy == cols or yy < 0:
                    continue
                if grid[xx][yy] == 0 or grid[xx][yy] == 2:
                    continue
                fresh -= 1
                grid[xx][yy] = 2
                rotten.append((xx,yy))

    if fresh == 0:
        return output
    else:
        return -1

# Count the number of fresh oranges and place to co-ordinates of the rotten
# oranges in a deque. While there is rotten and fresh oranges left, check
# the co-ordinates adjacent to the rotten orange, if there is a fresh orange
# change it to a rotten orange and append it to the deque.
# If there is no more fresh oranges after going through each rotten orange and
# the ones it affected, return the number of minutes it took, else it is impossible
# so return -1. O(n*m*4j) where n = rows, m = cols and j = num of oranges,
# O(n) space
grid = [[2,1,1],[1,1,0],[0,1,1]]
minutesToRotOranges = orangesRotting(grid)
print(minutesToRotOranges)
