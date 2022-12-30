
def getMaximumGenerated(n):
    if n == 0:
        return 0
    nums = [0] * (n+1)
    nums[1] = 1
    for i in range(n+1):
        if 2 <= 2 * i and 2 * i <= n:
            nums[2 * i] = nums[i]
        if 2 <= (2 * i) + 1 and (2 * i) + 1 <= n:
            nums[(2 * i) + 1] = nums[i] + nums[i + 1]
    return max(nums)

n = 7
maximumInGeneratedArray = getMaximumGenerated(n)
print(maximumInGeneratedArray)
