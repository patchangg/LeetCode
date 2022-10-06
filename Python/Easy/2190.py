from collections import defaultdict

def mostFrequent(nums, key):
    dicts = defaultdict(int)
    for i in range(len(nums)-1):
        if nums[i] == key:
            dicts[nums[i+1]] += 1
    count = 0
    output = 0
    for key, value in dicts.items():
        if value > count:
            output = key
            count = value
    return output

nums = [1,100,200,1,100]
key = 1
frequentNum = mostFrequent(nums,key)
print(frequentNum)
