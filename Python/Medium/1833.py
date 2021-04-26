
def maxIceCream(costs, coins):
    costs.sort()
    count = 0
    for cost in costs:
        if cost <= coins:
            count += 1
            coins -= cost
    return count
    
costs = [1,3,2,4,1]
coins = 7
max = maxIceCream(costs,coins)
print(max)
