
def getMaximumConsecutive(coins):
    output = 1
    for coin in sorted(coins):
        if coin > output:
            break
        output += coin
    return output

# Sort the array. If the coin is less than the output, that means we can achieve
# the integers 0 to coin and any other number 0 + coin to output - 1 + coin.
# The only problem is the gap between coin + 1, so sort the coins so we reach it
# later. O(nlogn), O(n) space
coins = [1,1,1,4]
maximum = getMaximumConsecutive(coins)
print(maximum)
