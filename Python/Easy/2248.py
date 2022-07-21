from collections import Counter

def intersection(nums):
    n = len(nums)
    output = []
    combined = []
    for num in nums:
        combined += num
    counted = Counter(combined)
    for key,value in counted.items():
        if value == n:
            output.append(key)
    return sorted(output)

nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
present = intersection(nums)
print(present)
