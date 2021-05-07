
def sortedSquares(nums):
    for i in range(len(nums)):
        nums[i] = (nums[i] * nums[i])
    nums.sort()
    return nums


nums = [-4,-1,0,3,10]
sorted = sortedSquares(nums)
print(sorted)
