import math

def judgeSquareSum(c):
    left = 0
    right = int(math.sqrt(c))
    while left <= right:
        cur = left * left + right * right
        if cur < c:
            left += 1
        elif cur > c:
            right -= 1
        else:
            return True
    return False

# From 0 to the square root of the input, use two pointers to find a pair of
# values that equal to c. O(n), O(1) space
c = 5
isSum = judgeSquareSum(c)
print(isSum)
