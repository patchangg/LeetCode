
def createTargetArray(nums, index):
    output = []
    for i, n in zip(index,nums):
        output.insert(i,n)
    return output

nums = [0,1,2,3,4]
index = [0,1,2,2,1]
targetArray = createTargetArray(nums,index)
print(targetArray)
