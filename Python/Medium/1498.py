
def numSubseq(nums, target):
    nums = sorted(nums)
    output = 0
    left = 0
    right = len(nums) - 1
    modulo = (10**9 + 7)
    while left <= right:
        if nums[left] + nums[right] > target:
            right -= 1
        else:
            output += 2 ** (right - left)
            output %= modulo
            left += 1
    return output % modulo

# Sort the nums array to utilise two pointers.
# Create a sliding window where the left and right sum of the window is less
# than or equal to target, add the possible amount of subsequences to the
# output then make the window smaller. O(nlogn), O(n) space
nums = [3,5,6,7]
target = 9
minMaxTarget = numSubseq(nums,target)
print(minMaxTarget)
