
def countServers(grid):
    col = [0] * len(grid[0])
    row = [0] * len(grid)
    output = 0
    for g in range(len(grid)):
        for i in range(len(grid[0])):
            if grid[g][i] == 1:
                col[i] += 1
                row[g] += 1
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 1:
                if row[r] > 1 or col[c] > 1:
                    output += 1
    return output

# Count the number of servers in each row and column
# Iterate through the grid again and check if there is another server
# in the same row or column as the server, if so iterate the output by 1
# O(n), O(n) space
grid = [[1,0],[0,1]]
serversWhoCommunicate = countServers(grid)
print(serversWhoCommunicate)
