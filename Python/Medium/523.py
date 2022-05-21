
def checkSubarraySum(nums, k):
    dicts = {0: -1}
    total = 0
    for i, n in enumerate(nums):
        total = (total + n) % k
        if total not in dicts:
            dicts[total] = i
        else:
            if i - dicts[total] >= 2:
                return True
    return False

# Create a dictionary with 0:-1 inside for the case where the sum mod k equals
# 0. For each number in the array, add it to the prefix sum mod k.
# Check if the current prefix sum remainder is in the dictionary and that the
# index positions is greater than 1, which means there is a subarray that is
# a multiple of k. O(n), O(n) space
nums = [23,2,4,6,7]
k = 6
multipleOfK = checkSubarraySum(nums,k)
print(multipleOfK)
