
def maxProductDifference(nums):
    nums = sorted(nums)[::-1]
    return (nums[0] * nums[1]) - (nums[-1] * nums[-2])

nums = [5,6,2,7,4]
maxDifference = maxProductDifference(nums)
print(maxDifference)
