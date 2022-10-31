
def isMonotonic(nums):
    if len(nums) < 3:
        return True

    inc = False
    dec = False

    for i in range(1,len(nums)):
        if nums[i-1] > nums[i]:
            dec = True
        elif nums[i-1] < nums[i]:
            inc = True

        if inc and dec:
            return False
    return True

nums = [1,2,2,3]
isArrayMonotonic = isMonotonic(nums)
print(isArrayMonotonic)
