
def maxFrequency(nums, k):
    left = 0
    maximum = 0
    total = 0
    nums = sorted(nums)
    for right in range(len(nums)):
        total += nums[right]
        while (nums[right]*(right-left+1)-total>k):
            total -= nums[left]
            left += 1
        maximum = max(maximum,right-left+1)
    return maximum

# Sort the nums array then create a sliding window that contains the numbers
# that can be transformed  into the same number with k or less transformations.
# O(nlogn), O(n) space
nums = [1,2,4]
k = 5
frequency = maxFrequency(nums,k)
print(frequency)
