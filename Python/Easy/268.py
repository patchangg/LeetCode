
def missingNumber(nums):
    for i in range(len(nums)):
        if i not in nums:
            return i
    return len(nums)

nums = [3,0,1]
missingNo = missingNumber(nums)
print(missingNo)
