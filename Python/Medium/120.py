
def minimumTotal(self, triangle: List[List[int]]) -> int:
    if not triangle:
        return
    for i in range(len(triangle)-2,-1,-1):
        for j in range(len(triangle[i])):
            triangle[i][j] += min(triangle[i+1][j],triangle[i+1][j+1])
    return triangle[0][0]

# Modify the triangle bottom up. Store the minimum path sum to get to that
# index by adding the smallest path below it. O(n^2), O(n*n/2) space
triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
minimumPathSum = minimumTotal(triangle)
print(minimumPathSum)
