
def maxProduct(nums):
    if len(nums) == 2:
        return ((nums[0]-1) * (nums[1]-1))
    highest = 0
    previous = 0
    for num in nums:
        if num > highest:
            previous = highest
            highest = num
        elif num == highest:
            if num > previous:
                previous = num
        elif num > previous:
            previous = num
    return ((highest - 1) * (previous - 1))

nums = [10,2,5,2]
max = maxProduct(nums)
print(max)
