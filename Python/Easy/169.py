from collections import Counter

def majorityElement(nums):
    counted = Counter(nums)
    return counted.most_common(1)[0][0]

nums = [3,2,3]
majority = majorityElement(nums)
print(majority)
