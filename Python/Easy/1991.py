
def findMiddleIndex(nums):
    left = 0
    right = sum(nums)

    for i in range(len(nums)):
        if left == right - nums[i]:
            return i
        left += nums[i]
        right -= nums[i]
    return -1

nums = [2,3,-1,8,4]
middleIndex = findMiddleIndex(nums)
print(middleIndex)
