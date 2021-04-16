
def numIdenticalPairs(nums):
    goodPairs = 0
    i = 0
    while i < len(nums):
        j = i + 1
        while j < len(nums):
            if nums[i] == nums[j]:
                if i < j:
                    goodPairs += 1
            j += 1
        i += 1
        if i == len(nums):
            return goodPairs

nums = [1,2,3,1,1,3]
goodPairs = numIdenticalPairs(nums)
print(goodPairs)
