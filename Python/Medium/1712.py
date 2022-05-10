
def waysToSplit(self, nums: List[int]) -> int:
    prefix = [0] + list(accumulate(nums))
    output = 0
    j = 0
    k = 0

    for i in range(1,len(nums)):
        j = max(j,i+1)
        while j < len(nums) and 2 * prefix[i] > prefix[j]:
            j += 1
        k = max(k,j)
        while k < len(nums) and 2 * prefix[k] <= prefix[i] + prefix[-1]:
            k += 1
        output += k - j

    return output % (10**9 + 7)

# Create a prefix sum and use two pointers to find the middle and right index
# where prefix[i] <= prefix[j] - prefix[i] <= prefix[-1] - prefix[j]
# O(n), O(n) space
nums = [1,1,1]
numSplits = waysToSplit(nums)
print(numSplits)
