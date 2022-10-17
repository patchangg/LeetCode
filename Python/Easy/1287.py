from collections import Counter

def findSpecialInteger(arr):
    counted = Counter(arr)
    return counted.most_common(1)[0][0]

arr = [1,2,2,6,6,6,6,7,10]
specialInteger = findSpecialInteger(arr)
print(specialInteger)
