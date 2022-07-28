
def minStartValue(nums):
    prefixSum = 0
    output = 0
    for num in nums:
        prefixSum += num
        output = min(prefixSum,output)

    return -output + 1

nums = [-3,2,-3,4,2]
minPositiveValue = minStartValue(nums)
print(minPositiveValue)
