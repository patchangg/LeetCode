
def arraySign(nums):
    sum = 1
    for i in nums:
        sum *= i
    if sum > 0:
        return 1
    elif sum == 0:
        return 0
    else:
        return -1

nums = [-1,-2,-3,-4,3,2,1]

s = arraySign(nums)
print(s)
