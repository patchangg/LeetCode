
def optimalDivision(nums):
    if len(nums) == 1:
        return str(nums[0])
    elif len(nums) == 2:
        return '/'.join(map(str,nums))
    else:
        return '{}/({})'.format(str(nums[0]), '/'.join(map(str , nums[1:])))

# The optimal Division is always the first number divided by
# the rest of the numbers divided by each other
# e.g D1/(D2/D3/D4/D5/..)
nums = [1000,100,10,2]
optimal = optimalDivision(nums)
print(optimal)
