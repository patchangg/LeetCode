
def minPairSum(nums):
    nums.sort()
    pairSum = []
    for i in range(int(len(nums)/2)):
        pairSum.append(nums[i] + nums[-(i+1)])
    return max(pairSum)



nums = [3,5,4,2,4,6]
minimum = minPairSum(nums)
print(minimum)
