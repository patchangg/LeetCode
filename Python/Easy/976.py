
def largestPerimeter(nums):
    nums = sorted(nums)[::-1]
    for i in range(len(nums)-2):
        if nums[i] < nums[i+1] + nums[i+2]:
            return nums[i] + nums[i+1] + nums[i+2]
    return 0

nums = [2,1,2]
largestPerm = largestPerimeter(nums)
print(largestPerm)
