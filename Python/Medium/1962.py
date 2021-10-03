import heapq
import math

def minStoneSum(piles, k):
    arr = [-pile for pile in piles]
    heapq.heapify(arr)
    for i in range(k):
        heapq.heapreplace(arr,math.floor(arr[0]/2))
    return -sum(arr)

# Use a priority queue to get the highest number in the piles
# For k times, replace the highest number with the floor(number / 2)
# O(n+klogn), O(n) space
piles = [5,4,9]
k = 2
minStones = minStoneSum(piles,k)
print(minStones)
