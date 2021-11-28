
def PredictTheWinner(nums):
    dp = {}
    def helper(i,j):
        if i == j:
            return nums[i]
        if (i,j) not in dp:
            dp[i,j] = max(nums[i] - helper(i+1,j),nums[j]-helper(i,j-1))
        return dp[i,j]
    return helper(0,len(nums)-1) >= 0

# Use Dynamic Programming with memorisation to check every proablity if
# player one can win by always choosing the most optimal move.
# Each step, calculate if its better to choose the first or last number in the
# array as choosing either step will get the sum of the maximum possible score
# after choosing the number. If the final difference in scores is >= 0,
# player 1 wins. O(n), O(n) space 
nums = [1,5,2]
canPlayerOneWin = PredictTheWinner(nums)
print(canPlayerOneWin)
