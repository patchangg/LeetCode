
def minimumCost(cost):
    output = 0
    cost = sorted(cost)[::-1]
    for i in range(len(cost)):
        if (i + 1) % 3 != 0:
            output += cost[i]
    return output

cost = [1,2,3]
minCost = minimumCost(cost)
print(minCost)
