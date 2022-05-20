
def minSubarray(nums, p):
    remainder = sum(nums) % p
    output = len(nums)
    prefix = 0
    prefixSum = {prefix : -1}
    for i, num in enumerate(nums):
        prefix = (prefix + num) % p
        key = (prefix - remainder) % p
        prefixSum[prefix] = i
        if key in prefixSum:
            output = min(output, i - prefixSum[key])
    if output < len(nums):
        return output
    else:
        return -1

# Find the remainder of the sum of the array divided by p. Using a prefix sum
# stored in a hashmap, check any key pairs are in the hashmap that would make
# the sum divisable by p with no remainders and find the length from the current
# index to the key to get the minimum length subarry. O(n), O(n) space
nums = [3,1,4,2]
p = 6
minArray = minSubarray(nums,p)
print(minArray)
