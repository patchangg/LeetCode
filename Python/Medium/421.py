
def findMaximumXOR(nums):
    output = 0
    mask = 0
    for i in range(31,-1,-1):
        mask = mask | 1 << i
        found = set([num & mask for num in nums])
        start = output | 1 << i
        for prefix in found:
            if start ^ prefix in found:
                output = start
                break
    return output

# Highest possible number is 2^31 - 1 so we start with the highest number
# Create a mask and a set of all possible starts of numbers and then apply
# the two sum problem where if we find two numbers with XOR starting with
# the start, we update the output and look for the next digit
# O(nlogn), O(1) space
nums = [3,10,5,25,2,8]
maximumXOR = findMaximumXOR(nums)
print(maximumXOR)
