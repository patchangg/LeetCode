from collections import defaultdict

def leastBricks(wall):
    dicts = defaultdict(int)
    for line in wall:
        i = 0
        for brick in line[:-1]:
            i += brick
            dicts[i] += 1
    return len(wall) - max(dicts.values(),default=0)

# Create a hash map that stores the indexes of edges where edges are where two
# bricks meet each other. This will find the index that contains the most
# amount of edges which we will cut on to find the line that will cut the least
# amount of bricks. O(n*m) where n is length of the walls and m is the
# amount of bricks in the line, O(n) space
wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
numCutBricks = leastBricks(wall)
print(numCutBricks)
