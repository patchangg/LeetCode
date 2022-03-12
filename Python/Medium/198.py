
def rob(nums):
    rob = 0
    dontRob = 0
    for num in nums:
        rob, dontRob = dontRob + num, max(rob, dontRob)
    return max(rob,dontRob)

# Go through the array, constantly checking the max between robbing the house
# compared to not robbing the previous house plus the current house.
# O(n), O(1) space
nums = [1,2,3,1]
maximumMoney = rob(nums)
print(maximumMoney)
