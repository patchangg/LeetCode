
def findShortestSubArray(nums):
    output = float(inf)
    length = 1
    index = {}

    for i in range(len(nums)):
        if nums[i] not in index:
            index[nums[i]] = [i]
        else:
            index[nums[i]].append(i)
            length = max(length,len(index[nums[i]]))
    for i in index:
        arr = index[i]
        if len(arr) == length:
            output = min(output,arr[-1] - arr[0] + 1)
    return output

nums = [1,2,2,3,1]
smallestDegree = findShortestSubArray(nums)
print(smallestDegree)
