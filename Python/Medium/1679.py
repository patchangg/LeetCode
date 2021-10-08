from collections import Counter

def maxOperations(nums, k):
    counted = Counter(nums)
    output = 0
    for num in counted:
        output += min(counted[num],counted[k-num])
    return output//2

# Count the number of integers in the nums array
# Create a loop and add any pairs that make k, if there isn't any pair for that
# integer, add 0 to the output. Divide the pairs by 2 to get the correct
# amount of pairs. O(nlogn), O(n) space
nums = [1,2,3,4]
k = 5
kPairNum = maxOperations(nums,k)
print(kPairNum)
