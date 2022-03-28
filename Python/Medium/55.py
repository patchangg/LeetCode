
def canJump(nums):
    lastJump = len(nums) - 1
    for i in range(len(nums)-2,-1,-1):
        if nums[i] + i >= lastJump:
            lastJump = i
    if lastJump == 0:
        return True
    else:
        return False

# Going from the end of the array, check if the index plus the number in the
# array can reach the last jump that can reach the end, if so change the
# last jump to the index. If the last jump reaches the 0th index, that means
# that there is a path to the end. O(n), O(1) space
nums = [2,3,1,1,4]
reachEnd = canJump(nums)
print(reachEnd)
