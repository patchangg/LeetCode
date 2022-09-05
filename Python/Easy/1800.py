
def maxAscendingSum(nums):
    output = nums[0]
    curr = nums[0]
    prev = nums[0]
    for i in range(1,len(nums)):
        if nums[i] > prev:
            curr += nums[i]
        else:
            output = max(output,curr)
            curr = nums[i]
        prev = nums[i]
    output = max(output,curr)
    return output

nums = [10,20,30,5,10,50]
maximumAscendingSum = maxAscendingSum(nums)
print(maximumAscendingSum)
