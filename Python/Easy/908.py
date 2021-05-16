
def smallestRangeI(nums, k):
    minNum = min(nums)
    maxNum = max(nums)
    return max(0,maxNum-k-minNum-k)


nums = [1]
k = 0
smallest = smallestRangeI(nums,k)
print(smallest)
