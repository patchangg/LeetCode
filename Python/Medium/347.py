import collections

def topKFrequent(nums, k):
    output = [key for key,value in collections.Counter(nums).most_common(k)]
    return output

# Use python Counter to count the times the number appears in the array
# Get the k most common numbers in the dictionary and return it
# O(k + n) = O(n), O(1) space
nums = [3,0,2,0]
k = 1
mostFrequent = topKFrequent(nums,k)
print(mostFrequent)
