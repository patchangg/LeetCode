from collections import Counter

def subarraySum(nums, k):
    count = Counter()
    count[0] = 1
    output = 0
    prefix = 0
    for num in nums:
        prefix += num
        output += count[prefix-k]
        count[prefix] += 1
    return output

# Create a hashmap with 0 inside it to take care of the cases where num == k
# Go through the nums array and keep track of a prefix sum.
# Using the sum, check if the sum - k exists in the hashmap, if so that means
# that you can create a subarray thats sum equals k
# O(n), O(n) space
nums = [1,1,1]
k = 2
totalKSubarrays = subarraySum(nums,k)
print(totalKSubarrays)
