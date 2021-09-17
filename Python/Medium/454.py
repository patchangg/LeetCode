import collections

def fourSumCount(nums1, nums2, nums3, nums4):
    output = 0
    complement = collections.defaultdict(int)
    for num1 in nums1:
        for num2 in nums2:
            complement[num1+num2] += 1
    for num3 in nums3:
        for num4 in nums4:
            output += complement[-(num3+num4)]
    return output

# Create a hashmap and put the sum of num1 and num2 as a index
# Check -(num3 + num4) is in the hashmap and add it to the result
# as that means we have the numbers in the arrays to add up to 0 when all the
# integers are added together. O(n^2), O(1) space
nums1 = [1,2]
nums2 = [-2,-1]
nums3 = [-1,2]
nums4 = [0,2]
totalSum = fourSumCount(nums1,nums2,nums3,nums4)
print(totalSum)
