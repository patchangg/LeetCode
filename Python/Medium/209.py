
def minSubArrayLen(target, nums):
    output = float(inf)
    left = 0
    right = 0
    total = 0

    while right < len(nums):
        total += nums[right]
        right += 1
        while total >= target:
            output = min(output, right-left)
            total -= nums[left]
            left += 1

    if output == float(inf):
        return 0
    else:
        return output

# Create a sliding window which captures if the sum is greater than the target.
# If so, move the left window forward while checking if the minimum length
# is smaller than the current smallest length. O(n), O(1) space
target = 7
nums = [2,3,1,2,4,3]
minLength = minSubArrayLen(target,nums)
print(minLength)
