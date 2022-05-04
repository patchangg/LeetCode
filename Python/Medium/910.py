
def smallestRangeII(nums, k):
    nums = sorted(nums)
    output = nums[-1] - nums[0]
    for i in range(len(nums) - 1):
        maximum = max(nums[-1] - k, nums[i] + k)
        minimum = min(nums[i + 1] - k, nums[0] + k)
        output = min(output, maximum - minimum)
    return output

# Sort the array and use the smallest and largest as the base score
# For each number in the array, check if the newest minimum score can be created.
# Minimum will always use the smallest score + k and maximum will use the
# largest - k. O(nlogn), O(n) space
nums = [1,3,6]
k = 3
minScore = smallestRangeII(nums,k)
print(minScore)
