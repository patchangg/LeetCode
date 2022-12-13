
def minimumDifference(nums, k):
    if k == 1:
        return 0

    nums = sorted(nums)
    output = float('inf')

    for i in range(k - 1,len(nums)):
        output = min(output,nums[i] - nums[i-k+1])
    return output

nums = [90]
k = 1
minDifference = minimumDifference(nums,k)
print(minDifference)
