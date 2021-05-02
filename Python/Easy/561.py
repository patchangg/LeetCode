
def arrayPairSum(nums):
    nums.sort()
    output = 0
    i = 0
    while i < len(nums):
        output += min(nums[i],nums[i+1])
        i += 2
    return output

nums = [6,2,6,5,1,2]
paired = arrayPairSum(nums)
print(paired)
