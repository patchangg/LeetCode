
def findLengthOfLCIS(nums):
    output = 1
    curr = 1
    for i in range(1,len(nums)):
        if nums[i] > nums[i-1]:
            curr += 1
        else:
            curr = 1
        output = max(curr,output)
    return output

nums = [1,3,5,4,7]
LCISLength = findLengthOfLCIS(nums)
print(LCISLength)
