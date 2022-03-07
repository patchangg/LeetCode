from collections import Counter

def findPairs(nums, k):
    output = 0
    freq = Counter(nums)
    for num in freq:
        if (k > 0 and num + k in freq) or (k == 0 and freq[num] > 1):
            output += 1
    return output

# Count each number in the nums array.
# Go through each frequency of every number in the array, checking if
# num + k is in it if k is greater than 0 which means we can create a unique pair.
# If k equals 0, that means we need to find the same number, so check if the
# frequency of the number is greate than one. O(nlogn), O(n) space
nums = [3,1,4,1,5]
k = 2
numUnqiuePairs = findPairs(nums,k)
print(numUnqiuePairs)
