
def getMinDistance(nums, target, start):
    output = float(inf)
    for i in range(len(nums)):
        if nums[i] == target:
            if abs(i-start) < output:
                output = abs(i-start)
    return output

nums = [1,2,3,4,5]
target = 5
start = 3
minDistanceToTarget = getMinDistance(nums,target,start)
print(minDistanceToTarget)
