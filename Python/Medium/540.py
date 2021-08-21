from collections import Counter

def singleNonDuplicate(nums):
    return Counter(nums).most_common()[-1][0]

# Count the nums and get the least common element
# O(n), O(1) space
nums = [1,1,2,3,3,4,4,8,8]
singleInteger = singleNonDuplicate(nums)
print(singleInteger)
