
def checkPossibility(nums):
    index = -1

    if len(nums) == 0 or len(nums) == 1:
        return True

    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            if index != -1:
                return False
            index = i

    if index in [-1, 0, len(nums)-2]:
        return True

    if nums[index-1] <= nums[index+1] or nums[index] <= nums[index+2]:
        return True

    return False

# Use the index as a flag. Go through the array checking that the next number
# is greater than the current. If two occur then it is impossible.
# If the index flag is 0, -1 or n - 2 then it is possible as n - 2 means to just
# remove the last index and it is non-decreasing, same for 0.
# Otherwise check if deleting the current or next index will make the array
# non decreasing at the index point. O(n), O(1) space
nums = [4,2,3]
isPossible = checkPossibility(nums)
print(isPossible)
