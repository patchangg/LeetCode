import heapq

def furthestBuilding(heights, bricks, ladders):
    heap = []
    for i in range(len(heights)-1):
        distance = heights[i+1] - heights[i]
        if distance > 0:
            heapq.heappush(heap,distance)
        if len(heap) > ladders:
            bricks -= heapq.heappop(heap)
        if bricks < 0:
            return i
    return len(heights) - 1

# Use a heap to keep track of the heights of the buildings. Once we reach
# over the ladder limit, remove the smallest distance from the bricks.
# If there are no more bricks, return the building reached.
# If the loop is finished, return the length of the array.
# O(nlogn), O(n) space
heights = [4,2,7,6,9,14,12]
bricks = 5
ladders = 1
building = furthestBuilding(heights,bricks,ladders)
print(building)
