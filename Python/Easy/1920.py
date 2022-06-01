
def buildArray(nums):
    output = []
    for i in range(len(nums)):
        output.append(nums[nums[i]])
    return output

nums = [0,2,1,5,3,4]
zeroArray = buildArray(nums)
print(zeroArray)
