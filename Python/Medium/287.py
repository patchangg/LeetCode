from collections import Counter

def findDuplicate(nums):
    arr = Counter(nums)
    return arr.most_common(1)[0][0]

# Count all the numbers in the nums array and return the repeated integer
# O(n), O(1) space
nums = [1,3,4,2,2]
duplicate = findDuplicate(nums)
print(duplicate)
