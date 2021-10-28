
def numSubarrayBoundedMax(nums, left, right):
    output = 0
    combos = 0
    prev = -1
    for i in range(len(nums)):
        if nums[i] < left:
            output += combos
        if nums[i] > right:
            combos = 0
            prev = i
        if left <= nums[i] <= right:
            combos = i - prev
            output += combos
    return output

# Each subarray must be bounded by [left,right]
# Go through the nums array
# If the number is less than left, that means we just create a new sub array
# containing the elements before the current number so we just add the same
# amount of combinations
# If the number is higher than right, we reset the combination counter to 0
# and set the previous as the current number index
# If the number is between left and right, we add the number of potential
# subarrays into the output based on the window size and the combinations made
# O(n), O(1) space
nums = [2,1,4,3]
left = 2
right = 3
nonEmptySubarrays = numSubarrayBoundedMax(nums,left,right)
print(nonEmptySubarrays)
