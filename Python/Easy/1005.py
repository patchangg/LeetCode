
def largestSumAfterKNegations(nums, k):
    nums = sorted(nums)
    i = 0
    while i < len(nums) and nums[i] < 0 and k > 0:
        nums[i] = -nums[i]
        i += 1
        k -= 1
    if k % 2 == 0:
        return sum(nums)
    else:
        return sum(nums) - 2 * min(nums)

nums = [4,2,3]
k = 1
arraySumAfterNegations = largestSumAfterKNegations(nums,k)
print(arraySumAfterNegations)
