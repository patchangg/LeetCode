from collections import Counter

def divideArray(nums):
    counted = Counter(nums)
    for num in counted.values():
        if num % 2 != 0:
            return False
    return True

nums = [3,2,3,2,2,2]
equalPairs = divideArray(nums)
print(equalPairs)
