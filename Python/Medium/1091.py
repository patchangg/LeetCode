from collections import deque

def shortestPathBinaryMatrix(grid):
    n = len(grid)
    if grid[0][0] or grid[n-1][n-1]:
        return -1
    dirs = [[-1,-1],[-1,0],[1,-1],[0,1],[1,1],[1,0],[-1,1],[0,-1]]
    seen = set()
    queue = deque([(0,0,1)])
    seen.add((0,0))
    while queue:
        i,j,dist = queue.popleft()
        if i == n-1 and j == n-1:
            return dist
        for p1, p2 in dirs:
            x = i + p1
            y = j + p2
            if 0 <= x < n and 0 <= y < n:
                if (x,y) not in seen and grid[x][y] == 0:
                    queue.append((x,y,dist+1))
                    seen.add((x,y))
    return -1

# Create an array that contains the 8 ways the index can move to
# Do BFS on the grid, moving to valid cells, checking if they equal 0.
# If it equals 0 and has not been seen, add it to the queue and seen.
# Repeat until the bottom right corner is reached and return the steps, otherwise
# return -1. O(n^2), O(n^2) space
grid = [[0,1],[1,0]]
stepsForShortestPath = shortestPathBinaryMatrix(grid)
print(stepsForShortestPath)
