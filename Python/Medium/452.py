
def findMinArrowShots(points):
    points.sort(key = lambda x: x[1])
    n = len(points)
    output = 1
    if n == 0:
        return 0
    curr = points[0]

    for i in range(n):
        if curr[1] < points[i][0]:
            output += 1
            curr = points[i]

    return output

# Sort the ballons by the end point then go through each point
# If the start of the new ballon does not overlap with the current end point
# of the ballon that means they do not overlap, therefore we need to fire another
# arrow to hit that ballon, so we make that ballon the new current ballon.
# O(nlogn), O(1) space
points = [[10,16],[2,8],[1,6],[7,12]]
minArrows = findMinArrowShots(points)
print(minArrows)
