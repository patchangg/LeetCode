
def maxProfit(prices):
    sell = 0
    hold = 0
    buy = float('inf')
    for p in prices:
        buy = min(buy, p-hold)
        hold = sell
        sell = max(sell,p-buy)
    return sell

# Buy is the comparing if we should buy the stocks now or sell the stocks
# compared to the market market.
# Holding is holding the amount of stocks we have and not buying
# Selling is the maximum profit selling the stocks now compared to buying the
# stock + price of stocks we have.
# O(n), O(1) space
prices = [1,2,3,0,2]
profit = maxProfit(prices)
print(profit)
