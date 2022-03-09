
def coinChange(coins, amount):
    output = 0
    coins = sorted(coins)
    dp = [0] + [float(inf)] * amount
    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i-coin]+1)
    if dp[amount] != float(inf):
        return dp[amount]
    else:
        return -1

# Using dp we can store the amount of coins used for each number leading to
# the amount and the last index will contain the lowest amount of coins used
# to get the amount. O(n*m) where n is the amount and m is the length of coins,
# O(n) space
coins = [1,2,5]
amount = 11
numCoins = coinChange(coins,amount)
print(numCoins)
