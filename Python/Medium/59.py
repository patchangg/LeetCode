
def generateMatrix(n):
    if not n:
        return []
    output = [[0 for j in range(n)] for i in range(n)]
    left = 0
    right = n-1
    top = 0
    down = n-1
    num = 1
    while left <= right and top <= down:
        for i in range(left, right+1):
            output[top][i] = num
            num += 1
        top += 1
        for i in range(top, down+1):
            output[i][right] = num
            num += 1
        right -= 1
        for i in range(right, left-1, -1):
            output[down][i] = num
            num += 1
        down -= 1
        for i in range(down, top-1, -1):
            output[i][left] = num
            num += 1
        left += 1
    return output

# Create a for loop that continously creates sprials until it reaches the center
# O(n^2), O(n) space
n = 3
spiral = generateMatrix(n)
print(spiral)
