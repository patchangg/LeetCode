
def twoSum(nums, target):
    seen = {}
    for i, value in enumerate(nums):
        remaining = target - nums[i]

        if remaining in seen: #3
            return [i, seen[remaining]]
        else:
            seen[value] = i


nums = [2,7,11,15]
target = 9
combined = twoSum(nums,target)
print(combined)
