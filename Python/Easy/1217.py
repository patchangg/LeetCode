
def minCostToMoveChips(position):
    even = 0
    odd = 0
    for i in position:
        if (i % 2) == 0:
            even += 1
        else:
            odd += 1
    return min(even,odd)


position = [1,2,3]
minCost = minCostToMoveChips(position)
print(minCost)
