
def rob(nums):

    def leftRob(nums):
        rob = 0
        dontRob = 0
        for num in nums:
            rob, dontRob = dontRob + num, max(rob, dontRob)
        return max(rob,dontRob)

    def rightRob(nums):
        rob = 0
        dontRob = 0
        for num in nums:
            rob, dontRob = dontRob + num, max(rob, dontRob)
        return max(rob,dontRob)

    if len(nums) == 1:
        return nums[0]
    else:
        return max(leftRob(nums[1:]),rightRob(nums[:-1]))

# Rob the houses twice, once from each end to remove the circular array factor
# Go through the array, constantly checking the max between robbing the house
# compared to not robbing the previous house plus the current house.
# O(n), O(n) space
nums = [2,3,2]
mostMoney = rob(nums)
print(mostMoney)
