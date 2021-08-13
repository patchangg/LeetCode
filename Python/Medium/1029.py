
def twoCitySchedCost(costs):
    firstCity = [i for i,j in costs]
    difference = [j-i for i,j in costs]
    return (sum(firstCity)+sum(sorted(difference)[:len(costs)//2]))

# Send everyone to the first city and then get the difference
# of sending the person to the second city instead of the first
# Sort the difference array to get the cheaper B cities and send the employees there
# O(nlogn), O(n) space
costs = [[10,20],[30,200],[400,50],[30,20]]
minCosts = twoCitySchedCost(costs)
print(minCosts)
