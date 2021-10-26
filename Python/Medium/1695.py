
def maximumUniqueSubarray(nums):
    start = 0
    end = 0
    output = 0
    total = 0
    s = set()
    while end < len(nums):
        if nums[end] not in s:
            s.add(nums[end])
            total += nums[end]
            end += 1
            output = max(output,total)
        else:
            total -= nums[start]
            s.remove(nums[start])
            start += 1
    return output

# Sliding window
# Make the window 0 0 and create a set. If the number is not in the set,
# add it to the set, total and check if current total is larger than the highest
# then extend the window by 1
# If the number is in the set, remove it from the set, extend the start of the
# window by 1 and minus the number from the curretnt total.
# This makes it that the window always contains unique numbers and we get the
# sum of it. Once the window hits the end, return the maximum unique subarray sum
# O(n), O(n) space
nums = [4,2,4,5,6]
maximumSum = maximumUniqueSubarray(nums)
prin(maximumSum)
