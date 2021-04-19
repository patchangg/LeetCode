
def smallerNumbersThanCurrent(nums):
    list = []
    for i in nums:
        smaller = 0
        for j in nums:
            if j < i:
                smaller += 1
        list.append(smaller)
    return list


nums = [8,1,2,2,3]
s = smallerNumbersThanCurrent(nums)
print(s)
# j != i and nums[j] < nums[i]
