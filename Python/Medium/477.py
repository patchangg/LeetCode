
def totalHammingDistance(self, nums: List[int]) -> int:
    output = 0
    for i in range(32):
        one = 0
        zero = 0
        for num in nums:
            one += (num >> i) & 1
            zero += not (num >> i) & 1
        output += one * zero
    return output

# for each bit of every number in the nums array, count the number of zeroes
# and one bits, multiply them to get the hamming distance between each number
# for that bit. Do this for every bit and return the sum
# O(32*n) where n is the length of nums, O(1) space
nums = [4,14,2]
totalDistance = totalHammingDistance(nums)
print(totalDistance)
