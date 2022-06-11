from collections import defaultdict

def countKDifference(nums, k):
    dicts = defaultdict(int)
    output = 0
    for num in nums:
        dicts[num] += 1
        output += dicts[num-k]
        output += dicts[num+k]
    return output

nums = [1,2,2,1]
k = 1
pairs = countKDifference(nums,k)
print(pairs)
