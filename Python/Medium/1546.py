
def maxNonOverlapping(nums, target):
    seen = {0:1}
    curr = 0
    output = 0
    for i in range(len(nums)):
        curr += nums[i]
        prev = curr - target
        if prev in seen:
            output += 1
            seen = {}
        if curr not in seen:
            seen[curr] = 1
    return output

# Create a hashmap with 0:1 so that if the first element equals the target
# it will create a valid subarray. Create a prefix sum and check if the sum
# is equal to the target, if so that is a valid target and reset the dict
# otherwise add the prefix sum into the dict. O(n), O(n) space
nums = [1,1,1,1,1]
target = 2
numNonOverlapping = maxNonOverlapping(nums,target)
print(numNonOverlapping)
