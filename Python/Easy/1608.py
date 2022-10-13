
def specialArray(nums):
    nums.sort(reverse=True)
    length = len(nums)
    i = 0
    while i < length and nums[i] > i:
        i += 1
    if i < length and i == nums[i]:
        return -1
    else:
        return i

nums = [3,5]
specialArrayNum = specialArray(nums)
print(specialArrayNum)
