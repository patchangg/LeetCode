
def minMaxGame(nums):
    n = len(nums)
    while n > 1:
        newNums = [0] * (n // 2)
        for i in range(n // 2):
            if i % 2 == 0:
                newNums[i] = (min(nums[2*i],nums[2*i+1]))
            else:
                newNums[i] = (max(nums[2*i],nums[2*i+1]))
        n = n // 2
        nums = newNums
    return nums[0]

nums = [1,3,5,2,4,8,2,2]
remainingNumber = minMaxGame(nums)
print(remainingNumber)
