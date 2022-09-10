from collections import Counter

def findLucky(arr):
    counted = Counter(arr)
    output = []
    for key, item in counted.most_common():
        if key == item:
            output.append(key)
    if output:
        return max(output)
    else:
        return -1

arr = [2,2,3,4]
largestLuckyNumber = findLucky(arr)
print(largestLuckyNumber)
