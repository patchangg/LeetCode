
def minOperations(nums):
    operations = 0
    reach = nums[0]
    for i in range(1,len(nums)):
        if reach >= nums[i]:
            operations += reach - nums[i] + 1
            nums[i] = reach + 1
        reach = nums[i]
    return operations

nums = [1,5,2,4,1]
min = minOperations(nums)
print(min)
