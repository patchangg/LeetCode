
def kClosest(points, k):
    output = sorted(points, key=lambda point: sqrt(point[0] ** 2 + point[1] ** 2))
    return output[:k]

points = [[1,3],[-2,2]]
k = 1
closest = kClosest(points,k)
print(closest)
# Sort the points based on the distance from (0,0) and return k nearest.
# Use the Euclidean distance which is sqrt((x1^2-x2^2)+(y1^2-y2^2))
# O(n) for the sort
