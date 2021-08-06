
def longestSubarray(nums):
    output = 0
    total = 0
    lo = 0
    for hi, num in enumerate(nums):
        total += num
        while lo < hi and total < hi - lo:
            total -= nums[lo]
            lo += 1
        output = max(output, hi - lo)
    return output

# Sliding Window Problem
# Slide across the nums array until you reach a second zero in the window
# Keep reducing the window size until the first zero is gone
# Track the largest window size every loop to find the longest subarray
# that contains the most amount of ones (after removing the zero)
# O(n), O(1) space
nums = [0,1,1,1,0,1,1,0,1]
longest = longestSubarray(nums)
print(longest)
