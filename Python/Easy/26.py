
def removeDuplicates(nums):
    x = 1
    for i in range(len(nums)-1):
        if nums[i] != nums[i+1]:
            nums[x] = nums[i+1]
            x += 1
    return x

nums = [1,1,2]
noDuplicatesArrayLen = removeDuplicates(nums)
print(noDuplicatesArrayLen)
