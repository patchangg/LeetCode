
def maxAbsoluteSum(nums):
    max_so_far = 0
    positive_end = 0
    negative_end = 0
    for num in nums:
        positive_end = max(0,positive_end+num)
        negative_end = min(0,negative_end+num)
        max_so_far = max(max_so_far,positive_end,-negative_end)
    return max_so_far

# Adapt Kadane’s Algorithm to the problem
# Since we need to find the absolute, we find the highest positive and negative
# subarray in the array and track the maximum absolute number so far in the
# loop. This will find the largest absolute subarray value in the array
# O(n), O(1) space
nums = [1,-3,2,3,-4]
maximumSubarray = maxAbsoluteSum(nums)
print(maximumSubarray)
