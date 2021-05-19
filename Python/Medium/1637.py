
def maxWidthOfVerticalArea(points):
    p = sorted([pt[0] for pt in points])
    maximum = 0
    for i in range(len(points)-1):
        maximum = max(maximum, (p[i+1] - p[i]))
    return maximum


# Y axis is irrelevant for this question as it scales up infinitely
# Find the largest gap between two x points as that would the
# widest vertical area between two points
# O(n log n) + O(n-1) = O(n log n) sort O(n) space
#points = [[8,7],[9,9],[7,4],[9,7]]
points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
maxWidth = maxWidthOfVerticalArea(points)
print(maxWidth)
