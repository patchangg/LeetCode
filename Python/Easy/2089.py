
def targetIndices(nums, target):
    nums = sorted(nums)
    output = []
    for i in range(len(nums)):
        if nums[i] == target:
            output.append(i)
    return output

nums = [1,2,5,2,3]
target = 2
numIndices = targetIndices(nums,target)
print(numIndices)
