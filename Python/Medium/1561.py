
def maxCoins(piles):
    piles.sort()
    output = 0
    while piles:
        output += piles[-2]
        piles.pop()
        piles.pop()
        piles.pop(0)
    return output

# piles = [1,2,3,4,5,6,7,8,9]
# give bob the first index of the pile
# give Alice the max and give yourself the 2nd max
# another solution is to do range(len(piles)/3)
#  then pop() then add the next pop.val
piles = [9,8,7,6,5,1,2,3,4]
maximum = maxCoins(piles)
print(maximum)
