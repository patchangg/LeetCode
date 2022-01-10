
def closestCost(baseCosts, toppingCosts, target):
    self.output = float('inf')
    def dfs(idx,cost):
        if abs(cost-target) < abs(self.output-target):
            self.output = cost
        elif abs(cost-target) == abs(self.output-target):
            self.output = min(self.output,cost)

        if idx == len(toppingCosts) or cost >= target:
            return

        dfs(idx+1,cost)
        dfs(idx+1,cost+toppingCosts[idx])
        dfs(idx+1,cost+(2*toppingCosts[idx]))

    for base in baseCosts:
        dfs(0,base)

    return self.output

# For each base cost, calculate its cost with 0, 1 or 2 of each topping and
# find the cost closest to the target. O(n * m * 3), O(1) space
baseCosts = [1,7]
toppingCosts = [3,4]
target = 10
cloest = closestCost(baseCosts,toppingCosts,target)
print(closest)
