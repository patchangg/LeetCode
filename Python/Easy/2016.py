
def maximumDifference(nums):
    output = -1
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            if nums[i] < nums[j]:
                output = max(output,nums[j]-nums[i])
    return output

nums = [7,1,5,4]
maxDiff = maximumDifference(nums)
print(maxDiff)
