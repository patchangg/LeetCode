
def maxProfit(prices):
    output = 0
    s = prices[0]
    for i in range(1,len(prices)):
        if prices[i] > s:
            output = max(output,prices[i] - s)
        else:
            s = prices[i]
    return output

prices = [7,1,5,3,6,4]
maximumProfit = maxProfit(prices)
print(maximumProfit)
