
def minAreaRect(points):
    seen = set()
    output = float('inf')
    for x1, y1 in points:
        for x2, y2 in seen:
            if (x1, y2) in seen and (x2, y1) in seen:
                area = abs(x1 - x2) * abs(y1 - y2)
                if area and area < output:
                    output = area
        seen.add((x1,y1))
    if output < float('inf'):
        return output
    else:
        return 0

# Brute Force Method
# Loop through all the points, adding them into a set.
# If two pair of points make a rectangle, check if the area is smaller than
# the current smallest. Return 0 if no valid rectangles were found
# O(n^2), O(1) space
points = [[1,1],[1,3],[3,1],[3,3],[2,2]]
minimumArea = minAreaRect(points)
print(minimumArea)
