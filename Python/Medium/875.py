import math

def minEatingSpeed(piles, h):
    left = 1
    right = max(piles)
    while left < right:
        middle = (left + right) // 2
        total = 0
        for pile in piles:
            total += math.ceil(pile / middle)
        if total > h:
            left = middle + 1
        else:
            right = middle
    return left

# Do a binary search to find the minimum amount of bananas to eat each hour
# While left < right, divide each pile by the middle to check if total per
# hour is still greater than h, if it is increment left, else right = middle
# which will make the range smaller. O(nlog(maxP)), O(1) space
piles = [3,6,7,11]
h = 8
minSpeed = minEatingSpeed(piles,h)
print(minSpeed)
