
def smallestEqual(nums):
    for i in range(len(nums)):
        if i % 10 == nums[i]:
            return i
    return -1

nums = [0,1,2]
smallestMod = smallestEqual(nums)
print(smallestMod)
