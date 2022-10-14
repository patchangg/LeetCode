from collections import Counter

def countElements(nums):
    counted = Counter(nums)
    print(counted[min(nums)],counted[max(nums)])
    if len(set(nums)) > 1:
        return len(nums) - counted[min(nums)] - counted[max(nums)]
    return 0

nums = [11,7,2,15]
numOfBetweenElements = countElements(nums)
print(numOfBetweenElements)
