
def findKDistantIndices(nums, key, k):
    output = []
    for j in range(len(nums)):
        if nums[j] == key:
            for i in range(len(nums)):
                if abs(i - j) <= k:
                    output.append(i)
    return set(output)

nums = [3,4,9,1,3,9,5]
key = 9
k = 1
kDistantIndices = findKDistantIndices(nums,key,k)
print(kDistantIndices)
