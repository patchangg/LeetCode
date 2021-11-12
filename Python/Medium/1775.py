
def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
    sum1 = sum(nums1)
    sum2 = sum(nums2)
    if sum1 == sum2:
        return 0
    elif sum1 > sum2:
        largerSum = nums1
        smallerSum = nums2
    else:
        largerSum = nums2
        smallerSum = nums1
    totalDiff = abs(sum1-sum2)
    largerGainsArray = [num - 1 for num in largerSum]
    smallerGainsArray = [6 - num for num in smallerSum]
    totalGainsArray = largerGainsArray + smallerGainsArray
    totalGainsArray = sorted(totalGainsArray, reverse=True)
    output = 0
    for i in range(len(totalGainsArray)):
        totalDiff -= totalGainsArray[i]
        output += 1
        if totalDiff <= 0:
            return output
    return -1

# Find which array has a smaller and larger sum and get the absolute difference
# between them.
# Calculate the "maximum gain" at each index for both arrays
# Add both arrays together then sort them
# Remove the largest gains possible until the totaldifference is <= 0
# If that is not possible, return -1 else return the amount of operations
# O(n+m), O(n+m) space
nums1 = [1,2,3,4,5,6]
nums2 = [1,1,2,2,2,2]
minimumGains = minOperations(nums1,nums2)
print(minimumGains)
