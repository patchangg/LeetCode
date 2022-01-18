
def minSwaps(nums):
    n = nums.count(1)
    nums = nums + nums
    ones = 0
    zeroes = 0
    for i in range(len(nums)):
        if i >= n and nums[i - n]:
            ones -= 1
        if nums[i] == 1:
            ones += 1
        zeroes = max(zeroes,ones)
    return n - zeroes

# Append the original array to itself to avoid the circular array problem
# Create a sliding window and count the amount of ones and zeroes in the window each
# time its moved. Store the maximum number of ones in the window and
# minus it from the total number of ones to get the number of min swaps
# O(n), O(n) space
nums = [0,1,0,1,1,0,0]
numSwaps = minSwaps(nums)
print(numSwaps)
