
def jump(nums):
    n = len(nums)
    i = 0
    maximum = 0
    lastReached = 0
    jumps = 0
    while lastReached < n - 1:
        maximum = max(maximum, i + nums[i])
        if i == lastReached:
            lastReached = maximum
            jumps += 1
        i += 1
    return jumps

# Go through each number in the jump array and find the maximum jump
# that it can reach. Once the previous maximum jump is reached, reset it to the
# new maximium jump found. This will get every combination possible to reach
# the end and find the minimum amount of jumps needed. O(n), O(1) space
nums = [2,3,1,1,4]
jumps = jump(nums)
print(jumps)
